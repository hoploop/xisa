import { RecordEventListRecordId200ResponseInner } from "@api/model/record-event-list-record-id200-response-inner";

export interface Frame {
  record:string,
  count: number,
  event?:RecordEventListRecordId200ResponseInner,
  resolved:boolean,
  milliseconds:number
}
