/**
 * Swagger for Utility Network
 * Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network]( https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.6.1 using [NSwagStudio](https://github.com/RSuter/NSwag/wiki/NSwagStudio) C# code gen . 
 *
 * OpenAPI spec version: 0.13
 * Contact: 
 *
 * NOTE: This class is auto generated by the swagger code generator 2.4.0-SNAPSHOT.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */



#include "FunctionBarrier.h"

namespace io {
namespace swagger {
namespace client {
namespace model {

FunctionBarrier::FunctionBarrier()
{
    m_FunctionType = utility::conversions::to_string_t("");
    m_NetworkAttributeName = utility::conversions::to_string_t("");
    m__operator = utility::conversions::to_string_t("");
    m_Value = utility::conversions::to_string_t("");
    m_UseLocalValues = false;
    m_UseLocalValuesIsSet = false;
}

FunctionBarrier::~FunctionBarrier()
{
}

void FunctionBarrier::validate()
{
    // TODO: implement validation
}

web::json::value FunctionBarrier::toJson() const
{
    web::json::value val = web::json::value::object();

    val[utility::conversions::to_string_t("functionType")] = ModelBase::toJson(m_FunctionType);
    val[utility::conversions::to_string_t("networkAttributeName")] = ModelBase::toJson(m_NetworkAttributeName);
    val[utility::conversions::to_string_t("operator")] = ModelBase::toJson(m__operator);
    val[utility::conversions::to_string_t("value")] = ModelBase::toJson(m_Value);
    if(m_UseLocalValuesIsSet)
    {
        val[utility::conversions::to_string_t("useLocalValues")] = ModelBase::toJson(m_UseLocalValues);
    }

    return val;
}

void FunctionBarrier::fromJson(web::json::value& val)
{
    setFunctionType(ModelBase::stringFromJson(val[utility::conversions::to_string_t("functionType")]));
    setNetworkAttributeName(ModelBase::stringFromJson(val[utility::conversions::to_string_t("networkAttributeName")]));
    setOperator(ModelBase::stringFromJson(val[utility::conversions::to_string_t("operator")]));
    setValue(ModelBase::stringFromJson(val[utility::conversions::to_string_t("value")]));
    if(val.has_field(utility::conversions::to_string_t("useLocalValues")))
    {
        setUseLocalValues(ModelBase::boolFromJson(val[utility::conversions::to_string_t("useLocalValues")]));
    }
}

void FunctionBarrier::toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix) const
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix.substr(namePrefix.size() - 1) != utility::conversions::to_string_t("."))
    {
        namePrefix += utility::conversions::to_string_t(".");
    }

    multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("functionType"), m_FunctionType));
    multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("networkAttributeName"), m_NetworkAttributeName));
    multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("operator"), m__operator));
    multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("value"), m_Value));
    if(m_UseLocalValuesIsSet)
    {
        multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("useLocalValues"), m_UseLocalValues));
    }
}

void FunctionBarrier::fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix)
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix.substr(namePrefix.size() - 1) != utility::conversions::to_string_t("."))
    {
        namePrefix += utility::conversions::to_string_t(".");
    }

    setFunctionType(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("functionType"))));
    setNetworkAttributeName(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("networkAttributeName"))));
    setOperator(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("operator"))));
    setValue(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("value"))));
    if(multipart->hasContent(utility::conversions::to_string_t("useLocalValues")))
    {
        setUseLocalValues(ModelBase::boolFromHttpContent(multipart->getContent(utility::conversions::to_string_t("useLocalValues"))));
    }
}

utility::string_t FunctionBarrier::getFunctionType() const
{
    return m_FunctionType;
}


void FunctionBarrier::setFunctionType(utility::string_t value)
{
    m_FunctionType = value;
    
}
utility::string_t FunctionBarrier::getNetworkAttributeName() const
{
    return m_NetworkAttributeName;
}


void FunctionBarrier::setNetworkAttributeName(utility::string_t value)
{
    m_NetworkAttributeName = value;
    
}
utility::string_t FunctionBarrier::getOperator() const
{
    return m__operator;
}


void FunctionBarrier::setOperator(utility::string_t value)
{
    m__operator = value;
    
}
utility::string_t FunctionBarrier::getValue() const
{
    return m_Value;
}


void FunctionBarrier::setValue(utility::string_t value)
{
    m_Value = value;
    
}
bool FunctionBarrier::isUseLocalValues() const
{
    return m_UseLocalValues;
}


void FunctionBarrier::setUseLocalValues(bool value)
{
    m_UseLocalValues = value;
    m_UseLocalValuesIsSet = true;
}
bool FunctionBarrier::useLocalValuesIsSet() const
{
    return m_UseLocalValuesIsSet;
}

void FunctionBarrier::unsetUseLocalValues()
{
    m_UseLocalValuesIsSet = false;
}

}
}
}
}

