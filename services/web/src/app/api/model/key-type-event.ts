/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface KeyTypeEvent { 
    _id?: string | null;
    type?: KeyTypeEventTypeEnum;
    record: string;
    frame: number;
    synthetic?: boolean;
    timestamp?: string;
    position?: Array<any> | null;
    key: string;
}
export enum KeyTypeEventTypeEnum {
    KeyType = 'key.type'
};



