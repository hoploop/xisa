import { Action, DetectObject, DetectorSuggestion, DetectText, RecorderEventList200ResponseInner, TrainImageObject, TrainLesson } from "@api/index";

export interface Frame {
  count: number,
  event?:RecorderEventList200ResponseInner,
  action?: Action,
  milliseconds:number,
  suggestions: DetectorSuggestion[],
  train: TrainImageObject[],
  lesson: TrainLesson,
  texts: DetectText[],
  objects: DetectObject[]
}
