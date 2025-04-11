
# PYTHON IMPORTS
from datetime import time
from enum import Enum
import json
import logging
import os
import re
from typing import Annotated, List, Literal, Union

# LIBRARY IMPORTS
import pyautogui
from pydantic import BaseModel, Field
import pytesseract
from pytesseract import Output
from ultralytics import YOLO

# LOCAL IMPORTS
from common.models.defaults import empty_list
from common.utils.imaging import ImageGrid

# INITIALIZATION
log = logging.getLogger(__name__)

def get_indent(value:int=0) -> str:
    t = ''
    for i in range(value):
        t += '\t'
    return t




class GrammarContext(BaseModel):
    line: int
    column: int


def default_grammar_ctx():
    return GrammarContext(line=0,column=0)    
    
class RuntimeException(Exception):
    
    def __init__(self,message:str,ctx):
        self.line = ctx.start.line
        self.column = ctx.start.column
        self.message = message
        
    def __repr__(self):
        return 'Error at line {0} and column {1}: {2}'.format(self.line,self.column,self.message)
    
    def __str__(self):
        return self.__repr__()
    

        
class RuntimeRegistry():
    def __init__(self):
        self.selectors = {}
        self.detectors = {}
        self.operations = {}
        self.sequences = {}
        self.current_detector = None
        self.current_detector_confidence = 0.1
        
class Runtime:
    
    def __init__(self):
        self.registry = RuntimeRegistry()
        self.screenWidth, self.screenHeight = pyautogui.size()
    

class Selector(BaseModel):
    type: str
    ctx: GrammarContext = Field(default_factory=default_grammar_ctx)
    
    def render(self, indent:int =0) -> str:
        return ""
    
    def execute(self,runtime:Runtime):
        pass


class SelectorReference(Selector):
    type: Literal["selector.reference"] = "selector.reference"
    reference: str

    def render(self,indent:int=0):
        return get_indent(indent)+self.reference
    
    def execute(self,runtime:Runtime):
        if self.reference not in runtime.registry.selectors:
            raise RuntimeException('player.runtime.errors.selector_not_found',self.ctx)
        selector = runtime.registry.selectors[self.reference]
        return selector.execute(runtime)


class LabelSelector(Selector):
    type: Literal["selector.label"] = "selector.label"
    value: str
    order: List[int] = Field(default_factory=empty_list)

    def render(self,indent:int=0) -> str:
        torder = ""
        for el in self.order:
            torder += ",{0}".format(el)
        return get_indent(indent)+'label("{0}"{1})'.format(self.value, torder)

    def execute(self, runtime:Runtime):
        img = pyautogui.screenshot()

        log.debug("Detecting visual elements")
        visual_results = runtime.registry.current_detector(img, conf=runtime.registry.current_detector_confidence)  # predict on an image

        # Access the results
        visual_matches = []
        for result in visual_results:
            detections = json.loads(result.to_json())

            # {'name': 'remote', 'class': 65, 'confidence': 0.63305, 'box': {'x1': 1.52126, 'y1': 49.41976, 'x2': 115.40047, 'y2': 946.6156}}
            for detection in detections:
                class_name = detection["name"]
                confidence = detection["confidence"]
                if class_name == self.value:
                    visual_matches.append(detection)

        if len(visual_matches) == 1:
            visual_match = visual_matches[0]
            confidence = visual_match["confidence"]
            class_name = visual_match["name"]
            class_id = visual_match["class"]
            x = visual_match["box"]["x1"]
            y = visual_match["box"]["y1"]
            w = visual_match["box"]["x2"] - visual_match["box"]["x1"]
            h = visual_match["box"]["y2"] - visual_match["box"]["y1"]
            log.debug(
                "I found the unique visual element [{0}] for this step with a confidence of: {1}".format(
                    class_name, confidence
                )
            )
            
            return x,y,w,h,confidence
            

        if (
            len(visual_matches) > 1
            and len(self.order) == 0
        ):
            msg = "There are too many visual elements matching this step ({0}) and no further text matching patterns has been specified".format(
                len(visual_matches)
            )
            log.debug(msg)
            return None

        if (
            len(visual_matches) > 1
            and len(self.order) > 0
        ):
            if len(self.order) == 1:
                ordering = self.order[0]
                if len(visual_matches) < ordering:
                    msg = "The visual elements cannot match the order({0})".format(
                        ordering
                    )
                    log.debug(msg)
                    return None
                else:
                    visual_match = visual_matches[ordering]
                    confidence = visual_match["confidence"]
                    class_name = visual_match["name"]
                    class_id = visual_match["class"]
                    x = visual_match["box"]["x1"]
                    y = visual_match["box"]["y1"]
                    w = visual_match["box"]["x2"] - visual_match["box"]["x1"]
                    h = visual_match["box"]["y2"] - visual_match["box"]["y1"]
                    log.debug(
                        "I found the unique visual element [{0}] for this step with a confidence of: {1}".format(
                            class_name, confidence
                        )
                    )
                    return x,y,w,h,confidence
            else:
                target_x = self.order[0]
                target_y = self.order[1]
                grid = ImageGrid(img.size[0], img.size[1])
                boxes = []
                for visual_match in visual_matches:
                    x = visual_match["box"]["x1"]
                    y = visual_match["box"]["y1"]
                    w = visual_match["box"]["x2"] - visual_match["box"]["x1"]
                    h = visual_match["box"]["y2"] - visual_match["box"]["y1"]
                    boxes.append((x, y, w, h))

                best_rows, best_cols = grid.optimal_grid_size(boxes)

                for visual_match in visual_matches:
                    confidence = visual_match["confidence"]
                    class_name = visual_match["name"]
                    class_id = visual_match["class"]
                    x = visual_match["box"]["x1"]
                    y = visual_match["box"]["y1"]
                    w = visual_match["box"]["x2"] - visual_match["box"]["x1"]
                    h = visual_match["box"]["y2"] - visual_match["box"]["y1"]
                    row, col = grid.classify_box(best_rows, best_cols, x, y, w, h)
                    
                    if row == target_y and col == target_x:
                        return x,y,w,h,confidence

        return None


class TextSelector(Selector):
    type: Literal["selector.text"] = "selector.text"
    value: str
    order: List[int] = Field(default_factory=empty_list)

    def render(self,indent:int=0) -> str:
        torder = ""
        for el in self.order:
            torder += ",{0}".format(el)
        return get_indent(indent)+'text("{0}"{1})'.format(self.value, torder)
    
    def execute(self, runtime:Runtime):
        img = pyautogui.screenshot()
        
        log.debug("Detecting text elements")
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

                
                if re.match(self.value, text):
                    text_matches.append(
                        (text, conf, x, y, w, h, page, block, par, line, word)
                    )

        if len(text_matches) == 0:
            msg = "There are no text elements matching this step as well as visual elements matching"
            log.debug(msg)
            return None

        if len(text_matches) == 1:
            text_match = text_matches[0]
            text = text_match[0]
            conf = text_match[1]
            log.debug(
                "I found the unique text element [{0}] for this step with a confidence of: {1}".format(
                    text, conf
                )
            )
            x = text_match[2]
            y = text_match[3]
            w = text_match[4]
            h = text_match[5]
            page = text_match[6]
            block = text_match[7]
            par = text_match[8]
            line = text_match[9]
            word = text_match[10]
            return x,y,w,h,conf

        if len(text_matches) > 1 and len(self.order) == 0:
            msg = "There are too many text elements matching this step ({0}) and no further order matching pattern has been specified".format(
                len(text_matches)
            )
            log.debug(msg)
            return None

        if len(text_matches) > 1 and len(self.order) > 0:
            if len(self.order) == 1:
                ordering = self.order[0]
                if len(text_matches) < ordering:
                    msg = "The text elements cannot match the order({0})".format(
                        ordering
                    )
                    log.debug(msg)
                    return None
                else:
                    text_match = text_matches[ordering]
                    text = text_match[0]
                    conf = text_match[1]
                    log.debug(
                        "I found the unique text element [{0}] for this step with a confidence of: {1}".format(
                            text, conf
                        )
                    )
                    x = text_match[2]
                    y = text_match[3]
                    w = text_match[4]
                    h = text_match[5]
                    page = text_match[6]
                    block = text_match[7]
                    par = text_match[8]
                    line = text_match[9]
                    word = text_match[10]

                    return x,y,w,h,conf
            elif len(self.order) > 1:
                lines_ups = []
                target_x = self.order[0]
                target_y = self.order[1]
                for text_match in text_matches:
                    page = text_match[6]
                    block = text_match[7]
                    par = text_match[8]
                    line = text_match[9]
                    word = text_match[10]
                    if line == target_y:
                        lines_ups.append(text_match)
                founds = []
                for line_up in lines_ups:
                    page = line_up[6]
                    block = line_up[7]
                    par = line_up[8]
                    line = line_up[9]
                    word = line_up[10]
                    if block == target_x:
                        founds.append(line_up)

                if len(founds) == 0:
                    msg = "The text elements cannot match the order({0,{1})".format(
                        target_x, target_y
                    )
                    log.debug(msg)
                    return None

                if len(founds) > 1:
                    msg = "There are too many text elements matching this step ({0}) and no further order matching pattern has been specified".format(
                        len(text_matches)
                    )
                    log.debug(msg)
                    return None

                if len(founds) == 1:
                    text_match = founds[0]
                    text = text_match[0]
                    conf = text_match[1]
                    log.debug(
                        "I found the unique text element [{0}] for this step with a confidence of: {1}".format(
                            text, conf
                        )
                    )
                    x = text_match[2]
                    y = text_match[3]
                    w = text_match[4]
                    h = text_match[5]
                    page = text_match[6]
                    block = text_match[7]
                    par = text_match[8]
                    line = text_match[9]
                    word = text_match[10]
                    return x,y,w,h,conf
        return None


class PositionSelector(Selector):
    type: Literal["selector.position"] = "selector.position"
    x: float
    y: float

    def render(self,indent:int=0) -> str:
        tx = "{:.2f}".format(self.x)
        ty = "{:.2f}".format(self.y)
        return get_indent(indent)+"position({0},{1})".format(tx, ty)
    
    def execute(self, runtime):
        return self.x-2,self.y-2,4,4,1.0


class RegexSelector(Selector):
    type: Literal["selector.regex"] = "selector.regex"
    value: str
    order: List[int] = Field(default_factory=empty_list)

    def render(self,indent:int=0) -> str:
        torder = ""
        for el in self.order:
            torder += ",{0}".format(el)
        return get_indent(indent)+'regex("{0}"{1})'.format(self.value, torder)

SELECTOR_TYPES = Union[
    LabelSelector,
    PositionSelector,
    TextSelector,
    RegexSelector,
    SelectorReference
]

SELECTORS = Annotated[SELECTOR_TYPES, Field(discriminator="type")]



class Operation(BaseModel):
    type: str
    ctx: GrammarContext = Field(default_factory=default_grammar_ctx)

    def render(self,indent:int=0) -> str:
        return ""
    
    def execute(self,runtime:Runtime):
        pass
    
    


class OperationReference(Operation):
    type: Literal["operation.reference"] = "operation.reference"
    reference: str

    def render(self,indent:int=0):
        return get_indent(indent)+self.reference
    
    def execute(self, runtime):
        if self.reference not in runtime.registry.operations:
            raise RuntimeException('player.runtime.errors.operation_not_found',self.ctx)
        
        op = runtime.registry.operations[self.reference]
        return op.execute(runtime)


class WaitOperation(Operation):
    type: Literal["operation.wait"] = "operation.wait"
    value: int = 1000
    selector: SELECTOR_TYPES

    def render(self,indent:int=0):
        return get_indent(indent)+"wait({0},{1})".format(self.selector.render(), self.value)
    
    def execute(self, runtime):
        found = None
        start_time = time.time()  # current time in seconds (float)
        while found is None and elapsed_time_ms < self.value:
            found = self.selector.execute(runtime)
            end_time = time.time()
            elapsed_time_ms = (end_time - start_time) * 1000  # convert to milliseconds
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        return found

class MouseOperationButton(str, Enum):
    LEFT = "left"
    MIDDLE = "middle"
    RIGHT = "right"


class MousePressOperation(Operation):
    type: Literal["operation.mouse.press"] = "operation.mouse.press"
    selector: SELECTOR_TYPES
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)

    def render(self,indent:int=0):
        but = "left"
        if self.button == MouseOperationButton.MIDDLE:
            but = "middle"
        elif self.button == MouseOperationButton.RIGHT:
            but = "right"
        return get_indent(indent)+"mousePress({0},{1})".format(self.selector.render(), but)
    
    def execute(self, runtime:Runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        if self.button == MouseOperationButton.LEFT:
            but = 'left'
        elif self.button == MouseOperationButton.MIDDLE:
            but = 'middle'
        elif self.button == MouseOperationButton.RIGHT:
            but = 'right'
            
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        pyautogui.mouseDown(guiX, guiY,but, duration=1)
        return True


class MouseReleaseOperation(Operation):
    type: Literal["operation.mouse.release"] = "operation.mouse.release"
    selector: SELECTOR_TYPES
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)

    def render(self,indent:int=0):
        but = "left"
        if self.button == MouseOperationButton.MIDDLE:
            but = "middle"
        elif self.button == MouseOperationButton.RIGHT:
            but = "right"
        return get_indent(indent)+"mouseRelease({0},{1})".format(self.selector.render(), but)
    
    def execute(self, runtime:Runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        if self.button == MouseOperationButton.LEFT:
            but = 'left'
        elif self.button == MouseOperationButton.MIDDLE:
            but = 'middle'
        elif self.button == MouseOperationButton.RIGHT:
            but = 'right'
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        pyautogui.mouseUp(guiX, guiY,but, duration=1)
        return True


class MouseClickOperation(Operation):
    type: Literal["operation.mouse.click"] = "operation.mouse.click"
    selector: SELECTOR_TYPES
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)

    def render(self,indent:int=0):
        but = "left"
        if self.button == MouseOperationButton.MIDDLE:
            but = "middle"
        elif self.button == MouseOperationButton.RIGHT:
            but = "right"
        return get_indent(indent)+"mouseClick({0},{1})".format(self.selector.render(), but)
    
    def execute(self, runtime:Runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        
        if self.button == MouseOperationButton.LEFT:
            pyautogui.leftClick(guiX,guiY, duration=1)
        elif self.button == MouseOperationButton.MIDDLE:
            pyautogui.middleClick(guiX,guiY, duration=1)
        elif self.button == MouseOperationButton.RIGHT:
            pyautogui.rightClick(guiX,guiY, duration=1)
        return True


class MouseDoubleClickOperation(Operation):
    type: Literal["operation.mouse.double.click"] = "operation.mouse.double.click"
    selector: SELECTOR_TYPES
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)

    def render(self,indent:int=0):
        but = "left"
        if self.button == MouseOperationButton.MIDDLE:
            but = "middle"
        elif self.button == MouseOperationButton.RIGHT:
            but = "right"
        return get_indent(indent)+"mouseDoubleClick({0},{1})".format(self.selector.render(), but)

    def execute(self, runtime:Runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        if self.button == MouseOperationButton.LEFT:
            pyautogui.doubleClick(guiX,guiY, duration=1)
        elif self.button == MouseOperationButton.MIDDLE:
            pyautogui.doubleClick(guiX,guiY, duration=1)
        elif self.button == MouseOperationButton.RIGHT:
            pyautogui.doubleClick(guiX,guiY, duration=1)
            
        return True
        

class MouseScrollOperation(Operation):
    type: Literal["operation.mouse.scroll"] = "operation.mouse.scroll"
    selector: SELECTOR_TYPES
    dx: int
    dy: int

    def render(self,indent:int=0):
        return get_indent(indent)+"mouseScroll({0},{1},{2})".format(self.selector.render(),self.dx, self.dy)
    
    def execute(self, runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        pyautogui.moveTo(guiX,guiY)
        pyautogui.scroll(0, self.dx, self.dy)
        return True


class KeyPressOperation(Operation):
    type: Literal["operation.key.press"] = "operation.key.press"
    value: str
    selector: SELECTOR_TYPES
    

    def render(self,indent:int=0):
        return get_indent(indent)+'keyPress({0},"{1}")'.format(self.selector.render(),self.value)
    
    def execute(self, runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        #pyautogui.click(guiX,guiY)
        pyautogui.keyDown(self.value)
        return True
    


class KeyTypeOperation(Operation):
    type: Literal["operation.key.type"] = "operation.key.type"
    value: str
    selector: SELECTOR_TYPES
    

    def render(self,indent:int=0):
        return get_indent(indent)+'keyType({0},"{1}")'.format(self.selector.render(),self.value)
    
    def execute(self,runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        #pyautogui.click(guiX,guiY)
        pyautogui.typewrite(self.value)
        return True



class KeyReleaseOperation(Operation):
    type: Literal["operation.key.release"] = "operation.key.release"
    value: str
    selector: SELECTOR_TYPES
    

    def render(self,indent:int=0):
        return get_indent(indent)+'keyRelease({0}"{1}")'.format(self.selector.render(),self.value)
    
    
    def execute(self,runtime):
        found = self.selector.execute(runtime)
        if found is None:
            raise RuntimeException('player.runtime.errors.timeout',self.ctx)
        x,y,w,h,conf = found
        guiX = (x+w/2)*runtime.screenWidth
        guiY = (y+h/2)*runtime.screenHeight
        pyautogui.keyUp(self.value)
        return True


OPERATION_TYPES = Union[
    MousePressOperation,
    MouseClickOperation,
    MouseReleaseOperation,
    MouseDoubleClickOperation,
    MouseScrollOperation,
    KeyPressOperation,
    KeyReleaseOperation,
    KeyTypeOperation,
    WaitOperation,
    OperationReference
]

OPERATIONS = Annotated[OPERATION_TYPES, Field(discriminator="type")] 


class Statement(BaseModel):
    type: str
    ctx: GrammarContext = Field(default_factory=default_grammar_ctx)

    def render(self,indent:int=0) -> str:
        return ""
    
    def execute(self,runtime:Runtime):
        pass


class CreateDetectorStatement(Statement):
    type: Literal["statement.create.detector"] = "statement.create.detector"
    id: str
    value: str

    def render(self,indent:int=0):
        return get_indent(indent)+'{0} = detector("{1}");'.format(self.id, self.value)
    
    def execute(self,runtime:Runtime):
        model_path = os.path.join(os.getcwd(),self.detector_path,self.value)
        if not os.path.exists(model_path):
            raise RuntimeException('player.runtime.errors.detector_not_found',self.ctx)
        
        if id in runtime.registry.detectors:
            log.warning('Detector has been already registered with id: {0}'.format(id))
        
        log.debug('Loading detector object model from path: {0}'.format(model_path))
        model = YOLO(model_path)
        
        log.debug('Storing the detector object model to registry with id: {0}'.format(id))
        runtime.registry.detectors[id] = model
        return model


class UseDetectorStatement(Statement):
    type: Literal["statement.use.detector"] = "statement.use.detector"
    id: str
    confidence: float = Field(default=0.1)

    def render(self,indent:int=0):
        tconf = "{:.2f}".format(self.confidence)
        return get_indent(indent)+"{0} = use({1},{2});".format(self.id, self.value, tconf)
    
    def execute(self,runtime:Runtime):
        if self.id not in runtime.registry.detectors:
            raise RuntimeException('player.runtime.errors.detector_not_found',self.ctx)
            
        log.debug('Setting current detector: {0}'.format({self.id}))
        runtime.registry.current_detector = runtime.registry.detectors[self.id]
        
        log.debug('Setting current detector confidence: {0}'.format(self.confidence))
        runtime.registry.current_detector_confidence = self.confidence
        return runtime.registry.detectors[self.id]
        


class CreateSelectorStatement(Statement):
    type: Literal["statement.create.selector"] = "statement.create.selector"
    id: str
    selector: SELECTOR_TYPES

    def render(self,indent:int=0):
        return get_indent(indent)+"{0} = {1};".format(self.id, self.selector.render())
    
    def execute(self, runtime):
        if self.id in runtime.registry.selectors:
            log.warning('Selector already in the registry with id: {0}'.format(self.id))
        
        log.debug('Storing selector to the registry with id: {0}'.format(self.id))
        runtime.registry.selectors[self.id] = self.selector
        return self.selector


class CreateOperationStatement(Statement):
    type: Literal["statement.create.operation"] = "statement.create.operation"
    id: str
    operation: OPERATION_TYPES

    def render(self,indent:int=0):
        return get_indent(indent)+"{0} = {1};".format(self.id, self.operation.render())
    
    def execute(self, runtime):
        if self.id in runtime.registry.operations:
            log.warning('Operation already in the registry with id: {0}'.format(self.id))
        
        log.debug('Storing operation to the registry with id: {0}'.format(self.id))
        runtime.registry.operations[self.id] = self.operation
        return self.operation


class CreateSequenceStatement(Statement):
    type: Literal["statement.create.sequence"] = "statement.create.sequence"
    id: str
    statements: List[Statement] = Field(default=empty_list)

    def render(self,indent:int=0):
        content = ""
        counter = 0
        
        for stmt in self.statements:
            nl = ''
            if counter > 0:
                nl = '\r\n'
            content += "{0}{1}".format(nl,stmt.render(indent+1))
            counter+=1
        return get_indent(indent)+"{0} = sequence {{\r\n{1}\r\n}};".format(self.id, content)
    
    def execute(self, runtime):
        if self.id in runtime.registry.sequences:
            log.warning('Sequence already in the registry with id: {0}'.format(self.id))
        
        log.debug('Storing sequence to the registry with id: {0}'.format(self.id))
        runtime.registry.sequences[self.id] = self.statements
        return self.statements


class RunOperationStatement(Statement):
    type: Literal["statement.run.operation"] = "statement.run.operation"
    operation: OPERATION_TYPES

    def render(self,indent:int=0):
        return get_indent(indent)+"{0};".format(self.operation.render())
    
    def execute(self, runtime):
        return self.operation.execute(runtime)