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



export interface OperatorServiceInterface {
    defaultHeaders: HttpHeaders;
    configuration: Configuration;

    /**
     * Ask
     * 
     * @param message 
     */
    operatorAsk(message: string, extraHttpRequestParams?: any): Observable<string>;

}
