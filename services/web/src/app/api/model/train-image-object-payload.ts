/**
 * API
 *
 * Contact: dp@x-force.example.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface TrainImageObjectPayload { 
    lessonId: string;
    frame: number;
    labels: Array<string>;
    xstart: number;
    xend: number;
    ystart: number;
    yend: number;
    val: boolean;
    test: boolean;
    train: boolean;
}

