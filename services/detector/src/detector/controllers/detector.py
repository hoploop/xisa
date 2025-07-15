import logging
from typing import Optional

from beanie import PydanticObjectId

from common.models.detector import Detector


log = logging.getLogger(__name__)

class DetectorController:
    
    @staticmethod
    async def load_detector(id:str) -> Detector:
        log.debug("Loading detector")
        detector_id = PydanticObjectId(id)
        detector = await Detector.find_many(
            Detector.id == detector_id
        ).first_or_none()
        if detector is None:
            raise Exception("detector.errors.not_found")
        return detector