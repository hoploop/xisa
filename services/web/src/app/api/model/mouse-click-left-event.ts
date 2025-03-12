/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface MouseClickLeftEvent { 
    _id?: string | null;
    type?: MouseClickLeftEventTypeEnum;
    record: string;
    frame: number;
    timestamp?: string;
    position?: Array<any> | null;
}
export enum MouseClickLeftEventTypeEnum {
    MouseClickLeft = 'mouse.click.left'
};



