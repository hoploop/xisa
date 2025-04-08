/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface RecordActionCreatePayload { 
    recordId: string;
    eventId: string;
    byLabel?: string | null;
    byText?: string | null;
    byRegex?: string | null;
    byOrder?: Array<number>;
    byPosition?: Array<number>;
    confidence: number;
    image?: string | null;
}

