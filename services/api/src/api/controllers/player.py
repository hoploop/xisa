# PYTHON IMPORTS
from itertools import combinations
import json
import logging
import os
import re
import time
from typing import Annotated, List

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from fastapi import Depends, Request
from pydantic import BaseModel
import numpy as np
import pyautogui
import pytesseract
from pytesseract import Output
from ultralytics import YOLO

# LOCAL IMPORTS
from api.models.player import Scenario, Step, StepResult, StepResultStatus
from api.routers.ws import Websocket
from api.models.detector import Detector
from api.models.defaults import utc_now
from api.models.recorder import Event
from common.utils.imaging import ImageGrid

# INITIALIZATION
log = logging.getLogger(__name__)


class PlayerControllerConfig(BaseModel):
    detectors: str


class PlayerController:

    def __init__(self, config: PlayerControllerConfig):
        self.config: PlayerControllerConfig = config
        self.size = pyautogui.size()

    async def move_to(self, x, y, duration=1):
        pyautogui.moveTo(x, y, duration=duration)

    async def move_rel(self, x, y, duration=1):
        pyautogui.moveRel(x, y, duration=duration)

    async def drag_rel(self, x, y, duration=1, button="primary"):
        pyautogui.dragRel(x, y, duration=duration, button=button)

    async def drag_to(self, x, y, duration=1, button="primary"):
        pyautogui.dragTo(x, y, duration=duration, button=button)

    async def position(self):
        return pyautogui.position()

    async def mouse_click(self, x, y, clicks=1, button="primary"):
        pyautogui.click(x, y, clicks, button=button)

    async def mouse_down(self, x, y, button="primary", duration=0):
        pyautogui.mouseDown(x, y, button, duration=duration)

    async def mouse_up(self, x, y, button="primary", duration=0):
        pyautogui.mouseUp(x, y, button, duration=duration)

    async def scroll(self, value_up, x, y):
        pyautogui.scroll(value_up, x, y)

    async def type(self, value: List[str]):
        pyautogui.typewrite(value)

    async def key_down(self, key):
        pyautogui.keyDown(key)

    async def key_up(self, key):
        pyautogui.keyUp(key)

    async def hotkeys(self, keys: List[str]):
        pyautogui.hotkey(*keys)
        # pyautogui.hotkey("ctrlleft", "a")

    async def scenario_prepare(
        self,
        session: str,
        user_id: PydanticObjectId,
        scenario_id: PydanticObjectId,
        detector_id: PydanticObjectId,
    ) -> YOLO:

        log.debug("Loading detector")
        detector = await Detector.find_many(Detector.id == detector_id).first_or_none()
        if detector is None:
            raise Exception("player.errors.detector_not_found")

        if detector.best is None:
            raise Exception("player.errors.detector_not_trained")

        log.debug("Loading scenario")
        scenario = await Scenario.find_many(Scenario.id == scenario_id).first_or_none()
        if scenario is None:
            raise Exception("player.errors.scenario_not_found")

        log.debug("Loading model")
        model_path = os.path.join(self.config.detectors, detector.best)
        model = YOLO(model_path)

        log.debug("Validating model")
        metrics = model.val()
        # print(metrics.box.map)  # mAP50-95

    async def scenario_play(
        self, session: str, user_id: PydanticObjectId, scenario: Scenario, model: YOLO
    ):
        steps = (
            await Step.find_many(Step.scenario == scenario.id)
            .sort(Step.order)
            .to_list()
        )
        if len(steps) == 0:
            raise Exception("player.errors.scenario_no_steps")

        for step in steps:
            ret = False
            retry = 0
            while retry < step.retry and ret == False:
                ret = await self.play_step(session, user_id, scenario, step)
                time.sleep(step.duration)
                retry += 1
            if ret == False:
                break
            
            
    async def perform_event(self,event:Event,ex,ey,ew,eh):
        x = int(ex+ew/2)
        y = int(ey+eh/2)
        if event.type == 'mouse.click.left':
            await self.mouse_click(x,y,1,button='primary')
        elif event.type == 'mouse.press.left':
            await self.mouse_down(x,y,button='primary')
        

    async def step_play(
        self,
        session: str,
        user_id: PydanticObjectId,
        scenario: Scenario,
        step: Step,
        model: YOLO,
    ) -> bool:
        step_result = StepResult(
            scenario=scenario.id,
            step=step.id,
            start=utc_now,
            status=StepResultStatus.RUNNING,
        )
        event = await Event.find_many(Event.id == step.event,with_children=True).first_or_none()
        
        await step_result.insert()
        img = pyautogui.screenshot()

        log.debug("Detecting visual elements for step: {0}".format(step.order))
        visual_results = model(img, conf=0.1)  # predict on an image

        # Access the results
        visual_matches = []
        for result in visual_results:
            detections = json.loads(result.to_json())

            # {'name': 'remote', 'class': 65, 'confidence': 0.63305, 'box': {'x1': 1.52126, 'y1': 49.41976, 'x2': 115.40047, 'y2': 946.6156}}
            for detection in detections:
                class_name = detection["name"]
                confidence = detection["confidence"]
                if class_name in step.by_class:
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
            # TODO: Now I can perform the step action and go to the next step
            # After performing I proceed to save the results and return
            await self.perform_event(event,x,y,w,h)
            step_result.end = utc_now
            step_result.status = StepResultStatus.SUCCESS
            await step_result.save()
            return True

        if (
            len(visual_matches) > 1
            and len(step.by_order) == 0
            and len(step.by_text) == 0
        ):
            msg = "There are too many visual elements matching this step ({0}) and no further text matching patterns has been specified".format(
                len(visual_matches)
            )
            log.debug(msg)
            step_result.end = utc_now
            step_result.status = StepResultStatus.TRAINING_REQUIRED
            step_result.message = msg
            await step_result.save()
            return False

        if (
            len(visual_matches) > 1
            and len(step.by_text) == 0
            and len(step.by_order) > 0
        ):
            if len(step.by_order) == 1:
                ordering = step.by_order[0]
                if len(visual_matches) < ordering:
                    msg = "The visual elements cannot match the order({0})".format(
                        ordering
                    )
                    log.debug(msg)
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.FAIL
                    step_result.message = msg
                    await step_result.save()
                    return False
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
                    # TODO: Now I can perform the step action and go to the next step
                    # After performing I proceed to save the results and return
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.SUCCESS
                    await step_result.save()
                    return True
            else:
                target_x = step.by_order[0]
                target_y = step.by_order[1]
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

        if len(visual_matches) == 0 and len(step.by_text) == 0:
            msg = "There are no visual elements matching this step and no further matching patterns has been specified"
            log.debug(msg)
            step_result.end = utc_now
            step_result.status = StepResultStatus.TRAINING_REQUIRED
            step_result.message = msg
            await step_result.save()
            return False

        log.debug("Detecting text elements for step: {0}".format(step.order))
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

                for text_pattern in step.by_text:
                    if re.match(text_pattern, text):
                        text_matches.append(
                            (text, conf, x, y, w, h, page, block, par, line, word)
                        )

        if len(text_matches) == 0:
            msg = "There are no text elements matching this step as well as visual elements matching"
            log.debug(msg)
            step_result.end = utc_now
            step_result.status = StepResultStatus.FAIL
            step_result.message = msg
            await step_result.save()
            return False

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
            # TODO: Now I can perform the step action and go to the next step
            # After performing I proceed to save the results and return
            step_result.end = utc_now
            step_result.status = StepResultStatus.SUCCESS
            step_result.msg = ""
            await step_result.save()
            return True

        if len(text_matches) > 1 and len(step.by_order) == 0:
            msg = "There are too many text elements matching this step ({0}) and no further order matching pattern has been specified".format(
                len(text_matches)
            )
            log.debug(msg)
            step_result.end = utc_now
            step_result.status = StepResultStatus.TRAINING_REQUIRED
            step_result.message = msg
            await step_result.save()
            return False

        if len(text_matches) > 1 and len(step.by_order) > 0:
            if len(step.by_order) == 1:
                ordering = step.by_order[0]
                if len(text_matches) < ordering:
                    msg = "The text elements cannot match the order({0})".format(
                        ordering
                    )
                    log.debug(msg)
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.FAIL
                    step_result.message = msg
                    await step_result.save()
                    return False
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

                    # TODO: Now I can perform the step action and go to the next step
                    # After performing I proceed to save the results and return
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.SUCCESS
                    step_result.msg = ""
                    await step_result.save()
                    return True
            elif len(step.by_order) > 1:
                lines_ups = []
                target_x = step.by_order[0]
                target_y = step.by_order[1]
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
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.FAIL
                    step_result.message = msg
                    await step_result.save()
                    return False

                if len(founds) > 1:
                    msg = "There are too many text elements matching this step ({0}) and no further order matching pattern has been specified".format(
                        len(text_matches)
                    )
                    log.debug(msg)
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.TRAINING_REQUIRED
                    step_result.message = msg
                    await step_result.save()
                    return False

                if len(founds) == 0:
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
                    # TODO: Now I can perform the step action and go to the next step
                    # After performing I proceed to save the results and return
                    step_result.end = utc_now
                    step_result.status = StepResultStatus.SUCCESS
                    step_result.msg = ""
                    await step_result.save()
                    return True


async def get_player_controller(
    request: Request, wsManager: Websocket
) -> PlayerController:
    if not hasattr(request.app.state, "player"):
        request.app.state.player = PlayerController(
            request.app.state.config.player, wsManager
        )
    return request.app.state.player


GetPlayerController = Annotated[PlayerController, Depends(get_player_controller)]
