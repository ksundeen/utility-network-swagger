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
 * TokenRequest.h
 *
 * 
 */

#ifndef IO_SWAGGER_CLIENT_MODEL_TokenRequest_H_
#define IO_SWAGGER_CLIENT_MODEL_TokenRequest_H_


#include "../ModelBase.h"

#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  TokenRequest
    : public ModelBase
{
public:
    TokenRequest();
    virtual ~TokenRequest();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// TokenRequest members

    /// <summary>
    /// 
    /// </summary>
    utility::string_t getUsername() const;
        void setUsername(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getPassword() const;
        void setPassword(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getIp() const;
    bool ipIsSet() const;
    void unsetIp();
    void setIp(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getReferer() const;
    bool refererIsSet() const;
    void unsetReferer();
    void setReferer(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    double getExpiration() const;
        void setExpiration(double value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getF() const;
        void setF(utility::string_t value);

protected:
    utility::string_t m_Username;
        utility::string_t m_Password;
        utility::string_t m_Ip;
    bool m_IpIsSet;
    utility::string_t m_Referer;
    bool m_RefererIsSet;
    double m_Expiration;
        utility::string_t m_f;
    };

}
}
}
}

#endif /* IO_SWAGGER_CLIENT_MODEL_TokenRequest_H_ */
