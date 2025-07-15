import base64
from io import BytesIO
import logging
from PIL import Image

log = logging.getLogger(__name__)

class GraphicsController:
    
    @staticmethod
    def load_pil_image_from_base64_string(data:str) -> Image:
        log.debug("Loading image")
            
        b64image = data
        if "," in b64image:
            bsource = b64image.split(",")[1]
        else:
            bsource = b64image
        img = Image.open(BytesIO(GraphicsController.decode_base64(bsource)))
        return img
    
    @staticmethod
    def decode_base64(b64image: str):
        # Add padding if needed
        padding = len(b64image) % 4
        if padding != 0:
            b64image += "=" * (4 - padding)
        try:
            # Decode the Base64 string to bytes
            decoded_bytes = base64.decodebytes(bytes(b64image, "utf-8"))
            return decoded_bytes
        except Exception as e:
            return None