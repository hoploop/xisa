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
import { Project } from '../model/project';
// @ts-ignore
import { ProjectListResponse } from '../model/project-list-response';

// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';
import {
    WorkspaceServiceInterface
} from './workspace.serviceInterface';



@Injectable({
  providedIn: 'root'
})
export class WorkspaceService implements WorkspaceServiceInterface {

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
     * Create Project
     * Performs the creation of a project
     * @param name 
     * @param description 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public workspaceProjectCreate(name: string, description?: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<Project>;
    public workspaceProjectCreate(name: string, description?: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<Project>>;
    public workspaceProjectCreate(name: string, description?: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<Project>>;
    public workspaceProjectCreate(name: string, description?: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (name === null || name === undefined) {
            throw new Error('Required parameter name was null or undefined when calling workspaceProjectCreate.');
        }

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (name !== undefined && name !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>name, 'name');
        }
        if (description !== undefined && description !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>description, 'description');
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

        let localVarPath = `/workspace/project/create`;
        return this.httpClient.request<Project>('post', `${this.configuration.basePath}${localVarPath}`,
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
     * Delete Project
     * Performs the removal of a project
     * @param projectId 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public workspaceProjectDelete(projectId: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<boolean>;
    public workspaceProjectDelete(projectId: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<boolean>>;
    public workspaceProjectDelete(projectId: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<boolean>>;
    public workspaceProjectDelete(projectId: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (projectId === null || projectId === undefined) {
            throw new Error('Required parameter projectId was null or undefined when calling workspaceProjectDelete.');
        }

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (projectId !== undefined && projectId !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>projectId, 'projectId');
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

        let localVarPath = `/workspace/project/delete`;
        return this.httpClient.request<boolean>('delete', `${this.configuration.basePath}${localVarPath}`,
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
     * List Project
     * @param skip 
     * @param limit 
     * @param search 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public workspaceProjectList(skip?: number, limit?: number, search?: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<ProjectListResponse>;
    public workspaceProjectList(skip?: number, limit?: number, search?: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<ProjectListResponse>>;
    public workspaceProjectList(skip?: number, limit?: number, search?: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<ProjectListResponse>>;
    public workspaceProjectList(skip?: number, limit?: number, search?: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (skip !== undefined && skip !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>skip, 'skip');
        }
        if (limit !== undefined && limit !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>limit, 'limit');
        }
        if (search !== undefined && search !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>search, 'search');
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

        let localVarPath = `/workspace/project/list`;
        return this.httpClient.request<ProjectListResponse>('get', `${this.configuration.basePath}${localVarPath}`,
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
     * Load Project
     * @param projectId 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public workspaceProjectLoad(projectId: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<Project>;
    public workspaceProjectLoad(projectId: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<Project>>;
    public workspaceProjectLoad(projectId: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<Project>>;
    public workspaceProjectLoad(projectId: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (projectId === null || projectId === undefined) {
            throw new Error('Required parameter projectId was null or undefined when calling workspaceProjectLoad.');
        }

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (projectId !== undefined && projectId !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>projectId, 'projectId');
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

        let localVarPath = `/workspace/project/load`;
        return this.httpClient.request<Project>('get', `${this.configuration.basePath}${localVarPath}`,
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
     * Update Project
     * Performs the update of a project
     * @param projectId 
     * @param name 
     * @param description 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public workspaceProjectUpdate(projectId: string, name: string, description?: string, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<boolean>;
    public workspaceProjectUpdate(projectId: string, name: string, description?: string, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpResponse<boolean>>;
    public workspaceProjectUpdate(projectId: string, name: string, description?: string, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<HttpEvent<boolean>>;
    public workspaceProjectUpdate(projectId: string, name: string, description?: string, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json', context?: HttpContext, transferCache?: boolean}): Observable<any> {
        if (projectId === null || projectId === undefined) {
            throw new Error('Required parameter projectId was null or undefined when calling workspaceProjectUpdate.');
        }
        if (name === null || name === undefined) {
            throw new Error('Required parameter name was null or undefined when calling workspaceProjectUpdate.');
        }

        let localVarQueryParameters = new HttpParams({encoder: this.encoder});
        if (projectId !== undefined && projectId !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>projectId, 'projectId');
        }
        if (name !== undefined && name !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>name, 'name');
        }
        if (description !== undefined && description !== null) {
          localVarQueryParameters = this.addToHttpParams(localVarQueryParameters,
            <any>description, 'description');
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

        let localVarPath = `/workspace/project/update`;
        return this.httpClient.request<boolean>('put', `${this.configuration.basePath}${localVarPath}`,
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
