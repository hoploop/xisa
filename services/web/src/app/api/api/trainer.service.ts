/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
/* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent, HttpParameterCodec, HttpContext 
        }       from '@angular/common/http';
import { CustomHttpParameterCodec }                          from '../encoder';
import { Observable }                                        from 'rxjs';

// @ts-ignore
import { HTTPValidationError } from '../model/http-validation-error';
// @ts-ignore
import { TrainImageObject } from '../model/train-image-object';
// @ts-ignore
import { TrainImageObjectListResponse } from '../model/train-image-object-list-response';
// @ts-ignore
import { TrainImageObjectPayload } from '../model/train-image-object-payload';
// @ts-ignore
import { TrainImageObjectUpdatePayload } from '../model/train-image-object-update-payload';
// @ts-ignore
import { TrainLesson } from '../model/train-lesson';

// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';
import {
    TrainerServiceInterface
} from './trainer.serviceInterface';



@Injectable({
  providedIn: 'root'
})
export class TrainerService implements TrainerServiceInterface {

    protected basePath = 'http://localhost';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();
    public encoder: HttpParameterCodec;

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string|string[], @Optional() configuration: Configuration) {
        if (configuration) {
            this.configuration = configuration;
        }
        if (typeof this.configuration.basePath !== 'string') {
            const firstBasePath = Array.isArray(basePath) ? basePath[0] : undefined;
            if (firstBasePath != undefined) {
                basePath = firstBasePath;
            }

            if (typeof basePath !== 'string') {
                basePath = this.basePath;
            }
            this.configuration.basePath = basePath;
        }
        this.encoder = this.configuration.encoder || new CustomHttpParameterCodec();
    }


    // @ts-ignore
    private addToHttpParams(httpParams: HttpParams, value: any, key?: string): HttpParams {
        if (typeof value === "object" && value instanceof Date === false) {
            httpParams = this.addToHttpParamsRecursive(httpParams, value);
        } else {
            httpParams = this.addToHttpParamsRecursive(httpParams, value, key);
        }
        return httpParams;
    }

    private addToHttpParamsRecursive(httpParams: HttpParams, value?: any, key?: string): HttpParams {
        if (value == null) {
            return httpParams;
        }

        if (typeof value === "object") {
            if (Array.isArray(value)) {
                (value as any[]).forEach( elem => httpParams = this.addToHttpParamsRecursive(httpParams, elem, key));
            } else if (value instanceof Date) {
                if (key != null) {
                    httpParams = httpParams.append(key, (value as Date).toISOString().substring(0, 10));
                } else {
                   throw Error("key may not be null if value is Date");
                }
            } else {
                Object.keys(value).forEach( k => httpParams = this.addToHttpParamsRecursive(
                    httpParams, value[k], key != null ? `${key}.${k}` : k));
            }
        } else if (key != null) {
            httpParams = httpParams.append(key, value);
        } else {
            throw Error("key may not be null if value is not object or array");
        }
        return httpParams;
    }

    /**
     * Lesson
     * Checks if a recorder is running
     * @param recordId 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public trainerLesson(recordId: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<TrainLesson>;
    public trainerLesson(recordId: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<TrainLesson>>;
    public trainerLesson(recordId: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<TrainLesson>>;
    public trainerLesson(recordId: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (recordId === null || recordId === undefined) {
            throw new Error('Required parameter recordId was null or undefined when calling trainerLesson.');
        }

        let localVarHeaders = this.defaultHeaders;

        let localVarCredential: string | undefined;
        // authentication (OAuth2PasswordBearer) required
        localVarCredential = this.configuration.lookupCredential('OAuth2PasswordBearer');
        if (localVarCredential) {
            localVarHeaders = localVarHeaders.set('Authorization', 'Bearer ' + localVarCredential);
        }

        let localVarHttpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (localVarHttpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            localVarHttpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (localVarHttpHeaderAcceptSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Accept', localVarHttpHeaderAcceptSelected);
        }

        let localVarHttpContext: HttpContext | undefined = options && options.context;
        if (localVarHttpContext === undefined) {
            localVarHttpContext = new HttpContext();
        }

        let localVarTransferCache: boolean | undefined = options && options.transferCache;
        if (localVarTransferCache === undefined) {
            localVarTransferCache = true;
        }


        let responseType_: 'text' | 'json' | 'blob' = 'json';
        if (localVarHttpHeaderAcceptSelected) {
            if (localVarHttpHeaderAcceptSelected.startsWith('text')) {
                responseType_ = 'text';
            } else if (this.configuration.isJsonMime(localVarHttpHeaderAcceptSelected)) {
                responseType_ = 'json';
            } else {
                responseType_ = 'blob';
            }
        }

        let localVarPath = `/trainer/lesson/${this.configuration.encodeParam({name: "recordId", value: recordId, in: "path", style: "simple", explode: false, dataType: "string", dataFormat: undefined})}`;
        return this.httpClient.request<TrainLesson>('get', `${this.configuration.basePath}${localVarPath}`,
            {
                context: localVarHttpContext,
                responseType: <any>responseType_,
                withCredentials: this.configuration.withCredentials,
                headers: localVarHeaders,
                observe: observe,
                transferCache: localVarTransferCache,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Lesson Image Object
     * @param trainImageObjectPayload 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public trainerLessonImageObject(trainImageObjectPayload: TrainImageObjectPayload, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<TrainImageObject>;
    public trainerLessonImageObject(trainImageObjectPayload: TrainImageObjectPayload, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<TrainImageObject>>;
    public trainerLessonImageObject(trainImageObjectPayload: TrainImageObjectPayload, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<TrainImageObject>>;
    public trainerLessonImageObject(trainImageObjectPayload: TrainImageObjectPayload, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (trainImageObjectPayload === null || trainImageObjectPayload === undefined) {
            throw new Error('Required parameter trainImageObjectPayload was null or undefined when calling trainerLessonImageObject.');
        }

        let localVarHeaders = this.defaultHeaders;

        let localVarCredential: string | undefined;
        // authentication (OAuth2PasswordBearer) required
        localVarCredential = this.configuration.lookupCredential('OAuth2PasswordBearer');
        if (localVarCredential) {
            localVarHeaders = localVarHeaders.set('Authorization', 'Bearer ' + localVarCredential);
        }

        let localVarHttpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (localVarHttpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            localVarHttpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (localVarHttpHeaderAcceptSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Accept', localVarHttpHeaderAcceptSelected);
        }

        let localVarHttpContext: HttpContext | undefined = options && options.context;
        if (localVarHttpContext === undefined) {
            localVarHttpContext = new HttpContext();
        }

        let localVarTransferCache: boolean | undefined = options && options.transferCache;
        if (localVarTransferCache === undefined) {
            localVarTransferCache = true;
        }


        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Content-Type', httpContentTypeSelected);
        }

        let responseType_: 'text' | 'json' | 'blob' = 'json';
        if (localVarHttpHeaderAcceptSelected) {
            if (localVarHttpHeaderAcceptSelected.startsWith('text')) {
                responseType_ = 'text';
            } else if (this.configuration.isJsonMime(localVarHttpHeaderAcceptSelected)) {
                responseType_ = 'json';
            } else {
                responseType_ = 'blob';
            }
        }

        let localVarPath = `/trainer/lesson/image/object`;
        return this.httpClient.request<TrainImageObject>('post', `${this.configuration.basePath}${localVarPath}`,
            {
                context: localVarHttpContext,
                body: trainImageObjectPayload,
                responseType: <any>responseType_,
                withCredentials: this.configuration.withCredentials,
                headers: localVarHeaders,
                observe: observe,
                transferCache: localVarTransferCache,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Lesson Image Object List
     * @param lessonId 
     * @param frame 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public trainerLessonImageObjectList(lessonId: string, frame?: number, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<TrainImageObjectListResponse>;
    public trainerLessonImageObjectList(lessonId: string, frame?: number, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<TrainImageObjectListResponse>>;
    public trainerLessonImageObjectList(lessonId: string, frame?: number, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<TrainImageObjectListResponse>>;
    public trainerLessonImageObjectList(lessonId: string, frame?: number, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (lessonId === null || lessonId === undefined) {
            throw new Error('Required parameter lessonId was null or undefined when calling trainerLessonImageObjectList.');
        }

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (frame !== undefined && frame !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>frame, 'frame');
        }

        let localVarHeaders = this.defaultHeaders;

        let localVarCredential: string | undefined;
        // authentication (OAuth2PasswordBearer) required
        localVarCredential = this.configuration.lookupCredential('OAuth2PasswordBearer');
        if (localVarCredential) {
            localVarHeaders = localVarHeaders.set('Authorization', 'Bearer ' + localVarCredential);
        }

        let localVarHttpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (localVarHttpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            localVarHttpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (localVarHttpHeaderAcceptSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Accept', localVarHttpHeaderAcceptSelected);
        }

        let localVarHttpContext: HttpContext | undefined = options && options.context;
        if (localVarHttpContext === undefined) {
            localVarHttpContext = new HttpContext();
        }

        let localVarTransferCache: boolean | undefined = options && options.transferCache;
        if (localVarTransferCache === undefined) {
            localVarTransferCache = true;
        }


        let responseType_: 'text' | 'json' | 'blob' = 'json';
        if (localVarHttpHeaderAcceptSelected) {
            if (localVarHttpHeaderAcceptSelected.startsWith('text')) {
                responseType_ = 'text';
            } else if (this.configuration.isJsonMime(localVarHttpHeaderAcceptSelected)) {
                responseType_ = 'json';
            } else {
                responseType_ = 'blob';
            }
        }

        let localVarPath = `/trainer/lesson/image/object/list/${this.configuration.encodeParam({name: "lessonId", value: lessonId, in: "path", style: "simple", explode: false, dataType: "string", dataFormat: undefined})}`;
        return this.httpClient.request<TrainImageObjectListResponse>('get', `${this.configuration.basePath}${localVarPath}`,
            {
                context: localVarHttpContext,
                params: localVarQueryParameters,
                responseType: <any>responseType_,
                withCredentials: this.configuration.withCredentials,
                headers: localVarHeaders,
                observe: observe,
                transferCache: localVarTransferCache,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Lesson Image Object Remove
     * @param objectId 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public trainerLessonImageObjectRemove(objectId: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<boolean>;
    public trainerLessonImageObjectRemove(objectId: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<boolean>>;
    public trainerLessonImageObjectRemove(objectId: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<boolean>>;
    public trainerLessonImageObjectRemove(objectId: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (objectId === null || objectId === undefined) {
            throw new Error('Required parameter objectId was null or undefined when calling trainerLessonImageObjectRemove.');
        }

        let localVarHeaders = this.defaultHeaders;

        let localVarCredential: string | undefined;
        // authentication (OAuth2PasswordBearer) required
        localVarCredential = this.configuration.lookupCredential('OAuth2PasswordBearer');
        if (localVarCredential) {
            localVarHeaders = localVarHeaders.set('Authorization', 'Bearer ' + localVarCredential);
        }

        let localVarHttpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (localVarHttpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            localVarHttpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (localVarHttpHeaderAcceptSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Accept', localVarHttpHeaderAcceptSelected);
        }

        let localVarHttpContext: HttpContext | undefined = options && options.context;
        if (localVarHttpContext === undefined) {
            localVarHttpContext = new HttpContext();
        }

        let localVarTransferCache: boolean | undefined = options && options.transferCache;
        if (localVarTransferCache === undefined) {
            localVarTransferCache = true;
        }


        let responseType_: 'text' | 'json' | 'blob' = 'json';
        if (localVarHttpHeaderAcceptSelected) {
            if (localVarHttpHeaderAcceptSelected.startsWith('text')) {
                responseType_ = 'text';
            } else if (this.configuration.isJsonMime(localVarHttpHeaderAcceptSelected)) {
                responseType_ = 'json';
            } else {
                responseType_ = 'blob';
            }
        }

        let localVarPath = `/trainer/lesson/image/object/remove/${this.configuration.encodeParam({name: "objectId", value: objectId, in: "path", style: "simple", explode: false, dataType: "string", dataFormat: undefined})}`;
        return this.httpClient.request<boolean>('delete', `${this.configuration.basePath}${localVarPath}`,
            {
                context: localVarHttpContext,
                responseType: <any>responseType_,
                withCredentials: this.configuration.withCredentials,
                headers: localVarHeaders,
                observe: observe,
                transferCache: localVarTransferCache,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Lesson Image Object Update
     * @param trainImageObjectUpdatePayload 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public trainerLessonImageObjectUpdate(trainImageObjectUpdatePayload: TrainImageObjectUpdatePayload, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<boolean>;
    public trainerLessonImageObjectUpdate(trainImageObjectUpdatePayload: TrainImageObjectUpdatePayload, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<boolean>>;
    public trainerLessonImageObjectUpdate(trainImageObjectUpdatePayload: TrainImageObjectUpdatePayload, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<boolean>>;
    public trainerLessonImageObjectUpdate(trainImageObjectUpdatePayload: TrainImageObjectUpdatePayload, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (trainImageObjectUpdatePayload === null || trainImageObjectUpdatePayload === undefined) {
            throw new Error('Required parameter trainImageObjectUpdatePayload was null or undefined when calling trainerLessonImageObjectUpdate.');
        }

        let localVarHeaders = this.defaultHeaders;

        let localVarCredential: string | undefined;
        // authentication (OAuth2PasswordBearer) required
        localVarCredential = this.configuration.lookupCredential('OAuth2PasswordBearer');
        if (localVarCredential) {
            localVarHeaders = localVarHeaders.set('Authorization', 'Bearer ' + localVarCredential);
        }

        let localVarHttpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (localVarHttpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            localVarHttpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (localVarHttpHeaderAcceptSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Accept', localVarHttpHeaderAcceptSelected);
        }

        let localVarHttpContext: HttpContext | undefined = options && options.context;
        if (localVarHttpContext === undefined) {
            localVarHttpContext = new HttpContext();
        }

        let localVarTransferCache: boolean | undefined = options && options.transferCache;
        if (localVarTransferCache === undefined) {
            localVarTransferCache = true;
        }


        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Content-Type', httpContentTypeSelected);
        }

        let responseType_: 'text' | 'json' | 'blob' = 'json';
        if (localVarHttpHeaderAcceptSelected) {
            if (localVarHttpHeaderAcceptSelected.startsWith('text')) {
                responseType_ = 'text';
            } else if (this.configuration.isJsonMime(localVarHttpHeaderAcceptSelected)) {
                responseType_ = 'json';
            } else {
                responseType_ = 'blob';
            }
        }

        let localVarPath = `/trainer/lesson/image/object/update`;
        return this.httpClient.request<boolean>('put', `${this.configuration.basePath}${localVarPath}`,
            {
                context: localVarHttpContext,
                body: trainImageObjectUpdatePayload,
                responseType: <any>responseType_,
                withCredentials: this.configuration.withCredentials,
                headers: localVarHeaders,
                observe: observe,
                transferCache: localVarTransferCache,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Lesson Set Detector
     * @param detectorId 
     * @param lessonId 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public trainerLessonSetDetector(detectorId: string, lessonId: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<TrainLesson>;
    public trainerLessonSetDetector(detectorId: string, lessonId: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<TrainLesson>>;
    public trainerLessonSetDetector(detectorId: string, lessonId: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<TrainLesson>>;
    public trainerLessonSetDetector(detectorId: string, lessonId: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (detectorId === null || detectorId === undefined) {
            throw new Error('Required parameter detectorId was null or undefined when calling trainerLessonSetDetector.');
        }
        if (lessonId === null || lessonId === undefined) {
            throw new Error('Required parameter lessonId was null or undefined when calling trainerLessonSetDetector.');
        }

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (detectorId !== undefined && detectorId !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>detectorId, 'detectorId');
        }
        if (lessonId !== undefined && lessonId !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>lessonId, 'lessonId');
        }

        let localVarHeaders = this.defaultHeaders;

        let localVarCredential: string | undefined;
        // authentication (OAuth2PasswordBearer) required
        localVarCredential = this.configuration.lookupCredential('OAuth2PasswordBearer');
        if (localVarCredential) {
            localVarHeaders = localVarHeaders.set('Authorization', 'Bearer ' + localVarCredential);
        }

        let localVarHttpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (localVarHttpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            localVarHttpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (localVarHttpHeaderAcceptSelected !== undefined) {
            localVarHeaders = localVarHeaders.set('Accept', localVarHttpHeaderAcceptSelected);
        }

        let localVarHttpContext: HttpContext | undefined = options && options.context;
        if (localVarHttpContext === undefined) {
            localVarHttpContext = new HttpContext();
        }

        let localVarTransferCache: boolean | undefined = options && options.transferCache;
        if (localVarTransferCache === undefined) {
            localVarTransferCache = true;
        }


        let responseType_: 'text' | 'json' | 'blob' = 'json';
        if (localVarHttpHeaderAcceptSelected) {
            if (localVarHttpHeaderAcceptSelected.startsWith('text')) {
                responseType_ = 'text';
            } else if (this.configuration.isJsonMime(localVarHttpHeaderAcceptSelected)) {
                responseType_ = 'json';
            } else {
                responseType_ = 'blob';
            }
        }

        let localVarPath = `/trainer/lesson/detector`;
        return this.httpClient.request<TrainLesson>('post', `${this.configuration.basePath}${localVarPath}`,
            {
                context: localVarHttpContext,
                params: localVarQueryParameters,
                responseType: <any>responseType_,
                withCredentials: this.configuration.withCredentials,
                headers: localVarHeaders,
                observe: observe,
                transferCache: localVarTransferCache,
                reportProgress: reportProgress
            }
        );
    }

}
