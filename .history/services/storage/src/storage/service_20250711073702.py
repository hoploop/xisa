# PYTHON IMPORTS
from datetime import datetime
import logging
from pathlib import Path
from typing import List, Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from motor.motor_asyncio import AsyncIOMotorGridFSBucket, AsyncIOMotorClient

# LOCAL IMPORTS
from common.models import MODELS
from common.models.storage import File
from common.rpc.storage_pb2_grpc import StorageServicer
from common.rpc.player_pb2_grpc import PlayerServicer
from common.service import ClientConfig, Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)


class StorageServiceConfig(ServiceConfig):
    database: MongodbConfig
    

class StorageService(Service, StorageServicer):

    def __init__(self, config: StorageServiceConfig):
        PlayerServicer.__init__(self)
        Service.__init__(self)
        self.config: StorageServiceConfig = config

    async def start(self):
        db, fs = await Mongodb.initialize(self.config.database, MODELS)
        
    async def store_file(self, file_path: Path, content_type: Optional[str] = None) -> str:
        """
        Store a file in GridFS and create metadata in MongoDB.
        :param file_path: Path to local file to upload.
        :param content_type: MIME type of file (optional).
        :return: File ID as a string.
        """
        async with await self.fs_bucket.open_upload_stream(
            filename=file_path.name, metadata={"content_type": content_type}
        ) as grid_in:
            with open(file_path, "rb") as f:
                await grid_in.write(f.read())
            file_id = str(grid_in._id)

        # Save metadata separately in Beanie collection
        metadata = File(
            filename=file_path.name,
            content_type=content_type,
            length=grid_in.length,
            id=grid_in._id
        )
        await metadata.insert()
        return file_id

    async def list_files(self) -> List[File]:
        """
        List all stored files with metadata.
        :return: List of FileMetadata documents.
        """
        return await File.find_all().sort([("filename", ASCENDING)]).to_list()

    async def download_file(self, file_id: str, destination: Path) -> None:
        """
        Download a file from GridFS to a local path.
        :param file_id: The ID of the file in GridFS.
        :param destination: Path to save the downloaded file.
        """
        from bson import ObjectId
        async with await self.fs_bucket.open_download_stream(ObjectId(file_id)) as grid_out:
            data = await grid_out.read()
            with open(destination, "wb") as f:
                f.write(data)

    async def remove_file(self, file_id: str) -> None:
        """
        Delete a file from GridFS and remove its metadata.
        :param file_id: The ID of the file in GridFS.
        """
        from bson import ObjectId
        await self.fs_bucket.delete(ObjectId(file_id))
        await FileMetadata.find_one(FileMetadata.id == ObjectId(file_id)).delete()        
        