# PYTHON IMPORTS
import asyncio
import base64
from io import BytesIO
import json
import logging
import threading
import pytesseract
from pytesseract import Output
from ultralytics import YOLO
import yaml
import os
import shutil

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And,Or,In,RegEx

from PIL import Image
#from PIL import ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES = True

# LOCAL IMPORTS
from common.clients.api import ApiClient
from common.clients.recorder import RecorderClient
from common.models import MODELS
from common.models.auth import User
from common.models.detector import Detector, DetectorLabel, DetectorImage, DetectorImageLabel, DetectorImageMode, DetectorTrainingSession
from common.rpc.detector_pb2 import AddDetectorLabelRequest, AddDetectorLabelResponse, AddDetectorImageLabelRequest, AddDetectorImageLabelResponse, CountDetectorLabelRequest, CountDetectorLabelResponse, CountDetectorImageLabelRequest, CountDetectorImageLabelResponse, CountDetectorImageRequest, CountDetectorImageResponse, CountDetectorRequest, CountDetectorResponse, CreateDetectorResponse, DetectObject, DetectObjectsRequest, DetectObjectsResponse, DetectText, DetectTextsRequest, DetectTextsResponse, DetectorStepSuggestion, ExistsDetectorLabelRequest, ExistsDetectorLabelResponse, ListDetectorLabelRequest, ListDetectorLabelResponse, ListDetectorImageLabelRequest, ListDetectorImageLabelResponse, ListDetectorImageRequest, ListDetectorImageResponse, ListDetectorRequest, ListDetectorResponse, LoadDetectorRequest, LoadDetectorResponse, RemoveDetectorImageLabelRequest, RemoveDetectorImageLabelResponse, RemoveDetectorImageRequest, RemoveDetectorImageResponse, RemoveDetectorRequest, RemoveDetectorResponse, SuggestStepRequest, SuggestStepResponse, TrainDetectorRequest, TrainDetectorResponse, UpdateDetectorRequest, UpdateDetectorResponse, UploadDetectorImageRequest, UploadDetectorImageResponse, DetectorImageMode as GrpcDetectorImageMode
from common.service import ClientConfig, Service
from common.rpc.detector_pb2_grpc import DetectorServicer
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.imaging import ImageGrid
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)

class DetectorServiceConfig(ServiceConfig):
    database: MongodbConfig
    path: str
    original: str
    name: str
    data: str
    runs: str
    classes: str
    video:str
    recorder:ClientConfig
    api:ClientConfig

class DetectorService(Service, DetectorServicer):

    def __init__(self, config: DetectorServiceConfig):
        DetectorServicer.__init__(self)
        Service.__init__(self)
        self.config:DetectorServiceConfig = config
        self.api = ApiClient(self.config.api)
        self.recorder = RecorderClient(self.config.recorder)
        
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
         self.CACHE_YOLOS = {}
         await self.recorder.startup()
         
    async def suggestStep(self, request:SuggestStepRequest, context) -> SuggestStepResponse:
        try:
            user = await User.find_many(User.id == PydanticObjectId(request.user)).first_or_none()
            event = await self.recorder.loadEvent(user,PydanticObjectId(request.event))
            
            b64image = request.data
            log.debug("Loading image")
            if "," in b64image:
                bsource = b64image.split(",")[1]
            else:
                bsource = b64image
            img = Image.open(BytesIO(self.decode_base64(bsource)))
            width, height = img.size
            
            # If has no position, not suggestions are possible so far
            if not event.type.startswith('mouse'):
                return SuggestStepResponse(status=True,suggestions=[])
            
            x, y = event.position
            print('{0},{1}'.format(x,y))
            #x = x / width
            #y = y / height
            print('{0},{1}'.format(x,y))
            
            # Matching texts
            req = DetectTextsRequest(user=request.user,data=request.data,confidence=request.confidence)
            res = await self.detectTexts(req,context)
            
            suggestions = []
            
            if res.status == True:
                matched = None
                for text in res.texts:
                    nx = text.x*width
                    ny = text.y*height
                    nw = text.w*width
                    nh = text.h*height
                    
                    if x > nx and x < (nx+nw) and y > ny and y < (ny+nh):
                        matched = text
                        log.debug('detected Text: {0},{1} ({2},{3})'.format(nx,ny,nw,nh))
                        break
                        
                # Now checking if it is unique
                if matched:
                    others = []
                    for text in res.texts:
                        if text!=matched and text.value == matched.value:
                            others.append(text)
                    
                    # There are no other texts with same value, suggestion is unique for text
                    if len(others)==0:
                        suggestions.append(DetectorStepSuggestion(event=request.event,byText=matched.value,confidence=matched.confidence,x=nx,y=ny,w=nw,h=nh))
                    
                    else:
                        suggestions.append(DetectorStepSuggestion(event=request.event,byText=matched.value,byOrder=[matched.line,matched.block],x=nx,y=ny,w=nw,h=nh,confidence=matched.confidence))
                        
            # Mathing objects                            
            req = DetectObjectsRequest(user=request.user,data=request.data,detector=request.detector,confidence=request.confidence)
            res = await self.detectObjects(req,context)
                        
            #DetectObject(x=x,y=y,w=w,h=h,confidence=confidence,code=code,name=name,row=row,col=col
            
            if res.status == True:
                matched = None
                for obj in res.objects:
                    nx = obj.x*width
                    ny = obj.y*height
                    nw = obj.w*width
                    nh = obj.h*height
                    if x > nx and x < (nx+nw) and y > ny and y < (ny+nh):
                        matched = obj
                        break
                
                # Now checking if it is unique
                if matched:
                    others = []
                    for obj in res.objects:
                        if obj != matched and matched.name == obj.name:
                            others.append(obj)
                            
                    # There are no other objects with same value
                    if len(others)==0:
                        suggestions.append(DetectorStepSuggestion(event=request.event,byLabel=matched.name,confidence=matched.confidence,x=nx,y=ny,w=nw,h=nh))
                    
                    else:
                        suggestions.append(DetectorStepSuggestion(event=request.event,byLabel=matched.name,byOrder=[matched.row,matched.col],x=nx,y=ny,w=nw,h=nh,confidence=matched.confidence))
                
            return SuggestStepResponse(status=True,suggestions=suggestions)
            
        
        except Exception as e:
            log.warning(str(e))
            return SuggestStepResponse(status=False,message=str(e))
         
    
    async def detectTexts(self, request: DetectTextsRequest, context) -> DetectTextsResponse:
        try:
            b64image = request.data
            log.debug("Loading image")
            if "," in b64image:
                bsource = b64image.split(",")[1]
            else:
                bsource = b64image
            img = Image.open(BytesIO(self.decode_base64(bsource)))
            width, height = img.size
            
            log.debug("Detecting text elements")
            confidence_level = int(round(request.confidence*100))
            # Get verbose data including boxes, confidences, line and page numbers
            text_results = pytesseract.image_to_data(img, output_type=Output.DICT)
            n_boxes = len(text_results["text"])
            texts = []
            for i in range(n_boxes):
                confidence = int(text_results["conf"][i])
                text = text_results["text"][i]
                if confidence >=  confidence_level and text.strip()!='':
                    x = text_results["left"][i] / width
                    y = text_results["top"][i] / height
                    w = text_results["width"][i] / width
                    h = text_results["height"][i] / height
                    page = text_results["page_num"][i]
                    block = text_results["block_num"][i]
                    par = text_results["par_num"][i]
                    line = text_results["line_num"][i]
                    word = text_results["word_num"][i]
                    texts.append(DetectText(x=x,y=y,w=w,h=h,page=page,block=block,par=par,line=line,word=word,value=text,confidence=confidence))
            return DetectTextsResponse(status=True,texts=texts)
                    
            
        except Exception as e:
            log.warning(str(e))
            return DetectTextsResponse(status=False,message=str(e))
    
    async def detectObjects(self, request: DetectObjectsRequest, context)-> DetectObjectsResponse:
        try:
            log.debug("Loading detector")
            b64image = request.data
            detector_id = PydanticObjectId(request.detector)
            detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not detector:
                return DetectObjectsResponse(status=False,message="workspace.detector.errors.not_fopund")
            
            log.debug("Loading YOLO Model")
            if detector.best is None:
                path = os.path.join(self.config.path, str(detector_id), self.config.name)
                if not os.path.exists(path):
                    return DetectObjectsResponse(status=False,message="workspace.detector.errors.not_fopund")
            else:
                path = detector.best
                
            
            if path not in self.CACHE_YOLOS:
                model = YOLO(path)
                self.CACHE_YOLOS[path]= model
            else:
                model = self.CACHE_YOLOS[path]
            
            log.debug("Loading image")
            if "," in b64image:
                bsource = b64image.split(",")[1]
            else:
                bsource = b64image
            img = Image.open(BytesIO(self.decode_base64(bsource)))
            width, height = img.size
            grid = ImageGrid(width,height)
            
            log.debug("Start detection")
            visual_results = model(img, conf=request.confidence or 0.7)  # predict on an image
            
            boxes = []
            for result in visual_results:
                detections = json.loads(result.to_json())
                for detection in detections:
                    x = detection["box"]["x1"]
                    y = detection["box"]["y1"]
                    w = detection["box"]["x2"] - detection["box"]["x1"]
                    h = detection["box"]["y2"] - detection["box"]["y1"]
                    boxes.append((x, y, w, h))

            best_rows, best_cols = grid.optimal_grid_size(boxes)
            
            
            objects = []
            for result in visual_results:
                detections = json.loads(result.to_json())
                for detection in detections:
                    confidence = detection['confidence']
                    code = detection['class']
                    name = detection['name']
                    x = detection["box"]["x1"]
                    y = detection["box"]["y1"]
                    w = detection["box"]["x2"] - detection["box"]["x1"]
                    h = detection["box"]["y2"] - detection["box"]["y1"]
                    row, col = grid.classify_box(best_rows, best_cols, x, y, w, h)
                    objects.append(DetectObject(x=x,y=y,w=w,h=h,confidence=confidence,code=code,name=name,row=row,col=col))
            return DetectObjectsResponse(status=True,objects=objects)
            
        except Exception as e:
            log.warning(str(e))
            return DetectObjectsResponse(status=False, message = str(e))
         
    async def removeDetectorImage(self, request: RemoveDetectorImageRequest, context) -> RemoveDetectorImageResponse:
        try:
            image_id = PydanticObjectId(request.id)
            user_id = PydanticObjectId(request.user)
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return RemoveDetectorImageResponse(status=False,message="workspace.detector.image.errors.not_found")
            detector_id = found.detector
            mode = found.mdoe
            await found.delete()

            image_path = os.path.join(
                os.getcwd(), self.config.path, str(detector_id), "images"
            )
            image_train_path = os.path.join(image_path, "train")
            image_val_path = os.path.join(image_path, "val")
            image_test_path = os.path.join(image_path, "test")

            suffix_name = str(image_id.id) + ".png"
            if mode == DetectorImageMode.train:
                image_filename = os.path.join(image_train_path, suffix_name)
            elif mode == DetectorImageMode.test:
                image_filename = os.path.join(image_test_path, suffix_name)
            else:
                image_filename = os.path.join(image_val_path, suffix_name)

            log.debug("Removing image file")
            if os.path.exists(image_filename):
                os.remove(image_filename)

            log.debug("Removing class files")
            classes_filename = os.path.join(image_path, str(image_id.id) + ".txt")
            if os.path.exists(classes_filename):
                os.remove(classes_filename)

            await self.update_folder(user_id, detector_id)

            return RemoveDetectorImageResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorImageResponse(status=False,message=str(e))
         
    
    async def countDetectorImage(self, request: CountDetectorImageRequest, context) -> CountDetectorImageResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not found:
                return ListDetectorImageResponse(status=False,message="workspace.detector.errors.not_found")
                

            total = await DetectorImage.find_many(
                DetectorImage.detector == detector_id
            ).count()
            
            return CountDetectorImageResponse(status=True,total=total)
        except Exception as e:
            log.warning(str(e))
            return CountDetectorImageResponse(status=False,message=str(e))
        
         
         
    async def listDetectorImage(self, request: ListDetectorImageRequest, context) -> ListDetectorImageResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not found:
                return ListDetectorImageResponse(status=False,message="workspace.detector.errors.not_found")
                

            total = await DetectorImage.find_many(
                DetectorImage.detector == detector_id
            ).count()
            images = (
                await DetectorImage.find_many(DetectorImage.detector == detector_id)
                .skip(request.skip)
                .limit(request.limit)
                .sort(-DetectorImage.updated)
                .to_list()
            )
            ret = []
            for image in images:
                ret.append(Conversions.serialize(image))
            return ListDetectorImageResponse(status=True,total=total,images=ret)
        except Exception as e:
            log.warning(str(e))
            return ListDetectorImageResponse(status=False,message=str(e))
        
         
    async def listDetector(self, request: ListDetectorRequest, context) -> ListDetectorResponse:
        try:
            project_id = PydanticObjectId(request.project)
            search = request.search
            skip = request.skip
            limit = request.limit
            qry = And(Detector.project == project_id)
            if search is not None and search.strip()!='':
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
            return ListDetectorResponse(status=True,total=total,detectors=ret)
        except Exception as e:
            log.warning(str(e))
            return ListDetectorResponse(status=False,message=str(e))
        
    async def countDetector(self, request: CountDetectorRequest, context) -> CountDetectorResponse:
        try:
            project_id = PydanticObjectId(request.project)
            total = await Detector.find_many(Detector.project == project_id).count()
            return CountDetectorResponse(status=True,total=total)

        except Exception as e:
            log.warning(str(e))
            return CountDetectorResponse(status=False,message=str(e))
        
    async def updateDetector(self, request: UpdateDetectorRequest, context) -> UpdateDetectorResponse:
        try:
            detector_id = PydanticObjectId(request.id)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not found:
                return UpdateDetectorResponse(status=False,message="workspace.detector.errors.not_found")
            others_found = await Detector.find_many(
                Detector.project == found.project,
                Detector.name == request.name,
                Detector.id != found.id,
            ).first_or_none()
            if others_found:
                return UpdateDetectorResponse(status=False,message="workspace.detector.errors.already_existing")
            found.name = request.name
            found.description = request.description
            await found.save()
            return UpdateDetectorResponse(status=True,detector=Conversions.serialize(found))
        except Exception as e:
            log.warning(str(e))
            return UpdateDetectorResponse(status=False,message=str(e))
        
    async def loadDetector(self, request:LoadDetectorRequest, context) -> LoadDetectorResponse:
        try:
            detector_id = PydanticObjectId(request.id)
            detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if detector is None:
                return LoadDetectorResponse(status=False,message="workspace.detector.errors.not_found")
            return LoadDetectorResponse(status=True,detector=Conversions.serialize(detector))
        except Exception as e:
            log.warning(str(e))
            return LoadDetectorResponse(status=False,message=str(e))
        
    async def createDetector(self, request, context) -> CreateDetectorResponse:
        try:
            project_id = PydanticObjectId(request.project)
            name = request.name
            origin = request.origin
            description = request.description
            user_id = PydanticObjectId(request.user)
            others_found = await Detector.find_many(
            Detector.project == project_id, Detector.name == name).first_or_none()
            if others_found:
                return CreateDetectorResponse(status=False,message="workspace.detector.errors.already_existing")

            detector = Detector(
                project=project_id, name=name, description=description, users=[user_id]
            )

            await detector.insert()

            log.debug("Create detector paths")
            base_name = self.config.name
            target_path = os.path.join(self.config.path, str(detector.id), base_name)
            folder_name = os.path.join(self.config.path, str(detector.id))
            
            
            os.mkdir(folder_name)
            
            labels_path = os.path.join(folder_name,"labels")
            os.mkir(labels_path)
            
            labels_train_path = os.path.join(labels_path,"train")
            os.mkdir(labels_train_path)
            
            labels_val_path = os.path.join(labels_path,"val")
            os.mkdir(labels_val_path)
            
            labels_test_path = os.path.join(labels_path,"test")
            os.mkdir(labels_test_path)
            
            labels_train_path = os.path.join(labels_path,"train")
            os.mkdir(labels_train_path)
            
            images_path = os.path.join(folder_name, "images")
            os.mkdir(images_path)

            train_path = os.path.join(images_path, "train")
            os.mkdir(train_path)

            test_path = os.path.join(images_path, "test")
            os.mkdir(test_path)

            val_path = os.path.join(images_path, "val")
            os.mkdir(val_path)

            if origin is None:
                base_path = self.config.path
                original_path = os.path.join(base_path, self.config.original)
                original_classes_filename = os.path.join(base_path, self.config.classes)
            else:
                original_detector = await Detector.find_many(
                    Detector.id == origin
                ).first_or_none()
                if original_detector is None:
                    return CreateDetectorResponse(sttatus=False,message="worspace.detectors.errors.original_not_found")

                base_path = self.config.path
                original_path = os.path.join(
                    base_path, str(original_detector.id), base_name
                )
                original_classes_filename = os.path.join(
                    base_path, str(original_detector.id), self.config.classes
                )

            log.debug("Copy detector model")
            shutil.copyfile(original_path, target_path)

            log.debug("Loading original classes")
            with open(original_classes_filename, "r") as classes_file:
                classes = yaml.load(classes_file)

            log.debug("Create model configuration")
            data = dict(
                path=os.path.join(os.getcwd(), self.config.path, str(detector.id)) + "/",
                train="images/train",
                val="images/val",
                test="images/test",
                nc=classes["nc"],
                names=classes["names"],
            )
            log.debug("Saving model configuration")
            config_filename = os.path.join(
                self.config.path, str(detector.id), self.config.data
            )
            with open(config_filename, "w") as outfile:
                yaml.dump(data, outfile, default_flow_style=False)

            return CreateDetectorResponse(status=True,detector=Conversions.serialize(detector))
        except Exception as e:
            log.warning(str(e))
            return CreateDetectorResponse(status=False,message=str(e))
        
    async def trainDetector(self, request: TrainDetectorRequest, context) -> TrainDetectorResponse:
        
        try:
            epochs = request.epochs
            user_id = PydanticObjectId(request.user)
            detector_id = PydanticObjectId(request.detector)
            session = request.session
            image_size = request.imageSize
            
            detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if detector is None:
                return TrainDetectorResponse(status=False,message="workspace.detector.errors.not_found")
            
            training_session = DetectorTrainingSession(
                detector=detector_id,
                user=user_id,
                epoch_total=epochs,
                epoch_progress=0,
                box_loss=0.0,
                class_loss=0.0,
                object_loss=0.0,
            )

            def on_train_epoch_end(trainer):
                """
                Custom callback executed at the end of each training epoch.

                Args:
                    trainer: The YOLO Trainer object.
                """
                epoch = trainer.epoch  # Current epoch number
                results = trainer.metrics  # Training metrics (loss, mAP, etc.)

                
                training_session.epoch_progress = epoch
                # Example: Log the loss
                if results:
                    pass
                    #print(results)
                    # print(f"Loss: {results.box.loss:.4f}, "
                    #    f"Label Loss: {results.cls.loss:.4f}, "
                    #    f"Object Loss: {results.dfl.loss:.4f}"
                    
                    #training_session.box_loss = results['box']['loss']
                    #training_session.class_loss = results['cls']['loss']
                    #training_session.object_loss = results['dfl']['loss']
                    
                asyncio.create_task(self.api.updateSession(session,training_session))
                
                

            # Load a COCO-pretrained YOLO11n model
            log.debug("Loading YOLO Model")
            if detector.best is None:
                path = os.path.join(self.config.path, str(detector_id), self.config.name)
                if not os.path.exists(path):
                    return TrainDetectorResponse(status=False,message="workspace.detector.errors.not_found")
            else:
                path = detector.best
                
            
            async def training(path):
                model = YOLO(path)

                # Train the model on the COCO8 example dataset for 100 epochs
                data_path = os.path.join(
                    self.config.path, str(detector_id), self.config.data
                )
                runs_path = os.path.join(
                    self.config.path, str(detector_id), self.config.runs
                )
                model.add_callback("on_train_epoch_end", on_train_epoch_end)
                results = model.train(
                    data=data_path, epochs=epochs, imgsz=image_size, project=runs_path
                )
                
                training_session.epoch_progress = epochs
                await self.api.updateSession(session,training_session)
                log.debug("Results are saved into: {0}".format(results.save_dir))
                detector.best = os.path.join(results.save_dir,'weights/best.pt')
                detector.last = os.path.join(results.save_dir,'weights/last.pt')
                
                await detector.save()
                
            #train_thread = threading.Thread(target=training, args=(path,), daemon=True)
            #train_thread.start()
            task1 = asyncio.create_task(training(path))  # Run task_one concurrently
            
            return TrainDetectorResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return TrainDetectorResponse(status=False,message=str(e))
        
    async def addDetectorLabel(self, request: AddDetectorLabelRequest, context) -> AddDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if detector is None:
                return AddDetectorLabelResponse(status=False,message="workspace.detector.errors.not_found")
            
            found = await DetectorLabel.find_many(DetectorLabel.detector == detector_id,DetectorLabel.name == request.name.strip()).first_or_none()
            if found is not None:
                return AddDetectorLabelResponse(status=False,message="workspace.detector.class.errors.already_existing")
        
            label = await DetectorLabel(detector=detector_id,name=request.name.strip()).insert()
            return AddDetectorLabelResponse(status=True,label=Conversions.serialize(label))

        except Exception as e:
            log.warning(str(e))
            return AddDetectorLabelResponse(status=False,message=str(e))
        
    async def existsDetectorLabel(self, request: ExistsDetectorLabelRequest, context) -> ExistsDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if detector is None:
                return ExistsDetectorLabelResponse(status=False,message="workspace.detector.errors.not_found")
            
            found = await DetectorLabel.find_many(DetectorLabel.detector == detector_id,DetectorLabel.name == request.name.strip()).first_or_none()
            if found is None:
                return ExistsDetectorLabelResponse(status=True,label=None)
                
            return ExistsDetectorLabelResponse(status=True,label=Conversions.serialize(found))

        except Exception as e:
            log.warning(str(e))
            return ExistsDetectorLabelResponse(status=False,message=str(e))
        
    async def update_folder(
        self, user_id: PydanticObjectId, detector_id: PydanticObjectId
    ):

        labels = await DetectorLabel.find_many(
            DetectorLabel.detector == detector_id
        ).to_list()
        images = await DetectorImage.find_many(
            DetectorImage.detector == detector_id
        ).to_list()

        yaml_filename = os.path.join(
            self.config.path, str(detector_id), self.config.data
        )
        with open(yaml_filename, "r") as infile:
            yaml_file = yaml.load(infile)

        class_by_number = {}
        class_by_name = {}
        for label in labels:
            if label.name not in list(yaml_file["names"].values()):
                n = str(len(list(yaml_file["names"].keys())))
                yaml_file["names"][int(n)] = label.name
        for key in yaml_file["names"].keys():
            class_by_number[key] = yaml_file["names"][key]
            class_by_name[yaml_file["names"][key]] = key

        yaml_file["nc"] = len(list(yaml_file["names"].keys()))

        with open(yaml_filename, "w") as outfile:
            yaml.dump(yaml_file, outfile)

        for image in images:
            image_labels = await DetectorImageLabel.find_many(
                DetectorImageLabel.image == image.id
            ).to_list()
            
            sub_path = ''
            if image.mode == DetectorImageMode.train:
                sub_path = 'train'
            elif image.mode == DetectorImageMode.val:
                sub_path = 'val'
            else:
                sub_path = 'test'
            
            image_box_file = os.path.join(
                os.getcwd(),
                self.config.path,
                str(detector_id),
                "labels",
                sub_path,
                str(image.id) + ".txt",
            )
            lines = []
            for image_label in image_labels:
                dlabel = await DetectorLabel.find_many(
                    DetectorLabel.id == image_label.label
                ).first_or_none()
                label_name = dlabel.name
                w = (label.xend - label.xstart) / image.width
                h = (label.yend - label.ystart)/image.height
                x = label.xend/image.width - (w/2)
                y = label.yend/image.height - (h/2)
                

                # 16 0.048093 0.081250 0.051410 0.064583
                line = "{0} {1:0.6f} {2:0.6f} {3:0.6f} {4:0.6f} ".format(
                    class_by_name[label_name], x, y, w, h
                )
                log.debug(line)
                lines.append(line)
            with open(image_box_file, "w") as f:
                f.writelines(line + "\n" for line in lines)
                
        # Failover for no val images
        image_path = os.path.join(
            os.getcwd(), self.config.path, str(detector_id), "images"
        )
        image_train_path = os.path.join(image_path, "train")
        image_val_path = os.path.join(image_path, "val")
        image_test_path = os.path.join(image_path, "test")
        val_images_number = len([name for name in os.listdir(image_val_path) if os.path.isfile(os.path.join(image_val_path, name))])
        if val_images_number == 0:
            for fname in os.listdir(image_train_path):
    
                # copying the files to the 
                # destination directory
                shutil.copy2(os.path.join(image_train_path,fname), image_val_path)
                
    

    def decode_base64(self, b64image: str):
        # Add padding if needed
        padding = len(b64image) % 4
        if padding != 0:
            b64image += "=" * (4 - padding)

        try:
            # Decode the Base64 string to bytes
            decoded_bytes = base64.decodebytes(bytes(b64image, "utf-8"))
            return decoded_bytes
        except Exception as e:
            log.warning("Error decoding base64:", e)
            return None
        
    async def removeDetector(self, request: RemoveDetectorRequest, context) -> RemoveDetectorResponse:
        try:
            detector_id = PydanticObjectId(request.id)
            detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if detector:
                folder_name = os.path.join(self.config.path, str(detector_id))
                if os.path.exists(folder_name):
                    shutil.rmtree(folder_name)
                await detector.delete()
                return RemoveDetectorResponse(status=True)
            return RemoveDetectorResponse(status=False,message="workspace.detector.errors.not_found")
        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorResponse(status=False,message=str(e))
        
    async def addDetectorImageLabel(self, request:AddDetectorImageLabelRequest, context) -> AddDetectorImageLabelResponse:
        try:
            image_id = PydanticObjectId(request.image)
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return AddDetectorImageLabelResponse(status=False,message="workspace.detector.image.errors.not_found")
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

            detector_image_label = await DetectorImageLabel(
                image=image_id,
                label=class_id,
                xstart=request.xstart,
                xend=request.xend,
                ystart=request.ystart,
                yend=request.yend,
            ).insert()
            user_id = PydanticObjectId(request.user)
            await self.update_folder(user_id, detector_id)
            return AddDetectorImageLabelResponse(status=True,label=Conversions.serialize(detector_image_label))
        except Exception as e:
            log.warning(str(e))
            return AddDetectorImageLabelResponse(status=False,message=str(e))

    async def listDetectorLabel(self, request:ListDetectorLabelRequest, context) -> ListDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            skip = request.skip
            limit = request.limit
            search = request.search
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if found is None:
                return ListDetectorLabelResponse(status=False,message="workspace.detector.errors.not_found")

            if search is not None and search.strip() != "":
                classes = []
                qry = And(
                    DetectorLabel.detector == detector_id,
                    RegEx(DetectorLabel.name, search, "i"),
                )
            else:
                qry = And(DetectorLabel.detector == detector_id)
            total = await DetectorLabel.find_many(qry).count()
            labels = (
                await DetectorLabel.find_many(qry)
                .skip(skip)
                .limit(limit)
                .sort(-DetectorLabel.updated)
                .to_list()
            )
            user_id = PydanticObjectId(request.user)
            #await self.update_folder(user_id, detector_id)
            ret = []
            for label in labels:
                ret.append(Conversions.serialize(label))
            return ListDetectorLabelResponse(status=True,total=total,labels=ret)
        except Exception as e:
            log.warning(str(e))
            return ListDetectorLabelResponse(status=False,message=str(e))
        
    
    async def countDetectorLabel(self, request:CountDetectorLabelRequest, context) -> CountDetectorLabelResponse:
        try:
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if found is None:
                return ListDetectorLabelResponse(status=False,message="workspace.detector.errors.not_found")

            qry = And(DetectorLabel.detector == detector_id)
            total = await DetectorLabel.find_many(qry).count()
            
            user_id = PydanticObjectId(request.user)
            await self.update_folder(user_id, detector_id)
            
            return CountDetectorLabelResponse(status=True,total=total)
        except Exception as e:
            log.warning(str(e))
            return CountDetectorLabelResponse(status=False,message=str(e))


    async def listDetectorImageLabel(self, request: ListDetectorImageLabelRequest, context) -> ListDetectorImageLabelResponse:
        try:
            image_id = PydanticObjectId(request.image)
            user_id = PydanticObjectId(request.user)
            search = request.search
            skip = request.skip
            limit = request.limit
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return ListDetectorImageLabelResponse(status=False,message="workspace.detector.image.errors.not_found")

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
            return ListDetectorImageLabelResponse(status=True,total=total,labels=labels)

        except Exception as e:
            log.warning(str(e))
            return ListDetectorImageLabelResponse(status=False,message=str(e))
        

    async def uploadDetectorImage(self, request:UploadDetectorImageRequest, context) -> UploadDetectorImageResponse:
        try:
            log.debug("Loading detector")
            b64image = request.data
            detector_id = PydanticObjectId(request.detector)
            found = await Detector.find_many(Detector.id == detector_id).first_or_none()
            if not found:
                return UploadDetectorImageResponse(status=False,message="workspace.detector.errors.not_found")
            
            log.debug("Loading image")
            if "," in b64image:
                bsource = b64image.split(",")[1]
            else:
                bsource = b64image
            img = Image.open(BytesIO(self.decode_base64(bsource)))
            width, height = img.size

            log.debug("Creating new detector image document")
            ret = []
            for gmode in request.modes:
                mode = DetectorImageMode.test;
                if gmode == GrpcDetectorImageMode.TRAIN:
                    mode = DetectorImageMode.train
                elif gmode == GrpcDetectorImageMode.TEST:
                    mode = DetectorImageMode.test
                elif gmode == GrpcDetectorImageMode.VAL:
                    mode = DetectorImageMode.val
                
                detector_image = await DetectorImage(
                    detector=detector_id, mode=mode, data=b64image, width=width, height=height
                ).insert()


                image_path = os.path.join(
                    os.getcwd(), self.config.path, str(detector_id), "images"
                )
                image_train_path = os.path.join(image_path, "train")
                image_val_path = os.path.join(image_path, "val")
                image_test_path = os.path.join(image_path, "test")

                suffix_name = str(detector_image.id) + ".png"
                if mode == DetectorImageMode.train:
                    image_filename = os.path.join(image_train_path, suffix_name)
                elif mode == DetectorImageMode.test:
                    image_filename = os.path.join(image_test_path, suffix_name)
                else:
                    image_filename = os.path.join(image_val_path, suffix_name)

                log.debug("Saving image")

                img.save(image_filename, quality=100, subsampling=0)
                
                ret.append(Conversions.serialize(detector_image))
            user_id = PydanticObjectId(request.user)
            await self.update_folder(user_id, detector_id)
            return UploadDetectorImageResponse(status=True,images=ret)
        except Exception as e:
            log.warning(str(e))
            return UploadDetectorImageResponse(status=False,message=str(e))
        
    async def countDetectorImageLabel(self, request:CountDetectorImageLabelRequest, context) -> CountDetectorImageLabelResponse:
        try:
            image_id = PydanticObjectId(request.image)
            found = await DetectorImage.find_many(
                DetectorImage.id == image_id
            ).first_or_none()
            if found is None:
                return CountDetectorImageLabelResponse(status=False,message="workspace.detector.image.errors.not_found")
            total = await DetectorImageLabel.find_many(
                DetectorImageLabel.image == image_id
            ).count()
            return CountDetectorImageLabelResponse(status=True,total=total)

        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorImageLabelResponse(status=False,message=str(e))
        
    async def removeDetectorImageLabel(self, request:RemoveDetectorImageLabelRequest, context)-> RemoveDetectorImageLabelResponse:
        try:
            detector_image_label_id = PydanticObjectId(request.label)
            found = await DetectorImageLabel.find_many(
            DetectorImageLabel.id == detector_image_label_id
            ).first_or_none()
            if found is None:
                return RemoveDetectorImageLabelResponse(status=False,message="workspace.detector.image.errors.label_not_found")
            await found.delete()

            return RemoveDetectorImageLabelResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return RemoveDetectorImageLabelResponse(status=False,message=str(e))
