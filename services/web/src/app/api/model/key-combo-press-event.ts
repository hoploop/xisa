/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface KeyComboPressEvent { 
    _id?: string | null;
    type?: KeyComboPressEventTypeEnum;
    record: string;
    frame: number;
    synthetic?: boolean;
    timestamp?: string;
    keys: Array<string>;
}
export enum KeyComboPressEventTypeEnum {
    KeyComboPress = 'key.combo.press'
};



