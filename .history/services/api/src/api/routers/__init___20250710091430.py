
# PYTHON IMPORTS
from typing import Annotated

# LIBRARY IMPORTS
from uuid import uuid4
from fastapi import Depends, FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorGridFSBucket


async def get_host(request: Request) -> str:
    return request.client.host

async def get_session(request:Request) -> str:
    session = request.headers.get('X-Session',str(uuid4()))
    return session

async def get_app(request: Request) -> FastAPI:
    return request.app

async def get_filesystem(request: Request) ->  AsyncIOMotorGridFSBucket:
    return request.app.state.fs

async def get_config(request: Request):
    return request.app.state.config

GetFilesystem = Annotated[AsyncIOMotorGridFSBucket,Depends(get_filesystem)]
GetHost = Annotated[str,Depends(get_host)]
GetSession = Annotated[str,Depends(get_session)]
GetApp = Annotated[FastAPI,Depends(get_app)]


'''
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

    '''