# PYTHON IMPORTS
import io
import logging
import os
from typing import List, Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from starlette.responses import Response
import aiofiles

# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from api.controllers.recorder import GetRecorderController
from api.models.recorder import EVENTS, Record, RecordListResponse
from api.routers import GetApp


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



@router.get("/load/{id}",  response_model=Record)
async def load(
    user: CurrentUser, recorderController: GetRecorderController, id: str
):
    return await recorderController.load_record(user.id, PydanticObjectId(id))


@router.post("/edit",  response_model=Record)
async def edit(
    user: CurrentUser,
    recorderController: GetRecorderController,
    id: str,
    name: str,
    description: str,
):
    return await recorderController.update_record(
        user.id, PydanticObjectId(id), name, description
    )


@router.post(
    "/start",
    
    description="Performs the start of a new Recording",
    response_model=Record,
)
async def start(
    project: str,
    user: CurrentUser,
    recorderController: GetRecorderController,
    name: str,
    description: Optional[str] = "",
):
    return await recorderController.start(
        name, user.id, PydanticObjectId(project), description
    )


@router.post(
    "/stop",
    
    description="Performs the stop of a Recording",
    response_model=bool,
)
async def stop(user: CurrentUser, recorderController: GetRecorderController):
    return await recorderController.stop()


@router.delete(
    "/remove",
    
    description="Performs the removal of a Recording",
    response_model=bool,
)
async def stop(
    record: str, user: CurrentUser, recorderController: GetRecorderController
):
    return await recorderController.delete_record(user.id, PydanticObjectId(record))


@router.get(
    "/running",
    
    description="Checks if a recorder is running",
    response_model=bool,
)
async def running(user: CurrentUser, recorderController: GetRecorderController):
    return await recorderController.running()


@router.get(
    "/events/count/{record_id}",
    
    description="Counts how many events in the recording",
    response_model=int,
)
async def event_count(
    record_id: str, user: CurrentUser, recorderController: GetRecorderController
):
    return await recorderController.count_record_events(
        user.id, PydanticObjectId(record_id)
    )


@router.get(
    "/event/list/{record_id}",
    
    description="List events in the recording",
    response_model=List[EVENTS],
)
async def event_list(
    record_id: str, user: CurrentUser, recorderController: GetRecorderController
):
    return await recorderController.load_record_events(
        user.id, PydanticObjectId(record_id)
    )


@router.get(
    "/frame/count/{record_id}",
    
    description="Counts how many frames in the recording",
    response_model=int,
)
async def frame_count(
    record_id: str, user: CurrentUser, recorderController: GetRecorderController
):
    return await recorderController.count_record_frames(
        user.id, PydanticObjectId(record_id)
    )


@router.get(
    "/size/{record_id}",
    
    description="Size in bytes of the recording",
    response_model=int,
)
async def size(
    record_id: str, user: CurrentUser, recorderController: GetRecorderController
):
    return await recorderController.size_of_record(user.id, PydanticObjectId(record_id))


@router.get("/frame/{record_id}/{frame_number}", operation_id="frame")
async def frame(
    record_id: str, frame_number: int, recorderController: GetRecorderController
):
    """API endpoint to serve a specific frame."""
    frame_bytes = await recorderController.load_record_frame(
        None, PydanticObjectId(record_id), frame_number
    )
    return StreamingResponse(io.BytesIO(frame_bytes), media_type="image/png")


@router.get("/video/{video_id}", operation_id="video")
async def video(video_id: str, app: GetApp, request: Request):
    path = os.path.join(app.state.config.recorder.video, video_id + ".mp4")

    async def video_stream():
        """Async generator to read video in chunks."""
        async with aiofiles.open(path, "rb") as video_file:
            while chunk := await video_file.read(1024):  # Read 1MB chunks
                yield chunk

    file_size = os.path.getsize(path)
    range_header = request.headers.get("range")

    if range_header:
        # Parse the range header
        start, end = range_header.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else file_size - 1
        chunk_size = end - start + 1

        async with aiofiles.open(path, "rb") as video_file:
            await video_file.seek(start)
            chunk = await video_file.read(chunk_size)

        headers = {
            "Content-Range": f"bytes {start}-{end}/{file_size}",
            "Accept-Ranges": "bytes",
            "Content-Length": str(chunk_size),
            "Content-Type": "video/mp4",
        }
        return Response(chunk, status_code=206, headers=headers)

    return StreamingResponse(video_stream(), media_type="video/mp4")


@router.get(
    "/list/{project_id}",
    
    response_model=RecordListResponse,
)
async def list(
    user: CurrentUser,
    recorderController: GetRecorderController,
    project_id: str,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    total, records = await recorderController.list_records(
        user.id, PydanticObjectId(project_id), skip, limit, search
    )
    return RecordListResponse(total=total, records=records)
