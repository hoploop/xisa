/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface TrainImageObject { 
    _id?: string | null;
    record: string;
    detector: string;
    frame: number;
    labels?: Array<string>;
    xstart: number;
    xend: number;
    ystart: number;
    yend: number;
    test?: boolean;
    train?: boolean;
    val?: boolean;
    created?: string;
    updated?: string;
    archived?: boolean;
}

