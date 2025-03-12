# PYTHON IMPORTS
import asyncio
import base64
from io import BytesIO
import json
import logging
import os
import shutil
import threading
from typing import Annotated, List, Optional, Tuple

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, In, RegEx
import cv2
from fastapi import Depends, Request
from pydantic import BaseModel
import pytesseract
from pytesseract import Output
from ultralytics import YOLO
import yaml
from PIL import Image

# LOCAL IMPORTS
from api.models.detector import (
    Detector,
    DetectorClass,
    DetectorImage,
    DetectorImageLabel,
    DetectorImageMode,
    DetectorTrainingSession,
)
from api.routers.ws import Websocket, WsManager
from api.models.recorder import Record
from api.utils.imaging import ImageGrid

# INITIALIZATION
log = logging.getLogger(__name__)
VIDEO_EXT = '.mp4'


class DetectorControllerConfig(BaseModel):
    path: str
    original: str
    name: str
    data: str
    runs: str
    classes: str
    video:str


class DetectorController:

    def __init__(self, config: DetectorControllerConfig,wsManager:WsManager):
        self.config: DetectorControllerConfig = config
        self.wsManager:WsManager = wsManager

    async def list(
        self,
        user_id: PydanticObjectId,
        project_id: PydanticObjectId,
        skip: int = 0,
        limit: int = 10,
        search: str = None,
    ) -> Tuple[int, List[Detector]]:
        qry = And(Detector.project == project_id)
        if search is not None:
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
        return [total, detectors]

    async def count(
        self, user_id: PydanticObjectId, project_id: PydanticObjectId
    ) -> int:
        return await Detector.find_many(Detector.project == project_id).count()

    async def load(
        self, user_id: PydanticObjectId, detector_id: PydanticObjectId
    ) -> Detector:
        detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if detector is None:
            raise Exception("Detector not found")
        return detector

    async def remove(
        self, user_id: PydanticObjectId, detector_id: PydanticObjectId
    ):
        detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if detector:
            folder_name = os.path.join(self.config.path, str(detector_id))
            if os.path.exists(folder_name):
                shutil.rmtree(folder_name)
            await detector.delete()
            return True
        raise Exception("Detector not found")

    async def add_image_label(
        self,
        user_id: PydanticObjectId,
        image_id: PydanticObjectId,
        xstart: float,
        xend: float,
        ystart: float,
        yend: float,
        classes: List[str],
    ) -> DetectorImageLabel:
        found = await DetectorImage.find_many(
            DetectorImage.id == image_id
        ).first_or_none()
        if found is None:
            raise Exception("Image not found")
        detector_id = found.detector

        class_ids = []
        for class_name in classes:
            found_class = await DetectorClass.find_many(
                DetectorClass.detector == detector_id, DetectorClass.name == class_name
            ).first_or_none()
            if found_class is None:
                found_class = await DetectorClass(
                    detector=detector_id, name=class_name
                ).insert()
            class_ids.append(found_class.id)

        detector_image_label = await DetectorImageLabel(
            image=image_id,
            classes=class_ids,
            xstart=xstart,
            xend=xend,
            ystart=ystart,
            yend=yend,
        ).insert()
        await self.update_folder(user_id, detector_id)
        return detector_image_label
    
    async def objects_from_record_frame(self,user_id:PydanticObjectId,detector_id:PydanticObjectId, record_id:PydanticObjectId, frame:int,confidence:float=0.1):
        detector = Detector.find_many(Detector.id == detector_id).first_or_none()
        if detector is None:
            raise Exception("workspace.detector.errors.not_found")
        
        filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
        cap = cv2.VideoCapture(filename)

        if not cap.isOpened():
            raise("Error: Could not open video file.")
            
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        
        # Read the specific frame
        ret, frame = cap.read()
        
        if not ret:
            raise Exception(f"Error: Could not read frame {frame}.")
        
        # Check if frame was successfully read
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        cap.release()
        
        log.debug("Loading model")
        model_path = os.path.join(self.config.path, detector.best)
        model = YOLO(model_path)
        
        log.debug("Detecting visual elements for frame: {0}".format(frame))
        visual_results = model(img, conf=confidence)  # predict on an image
        grid = ImageGrid(img.size[0], img.size[1])
        
        boxes = []
            

        

        # Access the results
        for result in visual_results:
            detections = json.loads(result.to_json())
            for detection in detections:
                x = detection["box"]["x1"]
                y = detection["box"]["y1"]
                w = detection["box"]["x2"] - detection["box"]["x1"]
                h = detection["box"]["y2"] - detection["box"]["y1"]
                boxes.append((x, y, w, h))
            # {'name': 'remote', 'class': 65, 'confidence': 0.63305, 'box': {'x1': 1.52126, 'y1': 49.41976, 'x2': 115.40047, 'y2': 946.6156}}
        
        best_rows, best_cols = grid.optimal_grid_size(boxes)      
        
        for result in visual_results:
            detections = json.loads(result.to_json())
            for detection in detections:
                c = detection['name']
                
                x = detection["box"]["x1"]
                y = detection["box"]["y1"]
                w = detection["box"]["x2"] - detection["box"]["x1"]
                h = detection["box"]["y2"] - detection["box"]["y1"]
                row, col = grid.classify_box(best_rows, best_cols, x, y, w, h)

        
        log.debug("Detecting text elements for frame: {0}".format(frame))
        # Get verbose data including boxes, confidences, line and page numbers
        text_results = pytesseract.image_to_data(img, output_type=Output.DICT)
        text_matches = []
        n_boxes = len(text_results["text"])
        for i in range(n_boxes):
            conf = int(text_results["conf"][i])
            text = text_results["text"][i]
            if conf > 60:
                x = text_results["left"][i]
                y = text_results["top"][i]
                w = text_results["width"][i]
                h = text_results["height"][i]
                page = text_results["page_num"][i]
                block = text_results["block_num"][i]
                par = text_results["par_num"][i]
                line = text_results["line_num"][i]
                word = text_results["word_num"][i]
        
        
    async def update_folder(
        self, user_id: PydanticObjectId, detector_id: PydanticObjectId
    ):

        classes = await DetectorClass.find_many(
            DetectorClass.detector == detector_id
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
        for clazz in classes:
            if clazz.name not in list(yaml_file["names"].values()):
                n = str(len(list(yaml_file["names"].keys())))
                yaml_file["names"][int(n)] = clazz.name
        for key in yaml_file["names"].keys():
            class_by_number[key] = yaml_file["names"][key]
            class_by_name[yaml_file["names"][key]] = key

        yaml_file["nc"] = len(list(yaml_file["names"].keys()))

        with open(yaml_filename, "w") as outfile:
            yaml.dump(yaml_file, outfile)

        for image in images:
            labels = await DetectorImageLabel.find_many(
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
            for label in labels:
                for clazz_id in label.classes:
                    dclass = await DetectorClass.find_many(
                        DetectorClass.id == clazz_id
                    ).first_or_none()
                    class_name = dclass.name
                    w = (label.xend - label.xstart) / image.width
                    h = (label.yend - label.ystart)/image.height
                    x = label.xend/image.width - (w/2)
                    y = label.yend/image.height - (h/2)
                    

                    # 16 0.048093 0.081250 0.051410 0.064583
                    line = "{0} {1:0.6f} {2:0.6f} {3:0.6f} {4:0.6f} ".format(
                        class_by_name[class_name], x, y, w, h
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
                
            
    async def remove_image_label(
        self, user_id: PydanticObjectId, detector_image_label_id: PydanticObjectId
    ) -> bool:
        found = await DetectorImageLabel.find_many(
            DetectorImageLabel.id == detector_image_label_id
        ).first_or_none()
        if found is None:
            raise Exception("Image label not found")
        await found.delete()

        return True

    async def count_image_label(
        self, user_id: PydanticObjectId, image_id: PydanticObjectId
    ) -> int:
        found = await DetectorImage.find_many(
            DetectorImage.id == image_id
        ).first_or_none()
        if found is None:
            raise Exception("Image not found")
        total = await DetectorImageLabel.find_many(
            DetectorImageLabel.image == image_id
        ).count()
        return total

    async def rename_image_label(
        self,
        user_id: PydanticObjectId,
        image_id: PydanticObjectId,
        skip: int,
        limit: int,
        search: str,
    ) -> Tuple[int, List[DetectorImageLabel]]:
        found = await DetectorImage.find_many(
            DetectorImage.id == image_id
        ).first_or_none()
        if found is None:
            raise Exception("Image not found")

        if search is not None and search.trim() != "":
            classes = []
            qry = And(
                DetectorClass.detector == found.detector,
                RegEx(DetectorClass.name, search, "i"),
            )
            found_classes = await DetectorClass.find_many(qry).to_list()
            for found_class in found_classes:
                classes.append(found_class.id)
            qry = And(
                DetectorImageLabel.image == image_id,
                In(DetectorImageLabel.classes, classes),
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
        return total, labels

    async def list_class(
        self,
        user_id: PydanticObjectId,
        detector_id: PydanticObjectId,
        skip: int,
        limit: int,
        search: str,
    ) -> Tuple[int, List[DetectorClass]]:
        found = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if found is None:
            raise Exception("Detector not found")

        if search is not None and search.trim() != "":
            classes = []
            qry = And(
                DetectorClass.detector == detector_id,
                RegEx(DetectorClass.name, search, "i"),
            )
        else:
            qry = And(DetectorClass.detector == detector_id)
        total = await DetectorClass.find_many(qry).count()
        classes = (
            await DetectorClass.find_many(qry)
            .skip(skip)
            .limit(limit)
            .sort(-DetectorClass.updated)
            .to_list()
        )
        await self.update_folder(user_id, detector_id)
        return total, classes

    async def count_class(
        self, user_id: PydanticObjectId, detector_id: PydanticObjectId
    ) -> int:
        found = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if found is None:
            raise Exception("Detector not found")

        total = await DetectorClass.find_many(
            DetectorClass.detector == detector_id
        ).count()
        return total

    async def remove_image(
        self, user_id: PydanticObjectId, image_id: PydanticObjectId
    ) -> bool:
        found = await DetectorImage.find_many(
            DetectorImage.id == image_id
        ).first_or_none()
        if found is None:
            raise Exception("Image not found")
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

        return True

    async def list_image(
        self,
        user_id: PydanticObjectId,
        detector_id: PydanticObjectId,
        skip: int,
        limit: int,
    ) -> Tuple[int, List[DetectorImage]]:
        found = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if not found:
            raise Exception("Detector not found")

        total = await DetectorImage.find_many(
            DetectorImage.detector == detector_id
        ).count()
        images = (
            await DetectorImage.find_many(DetectorImage.detector == detector_id)
            .skip(skip)
            .limit(limit)
            .sort(-DetectorImage.updated)
            .to_list()
        )
        return total, images

    async def count_image(
        self, user_id: PydanticObjectId, detector_id: PydanticObjectId
    ) -> int:
        found = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if not found:
            raise Exception("Detector not found")

        return await DetectorImage.find_many(
            DetectorImage.detector == detector_id
        ).count()

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
            print("Error decoding base64:", e)
            return None

    async def upload_image(
        self,
        user_id: PydanticObjectId,
        detector_id: PydanticObjectId,
        b64image: str,
        modes: List[DetectorImageMode],
    ) -> List[DetectorImage]:
        
        log.debug("Loading detector")
        found = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if not found:
            raise Exception("Detector not found")
        
        log.debug("Loading image")
        if "," in b64image:
            bsource = b64image.split(",")[1]
        else:
            bsource = b64image
        img = Image.open(BytesIO(self.decode_base64(bsource)))
        width, height = img.size

        log.debug("Creating new detector image document")
        ret = []
        for mode in modes:
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
            
            ret.append(detector_image)
        await self.update_folder(user_id, detector_id)
        return ret
    
    
    async def train(
        self,
        session:str,
        user_id: PydanticObjectId,
        detector_id: PydanticObjectId,
        epochs: int = 100,
        image_size: int = 640,
    ):
        detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if detector is None:
            raise Exception("Detector not found")
        
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
                #    f"Class Loss: {results.cls.loss:.4f}, "
                #    f"Object Loss: {results.dfl.loss:.4f}"
                
                #training_session.box_loss = results['box']['loss']
                #training_session.class_loss = results['cls']['loss']
                #training_session.object_loss = results['dfl']['loss']
                
            asyncio.run(self.wsManager.update(training_session,session))
            

        # Load a COCO-pretrained YOLO11n model
        log.debug("Loading YOLO Model")
        if detector.best is None:
            path = os.path.join(self.config.path, str(detector_id), self.config.name)
            if not os.path.exists(path):
                raise Exception("Detector model not found")
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
            await self.wsManager.update(training_session,session)
            log.debug("Results are saved into: {0}".format(results.save_dir))
            detector.best = os.path.join(results.save_dir,'weights/best.pt')
            detector.last = os.path.join(results.save_dir,'weights/last.pt')
            
            await detector.save()
            
        train_thread = threading.Thread(target=training, args=(path,), daemon=True)
        train_thread.start()

    async def create(
        self,
        user_id: PydanticObjectId,
        project_id: PydanticObjectId,
        name: str,
        description: str,
        origin: Optional[PydanticObjectId] = None,
    ) -> Detector:
        others_found = await Detector.find_many(
            Detector.project == project_id, Detector.name == name
        ).first_or_none()
        if others_found:
            raise Exception("Another detector with this username already found")

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
                raise Exception("Original detector not found")

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

        return detector

    async def update(
        self,
        user_id: PydanticObjectId,
        detector_id: PydanticObjectId,
        name: str,
        description: str,
    ) -> Detector:
        found = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if not found:
            raise Exception("Detector not found")
        others_found = await Detector.find_many(
            Detector.project == found.project,
            Detector.name == name,
            Detector.id != found.id,
        ).first_or_none()
        if others_found:
            raise Exception("Another detector with this username already found")
        found.name = name
        found.description = description
        await found.save()
        return found


async def get_detector_controller(request: Request, wsManager: Websocket) -> DetectorController:
    if not hasattr(request.app.state, "detector"):
        request.app.state.detector = DetectorController(
            request.app.state.config.detector, wsManager
        )
    return request.app.state.detector


GetDetectorController = Annotated[DetectorController, Depends(get_detector_controller)]
