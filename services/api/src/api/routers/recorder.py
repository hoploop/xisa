# PYTHON IMPORTS
import io
import logging
import os
from typing import Annotated, List, Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from starlette.responses import Response

# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from common.clients.recorder import RecorderClient
from common.models.recorder import EVENTS, Record
from api.routers import GetApp


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_recorder(request: Request) -> RecorderClient:
    if not hasattr(request.app.state, "recorder"):
        config = request.app.state.config.recorder
        request.app.state.recorder = RecorderClient(config)
        await request.app.state.recorder.startup()
    return request.app.state.recorder

Recorder = Annotated[RecorderClient, Depends(get_recorder)]


@router.get("/load/{recorderId}", response_model=Record)
async def load(user: CurrentUser, recorder: Recorder, recorderId: PydanticObjectId):
    try:
        return await recorder.loadRecord(user, recorderId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post("/edit", response_model=Record)
async def edit(
    user: CurrentUser,
    recorder: Recorder,
    recordId: PydanticObjectId,
    name: str,
    description: str,
):
    try:
        return await recorder.updateRecord(user, recordId, name, description)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/start",
    description="Performs the start of a new Recording",
    response_model=Record,
)
async def start(
    projectId: PydanticObjectId,
    user: CurrentUser,
    recorder: Recorder,
    name: str,
    description: Optional[str] = "",
):
    try:
        return await recorder.startRecord(user, projectId, name, description)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/stop",
    description="Performs the stop of a Recording",
    response_model=bool,
)
async def stop(user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.stopRecord(user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.delete(
    "/remove",
    description="Performs the removal of a Recording",
    response_model=bool,
)
async def remove(recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.deleteRecord(user, recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/running",
    description="Checks if a recorder is running",
    response_model=bool,
)
async def running(user: CurrentUser, recorder: Recorder):
    return await recorder.running()


@router.get(
    "/events/count/{recordId}",
    description="Counts how many events in the recording",
    response_model=int,
)
async def event_count(
    recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.countRecordEvent(user, recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/event/list/{recordId}",
    description="List events in the recording",
    response_model=List[EVENTS],
)
async def event_list(recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.listRecordEvent(user, recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/frame/count/{recordId}",
    description="Counts how many frames in the recording",
    response_model=int,
)
async def frame_count(recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.countRecordFrame(user,recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/size/{recordId}",
    description="Size in bytes of the recording",
    response_model=int,
)
async def size(recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.sizeRecord(user,recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get("/frame/{recordId}/{frame}", operation_id="frame")
async def frame(recordId: PydanticObjectId, frame: int, recorder: Recorder):
    try:
        frame_bytes = await recorder.loadRecordFrame('',recordId,frame)
        return StreamingResponse(io.BytesIO(frame_bytes), media_type="image/png")    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
    


@router.get("/video/{recordId}", operation_id="video")
async def video(recordId: PydanticObjectId, app: GetApp,user:CurrentUser, request: Request,recorder:Recorder):
    video_stream = await recorder.streamRecordVideo(user,recordId)

    async def video_generator():
        for chunk in video_stream:
            yield chunk.chunk_data

    file_size = await recorder.sizeRecordVideo(user,recordId)
    range_header = request.headers.get("range")

    if range_header:
        # Parse the range header
        start, end = range_header.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else file_size - 1
        chunk_size = end - start + 1

        chunk = await recorder.streamRangeRecordVideo(user,recordId)

        headers = {
            "Content-Range": f"bytes {start}-{end}/{file_size}",
            "Accept-Ranges": "bytes",
            "Content-Length": str(chunk_size),
            "Content-Type": "video/mp4",
        }
        return Response(chunk, status_code=206, headers=headers)

    return StreamingResponse(video_generator(), media_type="video/mp4")


class RecordListResponse(BaseModel):
    records: List[Record]
    total: int


@router.get(
    "/list/{projectId}",
    response_model=RecordListResponse,
)
async def list(
    user: CurrentUser,
    recorder: Recorder,
    projectId: PydanticObjectId,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    try:
        total, records = await recorder.listRecord(user, projectId, skip, limit, search)
        return RecordListResponse(total=total, records=records)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/record/count/{projectId}",
    response_model=int,
)
async def record_count(
    projectId: PydanticObjectId, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.countRecord(user, projectId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
