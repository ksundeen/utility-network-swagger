/**
 * Swagger for Utility Network
 * Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network]( https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.6.1 using [NSwagStudio](https://github.com/RSuter/NSwag/wiki/NSwagStudio) C# code gen . 
 *
 * OpenAPI spec version: 0.13
 * Contact: 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

import * as models from './models';

export interface FunctionsInnerNetworkAttributeConditions {
    "networkAttributeName"?: string;
    "operator"?: FunctionsInnerNetworkAttributeConditions.OperatorEnum;
    "value"?: string;
    "combineUsingOr"?: boolean;
    "isTypeSpecificValue"?: boolean;
}

export namespace FunctionsInnerNetworkAttributeConditions {
    export enum OperatorEnum {
        Equal = <any> 'equal',
        NotEqual = <any> 'notEqual',
        GreaterThan = <any> 'greaterThan',
        GreaterThanEqual = <any> 'greaterThanEqual',
        LessThan = <any> 'lessThan',
        LessThanEqual = <any> 'lessThanEqual',
        IncludesTheValues = <any> 'includesTheValues',
        DoesNotIncludeTheValues = <any> 'doesNotIncludeTheValues',
        IncludesAny = <any> 'includesAny',
        DoesNotIncludeAny = <any> 'doesNotIncludeAny'
    }
}