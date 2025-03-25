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


import { Configuration }                                     from '../configuration';



export interface TrainServiceInterface {
    defaultHeaders: HttpHeaders;
    configuration: Configuration;

    /**
     * Get Image
     * Retrieve image from MongoDB GridFS
     * @param fileId 
     */
    imageDownload(fileId: string, extraHttpRequestParams?: any): Observable<string>;

    /**
     * Upload File
     * 
     * @param file 
     */
    imageUpload(file: Blob, extraHttpRequestParams?: any): Observable<any>;

}
