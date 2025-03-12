import { RecordEventListRecordId200ResponseInner } from "@api/index";

export interface Frame {
  record:string,
  count: number,
  event?:RecordEventListRecordId200ResponseInner,
  resolved:boolean
}
