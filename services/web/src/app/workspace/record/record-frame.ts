import { DetectorSuggestion, TrainImageObject, TrainLesson } from "@api/index";
import { RecordEventListRecordId200ResponseInner } from "@api/model/record-event-list-record-id200-response-inner";

export interface Frame {
  count: number,
  event?:RecordEventListRecordId200ResponseInner,
  resolved:boolean,
  milliseconds:number,
  suggestions: DetectorSuggestion[],
  trainImageObjects: TrainImageObject[],
  lesson: TrainLesson
}
