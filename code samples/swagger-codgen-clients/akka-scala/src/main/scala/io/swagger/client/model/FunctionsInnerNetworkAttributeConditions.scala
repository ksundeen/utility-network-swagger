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
package io.swagger.client.model

import io.swagger.client.core.ApiModel
import org.joda.time.DateTime
import java.util.UUID

case class FunctionsInnerNetworkAttributeConditions (
  networkAttributeName: Option[String],
  operator: Option[FunctionsInnerNetworkAttributeConditionsEnums.Operator],
  value: Option[String],
  combineUsingOr: Option[Boolean],
  isTypeSpecificValue: Option[Boolean]
) extends ApiModel

object FunctionsInnerNetworkAttributeConditionsEnums {

  type Operator = Operator.Value
  object Operator extends Enumeration {
    val Equal = Value("equal")
    val NotEqual = Value("notEqual")
    val GreaterThan = Value("greaterThan")
    val GreaterThanEqual = Value("greaterThanEqual")
    val LessThan = Value("lessThan")
    val LessThanEqual = Value("lessThanEqual")
    val IncludesTheValues = Value("includesTheValues")
    val DoesNotIncludeTheValues = Value("doesNotIncludeTheValues")
    val IncludesAny = Value("includesAny")
    val DoesNotIncludeAny = Value("doesNotIncludeAny")
  }

}
