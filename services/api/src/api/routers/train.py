# PYTHON IMPORTS
import io
import logging
from bson import ObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response


# LOCAL IMPORTS
from api.routers import GetFilesystem


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)

@router.post("/image/upload/",operation_id="image_upload")
async def upload_file(fs:GetFilesystem,file: UploadFile = File(...)):
    file_content = await file.read()  # Read file as bytes
    file_id: ObjectId = await fs.upload_from_stream(file.filename, io.BytesIO(file_content), metadata={"content_type": file.content_type})
    return {"filename": file.filename, "status": "success","id":str(file_id)}


@router.get("/image/download/{file_id}",operation_id="image_download",response_model=str)
async def get_image(file_id: str,fs:GetFilesystem):
    """ Retrieve image from MongoDB GridFS """
    grid_out = await fs.open_download_stream(ObjectId(file_id))
    data = await grid_out.read()
    base64_image = base64.b64encode(data).decode('utf-8')
    return base64_image

    