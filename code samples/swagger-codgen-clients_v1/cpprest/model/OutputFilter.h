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
 * OutputFilter.h
 *
 * 
 */

#ifndef IO_SWAGGER_CLIENT_MODEL_OutputFilter_H_
#define IO_SWAGGER_CLIENT_MODEL_OutputFilter_H_


#include "../ModelBase.h"


namespace io {
namespace swagger {
namespace client {
namespace model {

/// <summary>
/// 
/// </summary>
class  OutputFilter
    : public ModelBase
{
public:
    OutputFilter();
    virtual ~OutputFilter();

    /////////////////////////////////////////////
    /// ModelBase overrides

    void validate() override;

    web::json::value toJson() const override;
    void fromJson(web::json::value& json) override;

    void toMultipart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) const override;
    void fromMultiPart(std::shared_ptr<MultipartFormData> multipart, const utility::string_t& namePrefix) override;

    /////////////////////////////////////////////
    /// OutputFilter members

    /// <summary>
    /// 
    /// </summary>
    double getSourceId() const;
        void setSourceId(double value);
    /// <summary>
    /// 
    /// </summary>
    double getAssetGroup() const;
        void setAssetGroup(double value);
    /// <summary>
    /// 
    /// </summary>
    double getAssetType() const;
        void setAssetType(double value);

protected:
    double m_SourceId;
        double m_AssetGroup;
        double m_AssetType;
    };

}
}
}
}

#endif /* IO_SWAGGER_CLIENT_MODEL_OutputFilter_H_ */
