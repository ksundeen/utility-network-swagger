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
 * UpdateIsConnectedResponse.h
 *
 * 
 */

#ifndef IO_SWAGGER_CLIENT_MODEL_UpdateIsConnectedResponse_H_
#define IO_SWAGGER_CLIENT_MODEL_UpdateIsConnectedResponse_H_


#include "../ModelBase.h"

#include "TokenResponse_error.h"
#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  UpdateIsConnectedResponse
    : public ModelBase
{
public:
    UpdateIsConnectedResponse();
    virtual ~UpdateIsConnectedResponse();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// UpdateIsConnectedResponse members

    /// <summary>
    /// 
    /// </summary>
    double getMoment() const;
    bool momentIsSet() const;
    void unsetMoment();
    void setMoment(double value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getSuccess() const;
    bool successIsSet() const;
    void unsetSuccess();
    void setSuccess(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    std::shared_ptr<TokenResponse_error> getError() const;
    bool errorIsSet() const;
    void unsetError();
    void setError(std::shared_ptr<TokenResponse_error> value);

protected:
    double m_Moment;
    bool m_MomentIsSet;
    utility::string_t m_Success;
    bool m_SuccessIsSet;
    std::shared_ptr<TokenResponse_error> m_Error;
    bool m_ErrorIsSet;
};

}
}
}
}

#endif /* IO_SWAGGER_CLIENT_MODEL_UpdateIsConnectedResponse_H_ */
