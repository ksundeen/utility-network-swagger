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
 * TokenResponse.h
 *
 * Token reesponse from Portal
 */

#ifndef IO_SWAGGER_CLIENT_MODEL_TokenResponse_H_
#define IO_SWAGGER_CLIENT_MODEL_TokenResponse_H_


#include "../ModelBase.h"

#include "TokenResponse_error.h"
#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// Token reesponse from Portal
/// </summary>
class  TokenResponse
    : public ModelBase
{
public:
    TokenResponse();
    virtual ~TokenResponse();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// TokenResponse members

    /// <summary>
    /// The generated token.
    /// </summary>
    utility::string_t getToken() const;
    bool tokenIsSet() const;
    void unsetToken();
    void setToken(utility::string_t value);
    /// <summary>
    /// The expiration time of the token in milliseconds since Jan. 1, 1970 (UTC).
    /// </summary>
    double getExpires() const;
    bool expiresIsSet() const;
    void unsetExpires();
    void setExpires(double value);
    /// <summary>
    /// True if the token must always pass over ssl.
    /// </summary>
    bool isSsl() const;
    bool sslIsSet() const;
    void unsetSsl();
    void setSsl(bool value);
    /// <summary>
    /// 
    /// </summary>
    std::shared_ptr<TokenResponse_error> getError() const;
    bool errorIsSet() const;
    void unsetError();
    void setError(std::shared_ptr<TokenResponse_error> value);

protected:
    utility::string_t m_Token;
    bool m_TokenIsSet;
    double m_Expires;
    bool m_ExpiresIsSet;
    bool m_Ssl;
    bool m_SslIsSet;
    std::shared_ptr<TokenResponse_error> m_Error;
    bool m_ErrorIsSet;
};

}
}
}
}

#endif /* IO_SWAGGER_CLIENT_MODEL_TokenResponse_H_ */