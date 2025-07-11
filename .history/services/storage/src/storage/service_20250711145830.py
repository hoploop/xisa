# PYTHON IMPORTS
from datetime import datetime
import logging
import os
from pathlib import Path
from typing import List, Optional, Tuple
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorGridFSBucket, AsyncIOMotorClient

# LOCAL IMPORTS
from common.models import MODELS
from common.models.storage import File
from common.rpc.storage_pb2 import StorageExistsRequest, StorageExistsResponse, StorageLoadByIdRequest, StorageLoadByIdResponse, StorageLoadRequest, StorageLoadResponse, StorageRemoveFolderRequest, StorageRemoveFolderResponse, StorageRemoveRequest, StorageRemoveResponse, StorageSaveRequest, StorageSaveResponse
from common.rpc.storage_pb2_grpc import StorageServicer
from common.rpc.player_pb2_grpc import PlayerServicer
from common.service import ClientConfig, Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)


class StorageServiceConfig(ServiceConfig):
    database: MongodbConfig
    path:str
    

class StorageService(Service, StorageServicer):

    def __init__(self, config: StorageServiceConfig):
        PlayerServicer.__init__(self)
        Service.__init__(self)
        self.config: StorageServiceConfig = config
        self.root: str = os.path.join(os.getcwd(),self.config.path)

    async def start(self): 
        self.db, self.fs = await Mongodb.initialize(self.config.database, MODELS)
        
    def _get_fs_bucket(self, bucket_name: str) -> AsyncIOMotorGridFSBucket:
        """
        Get a GridFS bucket for a given bucket name.
        """
        return AsyncIOMotorGridFSBucket(self.db, bucket_name=bucket_name)

    async def store_file(
        self,
        file_path: Path,
        bucket_name: str,
        content_type: Optional[str] = None
    ) -> str:
        """
        Upload a file into a specific GridFS bucket and create metadata.
        :param file_path: Path to the local file.
        :param bucket_name: The GridFS bucket name for this file.
        :param content_type: Optional MIME type.
        :return: File ID as a string.
        """
        fs_bucket = self._get_fs_bucket(bucket_name)
        file_size = file_path.stat().st_size  # Get file size from disk
        
        grid_in = fs_bucket.open_upload_stream(filename=file_path.name,
            metadata={"content_type": content_type})

        with open(file_path, "rb") as f:
            grid_in.write(f.read())
        
        file_id = str(grid_in._id)
        grid_in.close()

        # Save metadata in Beanie
        file_doc = File(
            filename=file_path.name,
            content_type=content_type,
            length=file_size,
            id=grid_in._id,
            bucket=bucket_name
        )
        await file_doc.insert()
        return file_id

    async def list_files(self, bucket_name: Optional[str] = None) -> List[File]:
        """
        List all files, optionally filtered by bucket.
        :param bucket_name: Filter files by bucket name.
        """
        query = File.find_all()
        if bucket_name:
            query = File.find(File.bucket == bucket_name)
        return await query.sort("filename").to_list()

    async def download_file(self, file_id: str, destination: Path) -> None:
        """
        Download a file from GridFS, automatically selecting the right bucket.
        """
        file_doc = await File.get(ObjectId(file_id))
        if not file_doc:
            raise FileNotFoundError(f"File with ID {file_id} not found.")
        fs_bucket = self._get_fs_bucket(file_doc.bucket)
        grid_out = fs_bucket.open_download_stream(ObjectId(file_id))
        data = grid_out.read()
        with open(destination, "wb") as f:
            f.write(data)

    async def remove_file(self, file_id: str) -> None:
        """
        Remove a file from GridFS and its metadata.
        """
        file_doc = await File.get(ObjectId(file_id))
        if not file_doc:
            raise FileNotFoundError(f"File with ID {file_id} not found.")
        fs_bucket = self._get_fs_bucket(file_doc.bucket)
        await fs_bucket.delete(ObjectId(file_id))
        await file_doc.delete()  
        
    async def get_file_by_name(self, bucket_name: str, filename: str) -> Optional[File]:
        """
        Find a file metadata document by bucket and filename.
        """
        return await File.find_one(File.bucket == bucket_name, File.filename == filename)

    async def read_file_by_name(self, bucket_name: str, filename: str) -> Tuple[bytes,str,int]:
        """
        Read file content from GridFS directly by bucket and filename.
        """
        file_doc = await self.get_file_by_name(bucket_name, filename)
        file_meta = await File.find(File.filename == filename,File.folder==bucket_name).first_or_none()
        if not file_doc:
            raise FileNotFoundError(f"File '{filename}' in bucket '{bucket_name}' not found.")
        data = await self.read_file_bytes(str(file_doc.id))
        return data,file_meta.content_type,file_meta.length

        
    async def read_file_bytes(self, file_id: str) -> bytes:
        """
        Read a file directly from GridFS into memory as bytes.
        """
        file_doc = await File.get(ObjectId(file_id))
        if not file_doc:
            raise FileNotFoundError(f"File with ID {file_id} not found.")
        fs_bucket = self._get_fs_bucket(file_doc.bucket)
        grid_out = await fs_bucket.open_download_stream(ObjectId(file_id))
        data = b"".join([chunk async for chunk in grid_out])
        return data
        
    async def write_file_bytes(
        self,
        data: bytes,
        filename: str,
        bucket_name: str,
        content_type: Optional[str] = None
    ) -> PydanticObjectId:
        """
        Upload file data from bytes directly into GridFS.
        :param data: File content as bytes.
        :param filename: Name to save in GridFS.
        :param bucket_name: The GridFS bucket name.
        :param content_type: Optional MIME type.
        :return: File ID as a string.
        """
        fs_bucket = self._get_fs_bucket(bucket_name)
        grid_in = fs_bucket.open_upload_stream(
            filename=filename,
            metadata={"content_type": content_type}
        ) 
        grid_in.write(data)
        file_id = grid_in._id
        grid_in.close()
        # Save metadata
        file_doc = File(
            filename=filename,
            content_type=content_type,
            length=0,
            id=grid_in._id,
            bucket=bucket_name
        )
        await file_doc.insert()
        return file_id
    
    async def remove_bucket(self, bucket_name: str) -> None:
        """
        Delete all files in a GridFS bucket and remove associated metadata.
        """
        # Drop GridFS collections for the bucket
        files_coll = f"{bucket_name}.files"
        chunks_coll = f"{bucket_name}.chunks"
        await self.db.drop_collection(files_coll)
        await self.db.drop_collection(chunks_coll)

        # Remove metadata documents
        await File.find(File.bucket == bucket_name).delete()
        
    async def storageSave(self, request: StorageSaveRequest, context) -> StorageSaveResponse:
        try:
            file_id = await self.write_file_bytes(request.data,request.filename,request.folder,request.content_type)
            ref = File(filename=request.filename,bucket=request.folder,context_type=request.content_type)
            folder_path = os.path.join(self.root,request.folder)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            file_path = os.path.join(folder_path,request.filename)
            with open(file_path,'wb') as f:
                f.write(request.data)
            await ref.save()
            return StorageSaveResponse(status=True,id=str(file_id))
        except Exception as e:
            log.warning(str(e))
            return StorageSaveResponse(status=False,message=str(e))
        
    async def storageLoad(self, request: StorageLoadRequest, context) -> StorageLoadResponse:
        try:
            found = await File.find(File.filename== request.filename,File.folder==request.folder).first_or_none()
            if not found:
                return StorageRemoveResponse(status=False,message="File not found")
            folder_path = os.path.join(self.root,request.folder)
            file_path = os.path.join(folder_path,request.filename)
            with open(file_path,'rb') as f:
                data = f.read()
            data = await self.read_file_bytes(found.id)
            return StorageLoadResponse(status=True,data=data,content_type=found.content_type,size=found.length)
        except Exception as e:
            log.warning(str(e))
            return StorageLoadResponse(status=False,message=str(e))
    
    async def storageLoadById(self, request: StorageLoadByIdRequest, context) -> StorageLoadByIdResponse:
        try:
            found = await File.find(File.id == PydanticObjectId(request.id)).first_or_none()
            if not found:
                return StorageRemoveResponse(status=False,message="File not found")
            data = await self.read_file_bytes(found.id)
            return StorageLoadByIdResponse(status=True,data=data,content_type=found.content_type,size=found.length)
        except Exception as e:
            log.warning(str(e))
            return StorageLoadByIdResponse(status=False,message=str(e))
    
        
    async def storageRemove(self, request: StorageRemoveRequest, context) -> StorageRemoveResponse:
        try:
            found = await File.find(File.filename== request.filename,File.folder==request.folder).first_or_none()
            if not found:
                return StorageRemoveResponse(status=False,message="File not found")
            await self.remove_file(found.id)
            return StorageRemoveResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return StorageRemoveResponse(status=False,message=str(e))
        
    async def storageRemoveFolder(self, request: StorageRemoveFolderRequest, context) -> StorageRemoveFolderResponse:
        try:
            await self.remove_bucket(request.folder)
            return StorageRemoveFolderResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return StorageRemoveFolderResponse(status=False,message=str(e))
        
    async def storageExists(self, request: StorageExistsRequest, context) -> StorageExistsResponse:
        try:
            found = await File.find(File.filename==request.filename,File.folder == request.folder).first_or_none()
            if not found:
                return StorageExistsResponse(status=True,exists=False)
            return StorageExistsResponse(status=True,exists=True)
        except Exception as e:
            log.warning(str(e))
            return StorageExistsResponse(status=False,message=str(e))
        
    