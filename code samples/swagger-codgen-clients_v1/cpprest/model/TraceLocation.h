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

/*
 * TraceLocation.h
 *
 * 
 */

#ifndef IO_SWAGGER_CLIENT_MODEL_TraceLocation_H_
#define IO_SWAGGER_CLIENT_MODEL_TraceLocation_H_


#include "../ModelBase.h"

#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  TraceLocation
    : public ModelBase
{
public:
    TraceLocation();
    virtual ~TraceLocation();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// TraceLocation members

    /// <summary>
    /// 
    /// </summary>
    utility::string_t getTraceLocationType() const;
    bool traceLocationTypeIsSet() const;
    void unsetTraceLocationType();
    void setTraceLocationType(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getGlobalId() const;
    bool globalIdIsSet() const;
    void unsetGlobalId();
    void setGlobalId(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    double getPercentAlong() const;
    bool percentAlongIsSet() const;
    void unsetPercentAlong();
    void setPercentAlong(double value);

protected:
    utility::string_t m_TraceLocationType;
    bool m_TraceLocationTypeIsSet;
    utility::string_t m_GlobalId;
    bool m_GlobalIdIsSet;
    double m_PercentAlong;
    bool m_PercentAlongIsSet;
};

}
}
}
}

#endif /* IO_SWAGGER_CLIENT_MODEL_TraceLocation_H_ */