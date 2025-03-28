import { DetectObject, DetectorSuggestion, DetectText, TrainImageObject, TrainLesson } from "@api/index";
import { RecordEventListRecordId200ResponseInner } from "@api/model/record-event-list-record-id200-response-inner";

export interface Frame {
  count: number,
  event?:RecordEventListRecordId200ResponseInner,
  resolved:boolean,
  milliseconds:number,
  suggestions: DetectorSuggestion[],
  train: TrainImageObject[],
  lesson: TrainLesson,
  texts: DetectText[],
  objects: DetectObject[]
}
