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
import { Project } from '../model/models';
import { ProjectListResponse } from '../model/models';


import { Configuration }                                     from '../configuration';



export interface ProjectServiceInterface {
    defaultHeaders: HttpHeaders;
    configuration: Configuration;

    /**
     * Project Create
     * Performs the creation of a project
     * @param name 
     * @param description 
     */
    projectCreate(name: string, description?: string, extraHttpRequestParams?: any): Observable<Project>;

    /**
     * Project Delete
     * Performs the removal of a project
     * @param projectId 
     */
    projectDelete(projectId: string, extraHttpRequestParams?: any): Observable<boolean>;

    /**
     * Project List
     * 
     * @param skip 
     * @param limit 
     * @param search 
     */
    projectList(skip?: number, limit?: number, search?: string, extraHttpRequestParams?: any): Observable<ProjectListResponse>;

    /**
     * Project Load
     * 
     * @param projectId 
     */
    projectLoad(projectId: string, extraHttpRequestParams?: any): Observable<Project>;

    /**
     * Project Update
     * Performs the update of a project
     * @param projectId 
     * @param name 
     * @param description 
     */
    projectUpdate(projectId: string, name: string, description?: string, extraHttpRequestParams?: any): Observable<boolean>;

}
