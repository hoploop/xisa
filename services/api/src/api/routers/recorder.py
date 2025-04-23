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
from common.models.recorder import EVENTS, Action, Record
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


@router.get("/load/{recorderId}", 
            operation_id="recorderLoad",
            response_model=Record)
async def load(user: CurrentUser, recorder: Recorder, recorderId: PydanticObjectId):
    try:
        return await recorder.loadRecord(user, recorderId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post("/edit", 
             operation_id="recorderEdit",
             response_model=Record)
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
    operation_id="recorderStart",
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
    operation_id="recorderStop",
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
    operation_id="recorderRemove",
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
    operation_id="recorderRunning",
    description="Checks if a recorder is running",
    response_model=bool,
)
async def running(user: CurrentUser, recorder: Recorder):
    return await recorder.running()


@router.get(
    "/event/count/{recordId}",
    operation_id="recorderEventCount",
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
    "/event/load/{eventId}",
    operation_id="recorderEventLoad",
    description="Loads a specific event",
    response_model=EVENTS,
)
async def event_load(eventId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.loadEvent(user, eventId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/event/list/{recordId}",
    operation_id="recorderEventList",
    description="List events in the recording",
    response_model=List[EVENTS],
)
async def event_list(recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.listRecordEvent(user, recordId)
    except Exception as e:
        log.warning(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/frame/count/{recordId}",
    operation_id="recorderFrameCount",
    description="Counts how many frames in the recording",
    response_model=int,
)
async def frame_count(
    recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.countRecordFrame(user, recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/size/{recordId}",
    operation_id="recorderSize",
    description="Size in bytes of the recording",
    response_model=int,
)
async def size(recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.sizeRecord(user, recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get("/frame/{recordId}/{frame}", 
            operation_id="recorderFrameLoad")
async def frame_load(
    recordId: PydanticObjectId, user: CurrentUser, frame: int, recorder: Recorder
):
    try:
        frame_bytes = await recorder.loadRecordFrame(user, recordId, frame)
        return StreamingResponse(io.BytesIO(frame_bytes), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get("/frame/thumbnail/{recordId}/{frame}", 
            operation_id="recorderFrameThumbnailLoad")
async def frame_load_thumbnail(
    recordId: PydanticObjectId, user: CurrentUser, frame: int, recorder: Recorder
):
    try:
        frame_bytes = await recorder.loadRecordFrame(user, recordId, frame,True)
        return StreamingResponse(io.BytesIO(frame_bytes), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get("/video/{recordId}", 
            operation_id="recorderVideo")
async def video(
    recordId: PydanticObjectId,
    app: GetApp,
    user: CurrentUser,
    request: Request,
    recorder: Recorder,
):
    try:

        async def video_generator():
            video_stream = await recorder.streamRecordVideo(user, recordId)
            for chunk in video_stream:
                yield chunk.chunk_data

        file_size = await recorder.sizeRecordVideo(user, recordId)
        log.debug('Downloading video file with size: {0}'.format(file_size))
        range_header = request.headers.get("range")
        
        def _invalid_range():
            return HTTPException(
                status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE,
                detail=f"Invalid request range (Range:{range_header!r})",
            )

        if range_header:
            # Parse the range header
            start, end = range_header.replace("bytes=", "").split("-")
            start = int(start)
            # end = min(int(end), file_size - 1)
            end = int(end) if end else file_size - 1
            #end = min(end,file_size)
            chunk_size = end - start + 1
            
            
            #if end > file_size -1:
            #    end = file_size
                
            log.debug('Returning chunk: {0} -> {1}'.format(start,end))
            
            #if start > end or start < 0 or end > file_size - 1:
            #    raise _invalid_range()

            chunk = await recorder.streamRangeRecordVideo(user, recordId, start, end)

            headers = {
                "Content-Range": f"bytes {start}-{end}/{file_size}",
                "Accept-Ranges": "bytes",
                "Content-Length": str(len(chunk)),
                "Content-Type": "video/mp4",
            }
            return Response(chunk, status_code=206, headers=headers)

        return StreamingResponse(
            video_generator(), media_type="video/mp4", headers={"Accept-Ranges": "bytes"}
        )
    except Exception as e:
        log.warning(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class RecordListResponse(BaseModel):
    records: List[Record]
    total: int


@router.get(
    "/list/{projectId}",
    operation_id="recorderList",
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
    operation_id="recorderCount",
    response_model=int,
)
async def count(
    projectId: PydanticObjectId, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.countRecord(user, projectId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class RecordActionListResponse(BaseModel):
    actions: List[Action]
    total:int
    


@router.get(
    "/list/action/{recordId}",
    operation_id="recorderActionList",
    response_model=RecordActionListResponse,
)
async def action_list(
    user: CurrentUser,
    recorder: Recorder,
    recordId: PydanticObjectId,
    eventId: Optional[PydanticObjectId]=None,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    try:
        total, actions = await recorder.listRecordAction(user, recordId,eventId, skip, limit, search)
        return RecordActionListResponse(total=total, actions=actions)
    except Exception as e:
        log.debug(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/list/action/frame/{recordId}",
    operation_id="recorderActionListByFrame",
    response_model=List[Action],
)
async def action_list_by_frame(
    user: CurrentUser,
    recorder: Recorder,
    recordId: PydanticObjectId,
    frame:int
):
    try:
        return await recorder.listRecordActionByFrame(user, recordId,frame)
    except Exception as e:
        log.debug(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/record/action/count/{recordId}",
    operation_id="recorderActionCount",
    response_model=int,
)
async def action_count(
    recordId: PydanticObjectId, user: CurrentUser, recorder: Recorder,eventId: Optional[PydanticObjectId]=None,search:str=None
):
    try:
        return await recorder.countRecordAction(user,recordId,eventId,search)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/record/action/remove",
    operation_id="recorderActionRemove",
    response_model=bool,
)
async def action_remove(
    actionId: PydanticObjectId, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.removeRecordAction(user,actionId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class RecordActionCreatePayload(BaseModel):
    recordId:PydanticObjectId
    eventId:PydanticObjectId
    byLabel: Optional[str]=None
    byText: Optional[str]=None
    byRegex: Optional[str]=None
    byOrder: List[int] = []
    byPosition: List[float] = []
    confidence: float
    image: Optional[str]=None
    

@router.post(
    "/record/action/create",
    operation_id="recorderActionCreate",
    response_model=Action,
)
async def action_create(
    payload: RecordActionCreatePayload, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.createRecordAction(user,payload.recordId,payload.eventId,payload.byLabel,payload.byText,payload.byRegex,payload.byOrder,payload.byPosition,payload.confidence,payload.image)
    except Exception as e:
        log.warning(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class RecordActionUpdatePayload(BaseModel):
    actionId:PydanticObjectId
    eventId:PydanticObjectId
    byLabel: Optional[str]=None
    byText: Optional[str]=None
    byRegex: Optional[str]=None
    byOrder: List[int] = []
    byPosition: List[float] = []
    confidence: float
    image: Optional[str]=None
    

@router.put(
    "/record/action/update",
    operation_id="recorderActionUpdate",
    response_model=Action,
)
async def action_update(
    payload: RecordActionUpdatePayload, user: CurrentUser, recorder: Recorder
):
    try:
        return await recorder.updateRecordAction(user,payload.actionId,payload.eventId,payload.byLabel,payload.byText,payload.byRegex,payload.byOrder,payload.byPosition,payload.confidence,payload.image)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/record/action/load/{actionId}",
    operation_id="recorderActionLoad",
    response_model=Action,
)
async def action_load(
    actionId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.loadRecordAction(user,actionId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/record/action/event/{eventId}",
    operation_id="recorderActionLoadByEvent",
    response_model=Action,
)
async def action_load_by_event(
    eventId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.loadRecordActionByEvent(user,eventId)
    except Exception as e:
        log.warning(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/record/event/action/exist/{eventId}",
    operation_id="recorderEventActionExist",
    response_model=bool,
)
async def event_action_exist(
    eventId: PydanticObjectId, user: CurrentUser, recorder: Recorder):
    try:
        return await recorder.existRecordEventAction(user,eventId)
    except Exception as e:
        log.warning(str(e))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
