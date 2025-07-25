# PYTHON IMPORTS
from io import BytesIO
import logging
import traceback
import os
import shutil

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, In, RegEx, NotIn
from PIL import Image

# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True

# LOCAL IMPORTS
from common.clients.api import ApiClient
from common.clients.auth import AuthClient
from common.clients.recorder import RecorderClient
from common.clients.storage import StorageClient
from common.clients.trainer import TrainerClient
from common.models import MODELS
from common.models.auth import User
from common.models.base import Box, Position
from common.models.detector import (
    Detector,
    DetectorLabel,
    DetectorImage,
    DetectorImageLabel,
    DetectorImageMode,
    DetectorSuggestion,
)
from common.rpc.detector_pb2 import (
    AddDetectorLabelRequest,
    AddDetectorLabelResponse,
    AddDetectorImageLabelRequest,
    AddDetectorImageLabelResponse,
    CanRemoveDetectorLabelRequest,
    CanRemoveDetectorLabelResponse,
    CountDetectorLabelRequest,
    CountDetectorLabelResponse,
    CountDetectorImageLabelRequest,
    CountDetectorImageLabelResponse,
    CountDetectorImageRequest,
    CountDetectorImageResponse,
    CountDetectorRequest,
    CountDetectorResponse,
    CreateDetectorResponse,
    DetectContoursRequest,
    DetectContoursResponse,
    DetectObjectsRequest,
    DetectObjectsResponse,
    DetectTextsRequest,
    DetectTextsResponse,
    DetectorImageRequest,
    DetectorImageResponse,
    ExistsDetectorLabelRequest,
    ExistsDetectorLabelResponse,
    FindDetectorImageLabelResponse,
    ListDetectorLabelRequest,
    ListDetectorLabelResponse,
    ListDetectorImageLabelRequest,
    ListDetectorImageLabelResponse,
    ListDetectorImageRequest,
    ListDetectorImageResponse,
    ListDetectorRequest,
    ListDetectorResponse,
    LoadDetectorLabelRequest,
    LoadDetectorLabelResponse,
    LoadDetectorRequest,
    LoadDetectorResponse,
    RemoveDetectorImageLabelRequest,
    RemoveDetectorImageLabelResponse,
    RemoveDetectorImageRequest,
    RemoveDetectorImageResponse,
    RemoveDetectorLabelRequest,
    RemoveDetectorLabelResponse,
    RemoveDetectorRequest,
    RemoveDetectorResponse,
    SuggestStepRequest,
    SuggestStepResponse,
    TrainDetectorRequest,
    TrainDetectorResponse,
    TrainResultRequest,
    TrainResultResponse,
    UpdateDetectorRequest,
    UpdateDetectorResponse,
    UploadDetectorImageRequest,
    UploadDetectorImageResponse,
    DetectorImageMode as GrpcDetectorImageMode,
)
from common.service import Service
from common.rpc.detector_pb2_grpc import DetectorServicer
from common.utils.conversions import Conversions
from common.utils.imaging import ImageGrid
from common.utils.mongodb import Mongodb
from detector.config import DetectorServiceConfig
from detector.manager import DetectorManager
from detector.controllers.graphics import GraphicsController
from detector.controllers.detector import DetectorController
from detector.controllers.object import ObjectController
from detector.controllers.contour import ContourController
from detector.controllers.text import TextController

# INITIALIZATION
log = logging.getLogger(__name__)


class DetectorService(Service, DetectorServicer):

    def __init__(self, config: DetectorServiceConfig):
        DetectorServicer.__init__(self)
        Service.__init__(self)
        self.config: DetectorServiceConfig = config
        self.api = ApiClient(self.config.api)
        self.recorder = RecorderClient(self.config.recorder)
        self.trainer = TrainerClient(self.config.trainer)
        self.auth = AuthClient(self.config.auth)
        self.storage = StorageClient(self.config.storage)

    async def start(self):
        await Mongodb.initialize(self.config.database, MODELS)

        # Yolos models cached in memory
        self.CACHE_YOLOS = {}

        # Starting up recorder client connectibity
        await self.recorder.startup()
        await self.api.startup()
        await self.trainer.startup()
        await self.storage.startup()

    async def findDetectorImageLabel(self, request, context):
        try:
            found = await DetectorLabel.find_many(
                DetectorLabel.detector == PydanticObjectId(request.detector),
                DetectorLabel.name == request.name,
            ).first_or_none()
            if found is not None:
                return FindDetectorImageLabelResponse(
                    status=True, label=Conversions.serialize(found)
                )
            return FindDetectorImageLabelResponse(
                status=False, message="detector.label.errors.not_found"
            )
        except Exception as e:
            log.warning(str(e))
            return FindDetectorImageLabelResponse(status=False, message=str(e))

    async def loadDetectorLabel(
        self, request: LoadDetectorLabelRequest, context
    ) -> LoadDetectorLabelResponse:
        try:
            label_id = PydanticObjectId(request.id)
            label = await DetectorLabel.find(
                DetectorLabel.id == label_id
            ).first_or_none()
            if label:
                return LoadDetectorLabelResponse(
                    status=True, label=Conversions.serialize(label)
                )
            else:
                return LoadDetectorLabelResponse(
                    status=False, message="detector.errors.label_not_found"
                )
        except Exception as e:
            log.warning(str(e))
            return LoadDetectorLabelResponse(status=False, message=str(e))

    async def suggestStep(
        self, request: SuggestStepRequest, context
    ) -> SuggestStepResponse:
        try:
            user = await User.find_many(
                User.id == PydanticObjectId(request.user)
            ).first_or_none()
            event = await self.recorder.loadEvent(user, PydanticObjectId(request.event))
            
            log.debug ("Loading image")
            img = GraphicsController.load_pil_image_from_base64_string(request.data)            
            width, height = img.size
            log.debug("Image loaded")

            if event.position:
                x, y = event.position
            else:
                x = 0
                y = 0

            # Matching texts
            req = DetectTextsRequest(
                user=request.user, data=request.data, confidence=request.confidence
            )
            log.debug("Detecting texts")
            res = await self.detectTexts(req, context)

            suggestions = []

            if res.status == True:
                matched = None
                for text in res.texts:
                    nx = text.x
                    ny = text.y
                    nw = text.w
                    nh = text.h

                    if x > nx and x < (nx + nw) and y > ny and y < (ny + nh):
                        matched = text
                        log.debug(
                            "detected Text: {0},{1} ({2},{3}) - '{4}'".format(
                                nx, ny, nw, nh, matched.value
                            )
                        )
                        break

                # Now checking if it is unique
                if matched:
                    others = []
                    for text in res.texts:
                        if text != matched and text.value == matched.value:
                            others.append(text)

                    # There are no other texts with same value, suggestion is unique for text
                    if len(others) == 0:
                        suggestions.append(
                            DetectorSuggestion(
                                event=PydanticObjectId(request.event),
                                by_text=matched.value,
                                confidence=matched.confidence,
                                x=nx,
                                y=ny,
                                w=nw,
                                h=nh,
                            )
                        )

                    else:
                        suggestions.append(
                            DetectorSuggestion(
                                event=PydanticObjectId(request.event),
                                by_text=matched.value,
                                by_order=[matched.line, matched.block],
                                x=nx,
                                y=ny,
                                w=nw,
                                h=nh,
                                confidence=matched.confidence,
                            )
                        )

            # Mathing objects
            log.debug("Detecting objects")
            req = DetectObjectsRequest(
                user=request.user,
                data=request.data,
                detector=request.detector,
                confidence=request.confidence,
            )
            res = await self.detectObjects(req, context)

            # DetectObject(x=x,y=y,w=w,h=h,confidence=confidence,code=code,name=name,row=row,col=col

            if res.status == True:
                matches = []
                for obj in res.objects:
                    log.debug(
                        "Detected object: "
                        + obj.name
                        + " now checking if it matches the area"
                    )
                    nx = obj.x  # * width
                    ny = obj.y  # * height
                    nw = obj.w  # * width
                    nh = obj.h  # * height

                    if x > nx and x < (nx + nw) and y > ny and y < (ny + nh):
                        matches.append(obj)

                # Now checking if it is unique
                for matched in matches:
                    others = []
                    for obj in res.objects:
                        if obj != matched and matched.name == obj.name:
                            others.append(obj)

                    if matched.w / width < 0.7 and matched.h / height < 0.7:

                        # There are no other objects with same value
                        if len(others) == 0:
                            suggestions.append(
                                DetectorSuggestion(
                                    event=PydanticObjectId(request.event),
                                    by_label=matched.name,
                                    confidence=matched.confidence,
                                    x=matched.x,
                                    y=matched.y,
                                    w=matched.w,
                                    h=matched.h,
                                )
                            )

                        else:
                            suggestions.append(
                                DetectorSuggestion(
                                    event=PydanticObjectId(request.event),
                                    by_label=matched.name,
                                    by_order=[matched.row, matched.col],
                                    x=matched.x,
                                    y=matched.y,
                                    w=matched.w,
                                    h=matched.h,
                                    confidence=matched.confidence,
                                )
                            )
                            
             # Mathing contouts
            log.debug("Detecting contours")
            req = DetectContoursRequest(
                user=request.user,
                data=request.data,
                confidence=request.confidence,
            )
            res: DetectContoursResponse = await self.detectContours(req, context)


            if res.status == True:
                matches = []
                for ctr in res.contours:
                    
                    nx = ctr.x  # * width
                    ny = ctr.y  # * height
                    nw = ctr.w  # * width
                    nh = ctr.h  # * height
                    conf = ctr.confidence
                    row = ctr.row
                    col = ctr.col

                    if x > nx and x < (nx + nw) and y > ny and y < (ny + nh):
                        suggestions.append(
                        DetectorSuggestion(
                            event=PydanticObjectId(request.event),
                            by_contour=Box(x=ctr.x,y=ctr.y,w=ctr.w,h=ctr.h),
                            by_order= [row,col],
                            confidence=conf,
                            x=nx,
                            y=ny,
                            w=nw,
                            h=nh,
                        )
                        )

                      
            xs = x - (20 / width)
            ys = y - (20 / height)
            w = 40 / width
            h = 40 / height

            log.debug("Adding actual position")
            suggestions.append(
                DetectorSuggestion(
                    event=PydanticObjectId(request.event),
                    by_position=Position(x=x, y=y),
                    x=xs,
                    y=ys,
                    w=w,
                    h=h,
                    confidence=0.5,
                )
            )
            ret = []

            log.debug("Serializing results")
            for su in suggestions:
                ret.append(Conversions.serialize(su))

            return SuggestStepResponse(status=True, suggestions=ret)

        except Exception as e:
            log.warning(str(e))
            return SuggestStepResponse(status=False, message=str(e))

    async def detectTexts(
        self, request: DetectTextsRequest, context
    ) -> DetectTextsResponse:
        try:
            img = GraphicsController.load_pil_image_from_base64_string(request.data)
            texts = TextController.detect_texts(img,request.confidence)
            return DetectTextsResponse(status=True, texts=texts)
        except Exception as e:
            log.warning(str(e))
            return DetectTextsResponse(status=False, message=str(e))
        
    async def detectContours(self, request: DetectContoursRequest, context) -> DetectContoursResponse:
        try:
            img = GraphicsController.load_pil_image_from_base64_string(request.data)
            edges, contours, hierarchy = ContourController.detect_contours(img)
            elements = ContourController.build_contours(img,edges,contours)
            return DetectContoursResponse(status=True,contours=elements)
            
        except Exception as e:
            log.warning(str(e))
            return DetectContoursResponse(status=False,message=str(e))

    async def detectObjects(
        self, request: DetectObjectsRequest, context
    ) -> DetectObjectsResponse:
        try:
            detector = await DetectorController.load_detector(request.detector)
            model = ObjectController.load_yolo(self.config.path,self.config.name,detector)
            img = GraphicsController.load_pil_image_from_base64_string(request.data)
            objects = ObjectController.detect_objects(model,img,request.confidence)
            return DetectObjectsResponse(status=True, objects=objects)
        except Exception as e:
            log.warning(str(e))
            return DetectObjectsResponse(status=False, message=str(e))

    async def removeDetectorImage(
        self, request: RemoveDetectorImageRequest, context
    ) -> RemoveDetectorImageResponse:
        try:
            image_id = PydanticObjectId(request.id)
            user_id = PydanticObjectId(request.user)
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return RemoveDetectorImageResponse(
                    status=False, message="detector.image.errors.not_found"
                )

            log.debug("Removing detector image")
            await found.delete()
            return RemoveDetectorImageResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            print(traceback.format_exc())
            return RemoveDetectorImageResponse(status=False, message=str(e))

    async def countDetectorImage(
        self, request: CountDetectorImageRequest, context
    ) -> CountDetectorImageResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not found:
                return ListDetectorImageResponse(
                    status=False, message="detector.errors.not_found"
                )

            total = await DetectorImage.find_many(
                DetectorImage.detector == detector_id
            ).count()

            return CountDetectorImageResponse(status=True, total=total)
        except Exception as e:
            log.warning(str(e))
            return CountDetectorImageResponse(status=False, message=str(e))

    async def listDetectorImage(
        self, request: ListDetectorImageRequest, context
    ) -> ListDetectorImageResponse:
        try:
            found = await DetectorController.load_detector(request.detector)
            
            total = await DetectorImage.find_many(
                DetectorImage.detector == found.id
            ).count()

            images = (
                await DetectorImage.find(DetectorImage.detector == found.id)
                .skip(request.skip)
                .limit(request.limit)
                # .sort(-DetectorImage.updated)
                # .allow_disk_use(True)
                .to_list()
            )
            ret = []
            for image in images:
                ret.append(Conversions.serialize(image))
            return ListDetectorImageResponse(status=True, total=total, images=ret)
        except Exception as e:
            log.warning(str(e))
            return ListDetectorImageResponse(status=False, message=str(e))

    async def listDetector(
        self, request: ListDetectorRequest, context
    ) -> ListDetectorResponse:
        try:
            project_id = PydanticObjectId(request.project)
            search = request.search
            skip = request.skip
            limit = request.limit
            qry = And(Detector.project == project_id)
            if search is not None and search.strip() != "":
                qry = And(
                    Detector.project == project_id,
                    Or(
                        RegEx(Detector.name, search, options="i"),
                        RegEx(Detector.description, search, options="i"),
                    ),
                )
            total = await Detector.find(qry).count()
            detectors = (
                await Detector.find(qry)
                .skip(skip)
                .limit(limit)
                .sort(-Detector.created)
                .to_list()
            )
            ret = []
            for detector in detectors:
                ret.append(Conversions.serialize(detector))
            return ListDetectorResponse(status=True, total=total, detectors=ret)
        except Exception as e:
            log.warning(str(e))
            return ListDetectorResponse(status=False, message=str(e))

    async def countDetector(
        self, request: CountDetectorRequest, context
    ) -> CountDetectorResponse:
        try:
            project_id = PydanticObjectId(request.project)
            total = await Detector.find_many(Detector.project == project_id).count()
            return CountDetectorResponse(status=True, total=total)

        except Exception as e:
            log.warning(str(e))
            return CountDetectorResponse(status=False, message=str(e))

    async def updateDetector(
        self, request: UpdateDetectorRequest, context
    ) -> UpdateDetectorResponse:
        try:
           
            found = await DetectorController.load_detector(request.id)
            others_found = await Detector.find_many(
                Detector.project == found.project,
                Detector.name == request.name,
                Detector.id != found.id,
            ).first_or_none()
            if others_found:
                return UpdateDetectorResponse(
                    status=False, message="detector.errors.already_existing"
                )
            found.name = request.name
            found.description = request.description
            await found.save()
            return UpdateDetectorResponse(
                status=True, detector=Conversions.serialize(found)
            )
        except Exception as e:
            log.warning(str(e))
            return UpdateDetectorResponse(status=False, message=str(e))

    async def loadDetector(
        self, request: LoadDetectorRequest, context
    ) -> LoadDetectorResponse:
        try:
            detector = await DetectorController.load_detector(request.id)
            return LoadDetectorResponse(
                status=True, detector=Conversions.serialize(detector)
            )
        except Exception as e:
            log.warning(str(e))
            return LoadDetectorResponse(status=False, message=str(e))

    async def createDetector(self, request, context) -> CreateDetectorResponse:
        try:
            project_id = PydanticObjectId(request.project)
            name = request.name
            description = request.description
            user_id = PydanticObjectId(request.user)
            others_found = await Detector.find_many(
                Detector.project == project_id, Detector.name == name
            ).first_or_none()
            if others_found:
                return CreateDetectorResponse(
                    status=False, message="detector.errors.already_existing"
                )

            detector = Detector(
                project=project_id, name=name, description=description, users=[user_id]
            )

            await detector.insert()

            return CreateDetectorResponse(
                status=True, detector=Conversions.serialize(detector)
            )
        except Exception as e:
            log.warning(str(e))
            return CreateDetectorResponse(status=False, message=str(e))

    async def trainDetector(
        self, request: TrainDetectorRequest, context
    ) -> TrainDetectorResponse:
        """
        Performs a full training of the detector
        """
        try:
            detector_id = PydanticObjectId(request.detector)
            user = await User.find(User.id==PydanticObjectId(request.user)).first_or_none()
            detector = await Detector.find_many(
                Detector.id == detector_id
            ).first_or_none()
            if detector is None:
                return TrainDetectorResponse(
                    status=False, message="detector.errors.not_found"
                )

            manager = DetectorManager(self.config,detector,self.storage,self.trainer,self.api)       
            await manager.train(request.epochs,user,request.session,request.imageSize)

            return TrainDetectorResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return TrainDetectorResponse(status=False, message=str(e))

    async def addDetectorLabel(
        self, request: AddDetectorLabelRequest, context
    ) -> AddDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            detector = await Detector.find_many(
                Detector.id == detector_id
            ).first_or_none()
            if detector is None:
                return AddDetectorLabelResponse(
                    status=False, message="detector.errors.not_found"
                )

            found = await DetectorLabel.find_many(
                DetectorLabel.detector == detector_id,
                DetectorLabel.name == request.name.strip(),
            ).first_or_none()
            if found is not None:
                return AddDetectorLabelResponse(
                    status=False,
                    message="detector.class.errors.already_existing",
                )

            label = await DetectorLabel(
                detector=detector_id, name=request.name.strip()
            ).insert()
            return AddDetectorLabelResponse(
                status=True, label=Conversions.serialize(label)
            )

        except Exception as e:
            log.warning(str(e))
            return AddDetectorLabelResponse(status=False, message=str(e))

    async def existsDetectorLabel(
        self, request: ExistsDetectorLabelRequest, context
    ) -> ExistsDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            detector = await Detector.find_many(
                Detector.id == detector_id
            ).first_or_none()
            if detector is None:
                return ExistsDetectorLabelResponse(
                    status=False, message="detector.errors.not_found"
                )

            found = await DetectorLabel.find_many(
                DetectorLabel.detector == detector_id,
                DetectorLabel.name == request.name.strip(),
            ).first_or_none()
            if found is None:
                return ExistsDetectorLabelResponse(status=True, label=None)

            return ExistsDetectorLabelResponse(
                status=True, label=Conversions.serialize(found)
            )

        except Exception as e:
            log.warning(str(e))
            return ExistsDetectorLabelResponse(status=False, message=str(e))

    

    async def removeDetector(
        self, request: RemoveDetectorRequest, context
    ) -> RemoveDetectorResponse:
        try:
            detector_id = PydanticObjectId(request.id)
            detector = await Detector.find_many(
                Detector.id == detector_id
            ).first_or_none()
            if detector:
                folder_name = os.path.join(self.config.path, str(detector_id))
                if os.path.exists(folder_name):
                    shutil.rmtree(folder_name)
                await detector.delete()
                return RemoveDetectorResponse(status=True)
            return RemoveDetectorResponse(
                status=False, message="detector.errors.not_found"
            )
        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorResponse(status=False, message=str(e))

    async def addDetectorImageLabel(
        self, request: AddDetectorImageLabelRequest, context
    ) -> AddDetectorImageLabelResponse:
        try:
            image_id = PydanticObjectId(request.image)
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return AddDetectorImageLabelResponse(
                    status=False, message="detector.image.errors.not_found"
                )
            detector_id = found.detector

            class_id = None
            class_name = request.label
            found_class = await DetectorLabel.find_many(
                DetectorLabel.detector == detector_id, DetectorLabel.name == class_name
            ).first_or_none()
            if found_class is None:
                found_class = await DetectorLabel(
                    detector=detector_id, name=class_name
                ).insert()
            class_id = found_class.id

            already_stored = await DetectorImageLabel.find(
                DetectorImageLabel.image == image_id,
                DetectorImageLabel.label == class_id,
                DetectorImageLabel.xstart == request.xstart,
                DetectorImageLabel.xend == request.xend,
                DetectorImageLabel.ystart == request.ystart,
                DetectorImageLabel.yend == request.yend,
            ).first_or_none()
            if not already_stored:
                detector_image_label = await DetectorImageLabel(
                    image=image_id,
                    label=class_id,
                    xstart=request.xstart,
                    xend=request.xend,
                    ystart=request.ystart,
                    yend=request.yend,
                ).insert()
                user_id = PydanticObjectId(request.user)
                return AddDetectorImageLabelResponse(
                    status=True, label=Conversions.serialize(detector_image_label)
                )
            else:
                return AddDetectorImageLabelResponse(
                    status=True, label=Conversions.serialize(already_stored)
                )
        except Exception as e:
            log.warning(str(e))
            return AddDetectorImageLabelResponse(status=False, message=str(e))

    async def listDetectorLabel(
        self, request: ListDetectorLabelRequest, context
    ) -> ListDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            skip = request.skip
            limit = request.limit
            search = request.search
            exclude = request.exclude
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if found is None:
                return ListDetectorLabelResponse(
                    status=False, message="detector.errors.not_found"
                )

            if search is not None and search.strip() != "":
                classes = []
                qry = And(
                    DetectorLabel.detector == detector_id,
                    RegEx(DetectorLabel.name, search, "i"),
                    NotIn(DetectorLabel.name, (exclude)),
                )
            else:
                qry = And(
                    DetectorLabel.detector == detector_id,
                    NotIn(DetectorLabel.name, (exclude)),
                )
            total = await DetectorLabel.find_many(qry).count()
            labels = (
                await DetectorLabel.find_many(qry)
                .skip(skip)
                .limit(limit)
                .sort(-DetectorLabel.updated)
                .to_list()
            )
            user_id = PydanticObjectId(request.user)
            ret = []
            for label in labels:
                ret.append(Conversions.serialize(label))
            return ListDetectorLabelResponse(status=True, total=total, labels=ret)
        except Exception as e:
            log.warning(str(e))
            return ListDetectorLabelResponse(status=False, message=str(e))

    async def removeDetectorLabel(
        self, request: RemoveDetectorLabelRequest, context
    ) -> RemoveDetectorLabelResponse:
        try:
            found = await DetectorLabel.find(
                DetectorLabel.id == PydanticObjectId(request.id)
            ).first_or_none()
            if found:
                total = await DetectorImageLabel.find(
                    DetectorImageLabel.label == PydanticObjectId(request.id)
                ).count()
                if total == 0:
                    await found.delete()
                    return RemoveDetectorLabelResponse(status=True)
                else:
                    return RemoveDetectorLabelResponse(
                        status=False, message="detector.class.errors.has_images"
                    )
            else:
                return RemoveDetectorLabelResponse(
                    status=False, message="detector.class.errors.not_found"
                )
        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorLabelResponse(status=False, message=str(e))

    async def canRemoveDetectorLabel(
        self, request: CanRemoveDetectorLabelRequest, context
    ) -> CanRemoveDetectorLabelResponse:
        try:
            found = await DetectorLabel.find(
                DetectorLabel.id == PydanticObjectId(request.id)
            ).first_or_none()
            if found:
                total = await DetectorImageLabel.find(
                    DetectorImageLabel.label == PydanticObjectId(request.id)
                ).count()
                if total == 0:
                    return CanRemoveDetectorLabelResponse(status=True, result=True)
                else:
                    return CanRemoveDetectorLabelResponse(status=True, result=False)
            else:
                return CanRemoveDetectorLabelResponse(
                    status=False, message="detector.class.errors.not_found"
                )
        except Exception as e:
            log.warning(str(e))
            return CanRemoveDetectorLabelResponse(status=False, message=str(e))

    async def countDetectorLabel(
        self, request: CountDetectorLabelRequest, context
    ) -> CountDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if found is None:
                return ListDetectorLabelResponse(
                    status=False, message="detector.errors.not_found"
                )

            qry = And(DetectorLabel.detector == detector_id)
            total = await DetectorLabel.find_many(qry).count()

            user_id = PydanticObjectId(request.user)

            return CountDetectorLabelResponse(status=True, total=total)
        except Exception as e:
            log.warning(str(e))
            return CountDetectorLabelResponse(status=False, message=str(e))

    async def listDetectorImageLabel(
        self, request: ListDetectorImageLabelRequest, context
    ) -> ListDetectorImageLabelResponse:
        try:
            image_id = PydanticObjectId(request.image)
            search = request.search
            skip = request.skip
            limit = request.limit
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return ListDetectorImageLabelResponse(
                    status=False, message="detector.image.errors.not_found"
                )

            if search is not None and search.strip() != "":
                classes = []
                qry = And(
                    DetectorLabel.detector == found.detector,
                    RegEx(DetectorLabel.name, search, "i"),
                )
                found_classes = await DetectorLabel.find_many(qry).to_list()
                for found_class in found_classes:
                    classes.append(found_class.id)
                qry = And(
                    DetectorImageLabel.image == image_id,
                    In(DetectorImageLabel.label, classes),
                )
            else:
                qry = And(DetectorImageLabel.image == image_id)
            total = await DetectorImageLabel.find_many(qry).count()
            labels = (
                await DetectorImageLabel.find_many(qry)
                .skip(skip)
                .limit(limit)
                .sort(-DetectorImageLabel.updated)
                .to_list()
            )

            ret = []
            for label in labels:
                ret.append(Conversions.serialize(label))
            return ListDetectorImageLabelResponse(status=True, total=total, labels=ret)

        except Exception as e:
            log.warning(str(e))
            return ListDetectorImageLabelResponse(status=False, message=str(e))

    async def uploadDetectorImage(
        self, request: UploadDetectorImageRequest, context
    ) -> UploadDetectorImageResponse:
        try:
            log.debug("Loading detector")
            file_id = PydanticObjectId(request.file)
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not found:
                return UploadDetectorImageResponse(
                    status=False, message="detector.errors.not_found"
                )

            log.debug("Loading image")
            data, content_type, size = await self.storage.loadById(file_id)
            img = Image.open(BytesIO(data))
            width, height = img.size

            log.debug("Creating new detector image document")
            ret = []
            for gmode in request.modes:
                mode = DetectorImageMode.test
                if gmode == GrpcDetectorImageMode.TRAIN:
                    mode = DetectorImageMode.train
                elif gmode == GrpcDetectorImageMode.TEST:
                    mode = DetectorImageMode.test
                elif gmode == GrpcDetectorImageMode.VAL:
                    mode = DetectorImageMode.val

                detector_image = await DetectorImage(
                    detector=detector_id,
                    mode=mode,
                    storage=file_id,
                    width=width,
                    height=height,
                ).insert()
                ret.append(Conversions.serialize(detector_image))
            return UploadDetectorImageResponse(status=True, images=ret)
        except Exception as e:
            log.warning(str(e))
            return UploadDetectorImageResponse(status=False, message=str(e))

    async def countDetectorImageLabel(
        self, request: CountDetectorImageLabelRequest, context
    ) -> CountDetectorImageLabelResponse:
        try:
            total = await ObjectController.count_image_labels(request.image)
            return CountDetectorImageLabelResponse(status=True, total=total)

        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorImageLabelResponse(status=False, message=str(e))

    async def removeDetectorImageLabel(
        self, request: RemoveDetectorImageLabelRequest, context
    ) -> RemoveDetectorImageLabelResponse:
        try:
            await ObjectController.remove_image_label(request.label)
            return RemoveDetectorImageLabelResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorImageLabelResponse(status=False, message=str(e))

    async def trainResult(
        self, request: TrainResultRequest, context
    ) -> TrainResultResponse:
        file_path = os.path.join(os.getcwd(), request.filename)
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            content_type = "application/octet-stream"  # Or detect via mimetypes
            return TrainResultResponse(data=data, content_type=content_type, found=True)
        except FileNotFoundError:
            return TrainResultResponse(found=False)

    async def detectorImage(self, request:DetectorImageRequest, context) -> DetectorImageResponse:
        try:
            data,content_type,size = await self.storage.loadById(PydanticObjectId(request.id))
            return DetectorImageResponse(found=True,data=data,content_type=content_type)
        except Exception:
            log.warning(str(e))
            return DetectorImageResponse(found=False)