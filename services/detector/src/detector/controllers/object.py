import json
import logging
import os
from typing import List
from PIL import Image
from beanie import PydanticObjectId
from ultralytics import YOLO

from common.models.detector import DetectObject, Detector, DetectorImage, DetectorImageLabel
from common.utils.imaging import ImageGrid


log = logging.getLogger(__name__)

CACHE_YOLOS = {}

class ObjectController:
    
    
    
    def load_yolo(models_path:str,models_name:str,detector:Detector) -> YOLO:
        log.debug("Loading YOLO Model")
        if detector.best is None:
            path = os.path.join(
                models_path, str(detector.id), models_name
            )
            if not os.path.exists(path):
                raise Exception("detector.errors.not_found")
        else:
            if not os.path.exists(detector.best):
                raise Exception("detector.errors.not_found")
            path = detector.best

        if path not in CACHE_YOLOS:
            model = YOLO(path)
            CACHE_YOLOS[path] = model
        else:
            model = CACHE_YOLOS[path]
        log.debug("YOLO Model loaded")
        return model
    
    def detect_objects(model:YOLO,img:Image,confidence:float) -> List[DetectObject]:
        width, height = img.size
        grid = ImageGrid(width, height)
        visual_results = model(
            img, conf=confidence or 0.7
        )  # predict on an image

        boxes = []
        for result in visual_results:
            detections = json.loads(result.to_json())
            for detection in detections:
                x = detection["box"]["x1"]
                y = detection["box"]["y1"]
                w = detection["box"]["x2"] - detection["box"]["x1"]
                h = detection["box"]["y2"] - detection["box"]["y1"]
                boxes.append((x, y, w, h))
        log.debug("Found boxes: {0}".format(len(boxes)))
        if len(boxes) > 1:
            best_rows, best_cols = grid.optimal_grid_size(boxes)

        objects = []
        for result in visual_results:
            detections = json.loads(result.to_json())
            for detection in detections:
                confidence = detection["confidence"]
                code = detection["class"]
                name = detection["name"]
                x = detection["box"]["x1"]
                y = detection["box"]["y1"]
                w = detection["box"]["x2"] - detection["box"]["x1"]
                h = detection["box"]["y2"] - detection["box"]["y1"]
                if len(boxes) > 1:
                    row, col = grid.classify_box(best_rows, best_cols, x, y, w, h)
                else:
                    row = 0
                    col = 0
                objects.append(
                    DetectObject(
                        x=x,
                        y=y,
                        w=w,
                        h=h,
                        confidence=confidence,
                        code=code,
                        name=name,
                        row=row,
                        col=col,
                    )
                )
        return objects
    
    
    @staticmethod
    async def remove_image_label(id:str):
        detector_image_label_id = PydanticObjectId(id)
        found = await DetectorImageLabel.find_many(
            DetectorImageLabel.id == detector_image_label_id
        ).first_or_none()
        if found is None:
            raise Exception("detector.image.errors.label_not_found")
        await found.delete()

    
    @staticmethod
    async def count_image_labels(id:str) -> int:
        image_id = PydanticObjectId(id)
        found = await DetectorImage.find_many(
            DetectorImage.id == image_id
        ).first_or_none()
        if found is None:
            raise Exception("detector.image.errors.not_found")
        total = await DetectorImageLabel.find_many(
            DetectorImageLabel.image == image_id
        ).count()
        return total