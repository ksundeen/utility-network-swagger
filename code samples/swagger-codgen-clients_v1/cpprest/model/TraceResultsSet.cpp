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



#include "TraceResultsSet.h"

namespace io {
namespace swagger {
namespace client {
namespace model {

TraceResultsSet::TraceResultsSet()
{
    m_TraceResultsIsSet = false;
    m_Success = false;
    m_SuccessIsSet = false;
    m_ErrorIsSet = false;
}

TraceResultsSet::~TraceResultsSet()
{
}

void TraceResultsSet::validate()
{
    // TODO: implement validation
}

web::json::value TraceResultsSet::toJson() const
{
    web::json::value val = web::json::value::object();

    if(m_TraceResultsIsSet)
    {
        val[utility::conversions::to_string_t("traceResults")] = ModelBase::toJson(m_TraceResults);
    }
    if(m_SuccessIsSet)
    {
        val[utility::conversions::to_string_t("success")] = ModelBase::toJson(m_Success);
    }
    if(m_ErrorIsSet)
    {
        val[utility::conversions::to_string_t("error")] = ModelBase::toJson(m_Error);
    }

    return val;
}

void TraceResultsSet::fromJson(web::json::value& val)
{
    if(val.has_field(utility::conversions::to_string_t("traceResults")))
    {
        if(!val[utility::conversions::to_string_t("traceResults")].is_null())
        {
            std::shared_ptr<TraceResultsSet_traceResults> newItem(new TraceResultsSet_traceResults());
            newItem->fromJson(val[utility::conversions::to_string_t("traceResults")]);
            setTraceResults( newItem );
        }
    }
    if(val.has_field(utility::conversions::to_string_t("success")))
    {
        setSuccess(ModelBase::boolFromJson(val[utility::conversions::to_string_t("success")]));
    }
    if(val.has_field(utility::conversions::to_string_t("error")))
    {
        if(!val[utility::conversions::to_string_t("error")].is_null())
        {
            std::shared_ptr<TokenResponse_error> newItem(new TokenResponse_error());
            newItem->fromJson(val[utility::conversions::to_string_t("error")]);
            setError( newItem );
        }
    }
}

void TraceResultsSet::toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix) const
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix.substr(namePrefix.size() - 1) != utility::conversions::to_string_t("."))
    {
        namePrefix += utility::conversions::to_string_t(".");
    }

    if(m_TraceResultsIsSet)
    {
        if (m_TraceResults.get())
        {
            m_TraceResults->toMultipart(multipart, utility::conversions::to_string_t("traceResults."));
        }
        
    }
    if(m_SuccessIsSet)
    {
        multipart->add(ModelBase::toHttpContent(namePrefix + utility::conversions::to_string_t("success"), m_Success));
    }
    if(m_ErrorIsSet)
    {
        if (m_Error.get())
        {
            m_Error->toMultipart(multipart, utility::conversions::to_string_t("error."));
        }
        
    }
}

void TraceResultsSet::fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& prefix)
{
    utility::string_t namePrefix = prefix;
    if(namePrefix.size() > 0 && namePrefix.substr(namePrefix.size() - 1) != utility::conversions::to_string_t("."))
    {
        namePrefix += utility::conversions::to_string_t(".");
    }

    if(multipart->hasContent(utility::conversions::to_string_t("traceResults")))
    {
        if(multipart->hasContent(utility::conversions::to_string_t("traceResults")))
        {
            std::shared_ptr<TraceResultsSet_traceResults> newItem(new TraceResultsSet_traceResults());
            newItem->fromMultiPart(multipart, utility::conversions::to_string_t("traceResults."));
            setTraceResults( newItem );
        }
    }
    if(multipart->hasContent(utility::conversions::to_string_t("success")))
    {
        setSuccess(ModelBase::boolFromHttpContent(multipart->getContent(utility::conversions::to_string_t("success"))));
    }
    if(multipart->hasContent(utility::conversions::to_string_t("error")))
    {
        if(multipart->hasContent(utility::conversions::to_string_t("error")))
        {
            std::shared_ptr<TokenResponse_error> newItem(new TokenResponse_error());
            newItem->fromMultiPart(multipart, utility::conversions::to_string_t("error."));
            setError( newItem );
        }
    }
}

std::shared_ptr<TraceResultsSet_traceResults> TraceResultsSet::getTraceResults() const
{
    return m_TraceResults;
}


void TraceResultsSet::setTraceResults(std::shared_ptr<TraceResultsSet_traceResults> value)
{
    m_TraceResults = value;
    m_TraceResultsIsSet = true;
}
bool TraceResultsSet::traceResultsIsSet() const
{
    return m_TraceResultsIsSet;
}

void TraceResultsSet::unsetTraceResults()
{
    m_TraceResultsIsSet = false;
}

bool TraceResultsSet::isSuccess() const
{
    return m_Success;
}


void TraceResultsSet::setSuccess(bool value)
{
    m_Success = value;
    m_SuccessIsSet = true;
}
bool TraceResultsSet::successIsSet() const
{
    return m_SuccessIsSet;
}

void TraceResultsSet::unsetSuccess()
{
    m_SuccessIsSet = false;
}

std::shared_ptr<TokenResponse_error> TraceResultsSet::getError() const
{
    return m_Error;
}


void TraceResultsSet::setError(std::shared_ptr<TokenResponse_error> value)
{
    m_Error = value;
    m_ErrorIsSet = true;
}
bool TraceResultsSet::errorIsSet() const
{
    return m_ErrorIsSet;
}

void TraceResultsSet::unsetError()
{
    m_ErrorIsSet = false;
}

}
}
}
}
