/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface DetectorSuggestion { 
    _id?: string | null;
    by_label?: string | null;
    by_text?: string | null;
    by_regex?: string | null;
    by_order?: Array<number>;
    event: string;
    confidence: number;
    x: number;
    y: number;
    w: number;
    h: number;
}

