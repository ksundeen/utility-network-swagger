/* 
 * Swagger for Utility Network
 *
 * Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network](https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.8.1 using OpenAPI Specification (OAC) written in [SwaggerEditor](https://github.com/swagger-api/swagger-editor)   and [SwaggerHub](https://app.swaggerhub.com/) for C# and Typescript-Angular code generation.  
 *
 * OpenAPI spec version: 3.0
 * Contact: kim.sundeen@sspinnovations.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Collections.Generic;

namespace IO.Swagger.Client
{
    /// <summary>
    /// API Response
    /// </summary>
        public class ApiResponse<T>
    {
        /// <summary>
        /// Gets or sets the status code (HTTP status code)
        /// </summary>
        /// <value>The status code.</value>
        public int StatusCode { get; private set; }

        /// <summary>
        /// Gets or sets the HTTP headers
        /// </summary>
        /// <value>HTTP headers</value>
        public IDictionary<string, string> Headers { get; private set; }

        /// <summary>
        /// Gets or sets the data (parsed HTTP body)
        /// </summary>
        /// <value>The data.</value>
        public T Data { get; private set; }

        /// <summary>
        /// Initializes a new instance of the <see cref="ApiResponse&lt;T&gt;" /> class.
        /// </summary>
        /// <param name="statusCode">HTTP status code.</param>
        /// <param name="headers">HTTP headers.</param>
        /// <param name="data">Data (parsed HTTP body)</param>
        public ApiResponse(int statusCode, IDictionary<string, string> headers, T data)
        {
            this.StatusCode= statusCode;
            this.Headers = headers;
            this.Data = data;
        }

    }

}
