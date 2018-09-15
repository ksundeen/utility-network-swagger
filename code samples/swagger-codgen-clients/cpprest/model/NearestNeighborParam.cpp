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



#include "NearestNeighborParam.h"

namespace io {
namespace swagger {
namespace client {
namespace model {

NearestNeighborParam::NearestNeighborParam()
{
    m_Count = 0;
    m_CountIsSet = false;
    m_CostNetworkAttributeName = utility::conversions::to_string_t("");
    m_CostNetworkAttributeNameIsSet = false;
}

NearestNeighborParam::~NearestNeighborParam()
{
}

void NearestNeighborParam::validate()
{
    // TODO: implement validation
}

web::json::value NearestNeighborParam::toJson() const
{
    web::json::value val = web::json::value::object();

    if(m_CountIsSet)
    {
        val[utility::conversions::to_string_t("count")] = ModelBase::toJson(m_Count);
    }
    if(m_CostNetworkAttributeNameIsSet)
    {
        val[utility::conversions::to_string_t("costNetworkAttributeName")] = ModelBase::toJson(m_CostNetworkAttributeName);
    }
    {
        std::vector<web::json::value> jsonArray;
        for( auto& item : m_NearestCategories )
        {
            jsonArray.push_back(ModelBase::toJson(item));
        }
        val[utility::conversions::to_string_t("nearestCategories")] = web::json::value::array(jsonArray);
    }
    {
        std::vector<web::json::value> jsonArray;
        for( auto& item : m_NearestAssets )
        {
            jsonArray.push_back(ModelBase::toJson(item));
        }
        val[utility::conversions::to_string_t("nearestAssets")] = web::json::value::array(jsonArray);
    }

    return val;
}

void NearestNeighborParam::fromJson(web::json::value& val)
{
    if(val.has_field(utility::conversions::to_string_t("count")))
    {
        setCount(ModelBase::int32_tFromJson(val[utility::conversions::to_string_t("count")]));
    }
    if(val.has_field(utility::conversions::to_string_t("costNetworkAttributeName")))
    {
        setCostNetworkAttributeName(ModelBase::stringFromJson(val[utility::conversions::to_string_t("costNetworkAttributeName")]));
    }
    {
        m_NearestCategories.clear();
        std::vector<web::json::value> jsonArray;
        for( auto& item : val[utility::conversions::to_string_t("nearestCategories")].as_array() )
        {
            m_NearestCategories.push_back(ModelBase::stringFromJson(item));
        }
    }
    {
        m_NearestAssets.clear();
        std::vector<web::json::value> jsonArray;
        for( auto& item : val[utility::conversions::to_string_t("nearestAssets")].as_array() )
        {
            m_NearestAssets.push_back(ModelBase::stringFromJson(item));
        }
    }
}

void NearestNeighborParam::toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix) const
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix.substr(namePrefix.size() - 1) != utility::conversions::to_string_t("."))
    {
        namePrefix += utility::conversions::to_string_t(".");
    }

    if(m_CountIsSet)
    {
        multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("count"), m_Count));
    }
    if(m_CostNetworkAttributeNameIsSet)
    {
        multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("costNetworkAttributeName"), m_CostNetworkAttributeName));
        
    }
    {
        std::vector<web::json::value> jsonArray;
        for( auto& item : m_NearestCategories )
        {
            jsonArray.push_back(ModelBase::toJson(item));
        }
        multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("nearestCategories"), web::json::value::array(jsonArray), utility::conversions::to_string_t("application/json")));
            }
    {
        std::vector<web::json::value> jsonArray;
        for( auto& item : m_NearestAssets )
        {
            jsonArray.push_back(ModelBase::toJson(item));
        }
        multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("nearestAssets"), web::json::value::array(jsonArray), utility::conversions::to_string_t("application/json")));
            }
}

void NearestNeighborParam::fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix)
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix.substr(namePrefix.size() - 1) != utility::conversions::to_string_t("."))
    {
        namePrefix += utility::conversions::to_string_t(".");
    }

    if(multipart->hasContent(utility::conversions::to_string_t("count")))
    {
        setCount(ModelBase::int32_tFromHttpContent(multipart->getContent(utility::conversions::to_string_t("count"))));
    }
    if(multipart->hasContent(utility::conversions::to_string_t("costNetworkAttributeName")))
    {
        setCostNetworkAttributeName(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("costNetworkAttributeName"))));
    }
    {
        m_NearestCategories.clear();

        web::json::value jsonArray = web::json::value::parse(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("nearestCategories"))));
        for( auto& item : jsonArray.as_array() )
        {
            m_NearestCategories.push_back(ModelBase::stringFromJson(item));
        }
    }
    {
        m_NearestAssets.clear();

        web::json::value jsonArray = web::json::value::parse(ModelBase::stringFromHttpContent(multipart->getContent(utility::conversions::to_string_t("nearestAssets"))));
        for( auto& item : jsonArray.as_array() )
        {
            m_NearestAssets.push_back(ModelBase::stringFromJson(item));
        }
    }
}

int32_t NearestNeighborParam::getCount() const
{
    return m_Count;
}


void NearestNeighborParam::setCount(int32_t value)
{
    m_Count = value;
    m_CountIsSet = true;
}
bool NearestNeighborParam::countIsSet() const
{
    return m_CountIsSet;
}

void NearestNeighborParam::unsetCount()
{
    m_CountIsSet = false;
}

utility::string_t NearestNeighborParam::getCostNetworkAttributeName() const
{
    return m_CostNetworkAttributeName;
}


void NearestNeighborParam::setCostNetworkAttributeName(utility::string_t value)
{
    m_CostNetworkAttributeName = value;
    m_CostNetworkAttributeNameIsSet = true;
}
bool NearestNeighborParam::costNetworkAttributeNameIsSet() const
{
    return m_CostNetworkAttributeNameIsSet;
}

void NearestNeighborParam::unsetCostNetworkAttributeName()
{
    m_CostNetworkAttributeNameIsSet = false;
}

std::vector<utility::string_t>& NearestNeighborParam::getNearestCategories()
{
    return m_NearestCategories;
}

void NearestNeighborParam::setNearestCategories(std::vector<utility::string_t> value)
{
    m_NearestCategories = value;
    
}
std::vector<utility::string_t>& NearestNeighborParam::getNearestAssets()
{
    return m_NearestAssets;
}

void NearestNeighborParam::setNearestAssets(std::vector<utility::string_t> value)
{
    m_NearestAssets = value;
    
}
}
}
}
}

