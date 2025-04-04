/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { HttpHeaders }                                       from '@angular/common/http';

import { Observable }                                        from 'rxjs';

import { Action } from '../model/models';
import { HTTPValidationError } from '../model/models';
import { Record } from '../model/models';
import { RecordActionCreatePayload } from '../model/models';
import { RecordActionListResponse } from '../model/models';
import { RecordActionUpdatePayload } from '../model/models';
import { RecordListResponse } from '../model/models';
import { RecorderEventList200ResponseInner } from '../model/models';
import { ResponseRecordereventload } from '../model/models';


import { Configuration }                                     from '../configuration';



export interface RecorderServiceInterface {
    defaultHeaders: HttpHeaders;
    configuration: Configuration;

    /**
     * Action Count
     * 
     * @param recordId 
     * @param eventId 
     * @param search 
     */
    recorderActionCount(recordId: string, eventId?: string, search?: string, extraHttpRequestParams?: any): Observable<number>;

    /**
     * Action Create
     * 
     * @param recordActionCreatePayload 
     */
    recorderActionCreate(recordActionCreatePayload: RecordActionCreatePayload, extraHttpRequestParams?: any): Observable<Action>;

    /**
     * Action List
     * 
     * @param recordId 
     * @param eventId 
     * @param skip 
     * @param limit 
     * @param search 
     */
    recorderActionList(recordId: string, eventId?: string, skip?: number, limit?: number, search?: string, extraHttpRequestParams?: any): Observable<RecordActionListResponse>;

    /**
     * Action Load
     * 
     * @param actionId 
     */
    recorderActionLoad(actionId: string, extraHttpRequestParams?: any): Observable<Action>;

    /**
     * Action Load By Event
     * 
     * @param eventId 
     */
    recorderActionLoadByEvent(eventId: string, extraHttpRequestParams?: any): Observable<Action>;

    /**
     * Action Remove
     * 
     * @param actionId 
     */
    recorderActionRemove(actionId: string, extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Action Update
     * 
     * @param recordActionUpdatePayload 
     */
    recorderActionUpdate(recordActionUpdatePayload: RecordActionUpdatePayload, extraHttpRequestParams?: any): Observable<Action>;

    /**
     * Count
     * 
     * @param projectId 
     */
    recorderCount(projectId: string, extraHttpRequestParams?: any): Observable<number>;

    /**
     * Edit
     * 
     * @param recordId 
     * @param name 
     * @param description 
     */
    recorderEdit(recordId: string, name: string, description: string, extraHttpRequestParams?: any): Observable<Record>;

    /**
     * Event Action Exist
     * 
     * @param eventId 
     */
    recorderEventActionExist(eventId: string, extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Event Count
     * Counts how many events in the recording
     * @param recordId 
     */
    recorderEventCount(recordId: string, extraHttpRequestParams?: any): Observable<number>;

    /**
     * Event List
     * List events in the recording
     * @param recordId 
     */
    recorderEventList(recordId: string, extraHttpRequestParams?: any): Observable<Array<RecorderEventList200ResponseInner>>;

    /**
     * Event Load
     * Loads a specific event
     * @param eventId 
     */
    recorderEventLoad(eventId: string, extraHttpRequestParams?: any): Observable<ResponseRecordereventload>;

    /**
     * Frame Count
     * Counts how many frames in the recording
     * @param recordId 
     */
    recorderFrameCount(recordId: string, extraHttpRequestParams?: any): Observable<number>;

    /**
     * Frame Load
     * 
     * @param recordId 
     * @param frame 
     */
    recorderFrameLoad(recordId: string, frame: number, extraHttpRequestParams?: any): Observable<any>;

    /**
     * List
     * 
     * @param projectId 
     * @param skip 
     * @param limit 
     * @param search 
     */
    recorderList(projectId: string, skip?: number, limit?: number, search?: string, extraHttpRequestParams?: any): Observable<RecordListResponse>;

    /**
     * Load
     * 
     * @param recorderId 
     */
    recorderLoad(recorderId: string, extraHttpRequestParams?: any): Observable<Record>;

    /**
     * Remove
     * Performs the removal of a Recording
     * @param recordId 
     */
    recorderRemove(recordId: string, extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Running
     * Checks if a recorder is running
     */
    recorderRunning(extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Size
     * Size in bytes of the recording
     * @param recordId 
     */
    recorderSize(recordId: string, extraHttpRequestParams?: any): Observable<number>;

    /**
     * Start
     * Performs the start of a new Recording
     * @param projectId 
     * @param name 
     * @param description 
     */
    recorderStart(projectId: string, name: string, description?: string, extraHttpRequestParams?: any): Observable<Record>;

    /**
     * Stop
     * Performs the stop of a Recording
     */
    recorderStop(extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Video
     * 
     * @param recordId 
     */
    recorderVideo(recordId: string, extraHttpRequestParams?: any): Observable<any>;

}
