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
 * ConditionBarrier.h
 *
 * 
 */

#ifndef IO_SWAGGER_CLIENT_MODEL_ConditionBarrier_H_
#define IO_SWAGGER_CLIENT_MODEL_ConditionBarrier_H_


#include "../ModelBase.h"

#include <cpprest/details/basic_types.h>

namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  ConditionBarrier
    : public ModelBase
{
public:
    ConditionBarrier();
    virtual ~ConditionBarrier();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// ConditionBarrier members

    /// <summary>
    /// 
    /// </summary>
    utility::string_t getNetworkAttributeName() const;
        void setNetworkAttributeName(utility::string_t value);
    /// <summary>
    /// 
    /// </summary>
    utility::string_t getOperator() const;
        void setOperator(utility::string_t value);
    /// <summary>
    /// 0 &#x3D; unknown, 1 &#x3D; open, 2 &#x3D; closed
    /// </summary>
    double getValue() const;
        void setValue(double value);
    /// <summary>
    /// 
    /// </summary>
    bool isCombineUsingOr() const;
        void setCombineUsingOr(bool value);
    /// <summary>
    /// 
    /// </summary>
    bool isIsTypeSpecificValue() const;
        void setIsTypeSpecificValue(bool value);

protected:
    utility::string_t m_NetworkAttributeName;
        utility::string_t m__operator;
        double m_Value;
        bool m_CombineUsingOr;
        bool m_IsTypeSpecificValue;
    };

}
}
}
}

#endif /* IO_SWAGGER_CLIENT_MODEL_ConditionBarrier_H_ */
