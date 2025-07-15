import logging
from typing import List

import pytesseract
from pytesseract import Output

from common.rpc.detector_pb2 import DetectText



log = logging.getLogger(__name__)

class TextController:
    
    @staticmethod
    def detect_texts(img,confidence:float) -> List[DetectText]:
        width, height = img.size

        log.debug("Detecting text elements")
        confidence_level = int(round(confidence * 100))
        # Get verbose data including boxes, confidences, line and page numbers
        text_results = pytesseract.image_to_data(img, output_type=Output.DICT)
        n_boxes = len(text_results["text"])
        texts = []
        for i in range(n_boxes):
            confidence = int(text_results["conf"][i])
            text = text_results["text"][i]
            if confidence >= confidence_level and text.strip() != "":
                x = text_results["left"][i] / width
                y = text_results["top"][i] / height
                w = text_results["width"][i] / width
                h = text_results["height"][i] / height
                page = text_results["page_num"][i]
                block = text_results["block_num"][i]
                par = text_results["par_num"][i]
                line = text_results["line_num"][i]
                word = text_results["word_num"][i]
                texts.append(
                    DetectText(
                        x=x,
                        y=y,
                        w=w,
                        h=h,
                        page=page,
                        block=block,
                        par=par,
                        line=line,
                        word=word,
                        value=text,
                        confidence=confidence / 100,
                    )
                )
        return texts