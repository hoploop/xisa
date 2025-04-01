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

import { HTTPValidationError } from '../model/models';
import { TrainImageObject } from '../model/models';
import { TrainImageObjectListResponse } from '../model/models';
import { TrainImageObjectPayload } from '../model/models';
import { TrainImageObjectUpdatePayload } from '../model/models';
import { TrainLesson } from '../model/models';


import { Configuration }                                     from '../configuration';



export interface TrainerServiceInterface {
    defaultHeaders: HttpHeaders;
    configuration: Configuration;

    /**
     * Lesson
     * Checks if a recorder is running
     * @param recordId 
     */
    trainerLesson(recordId: string, extraHttpRequestParams?: any): Observable<TrainLesson>;

    /**
     * Lesson Image Object
     * 
     * @param trainImageObjectPayload 
     */
    trainerLessonImageObject(trainImageObjectPayload: TrainImageObjectPayload, extraHttpRequestParams?: any): Observable<TrainImageObject>;

    /**
     * Lesson Image Object Count By Detector
     * 
     * @param detectorId 
     */
    trainerLessonImageObjectCountByDetector(detectorId: string, extraHttpRequestParams?: any): Observable<number>;

    /**
     * Lesson Image Object List
     * 
     * @param lessonId 
     * @param frame 
     */
    trainerLessonImageObjectList(lessonId: string, frame?: number, extraHttpRequestParams?: any): Observable<TrainImageObjectListResponse>;

    /**
     * Lesson Image Object Remove
     * 
     * @param objectId 
     */
    trainerLessonImageObjectRemove(objectId: string, extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Lesson Image Object Update
     * 
     * @param trainImageObjectUpdatePayload 
     */
    trainerLessonImageObjectUpdate(trainImageObjectUpdatePayload: TrainImageObjectUpdatePayload, extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Lesson Set Detector
     * 
     * @param detectorId 
     * @param lessonId 
     */
    trainerLessonSetDetector(detectorId: string, lessonId: string, extraHttpRequestParams?: any): Observable<TrainLesson>;

}
