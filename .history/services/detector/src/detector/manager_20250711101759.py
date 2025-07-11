from common.models.detector import Detector
from detector.config import DetectorServiceConfig


class DetectorManager:
    
    def __init__(self,config:DetectorServiceConfig,detector: Detector):
        self.config: DetectorServiceConfig = config
        self.detector: Detector = detector
        
    async def setup_folder(self):
        