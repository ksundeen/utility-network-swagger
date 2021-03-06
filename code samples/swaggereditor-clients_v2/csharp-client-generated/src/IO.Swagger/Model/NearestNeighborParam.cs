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
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// NearestNeighborParam
    /// </summary>
    [DataContract]
        public partial class NearestNeighborParam :  IEquatable<NearestNeighborParam>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="NearestNeighborParam" /> class.
        /// </summary>
        /// <param name="count">count.</param>
        /// <param name="costNetworkAttributeName">costNetworkAttributeName (default to &quot;&quot;).</param>
        /// <param name="nearestCategories">nearestCategories (required).</param>
        /// <param name="nearestAssets">nearestAssets (required).</param>
        public NearestNeighborParam(int? count = default(int?), string costNetworkAttributeName = "", List<string> nearestCategories = default(List<string>), List<string> nearestAssets = default(List<string>))
        {
            // to ensure "nearestCategories" is required (not null)
            if (nearestCategories == null)
            {
                throw new InvalidDataException("nearestCategories is a required property for NearestNeighborParam and cannot be null");
            }
            else
            {
                this.NearestCategories = nearestCategories;
            }
            // to ensure "nearestAssets" is required (not null)
            if (nearestAssets == null)
            {
                throw new InvalidDataException("nearestAssets is a required property for NearestNeighborParam and cannot be null");
            }
            else
            {
                this.NearestAssets = nearestAssets;
            }
            this.Count = count;
            // use default value if no "costNetworkAttributeName" provided
            if (costNetworkAttributeName == null)
            {
                this.CostNetworkAttributeName = "";
            }
            else
            {
                this.CostNetworkAttributeName = costNetworkAttributeName;
            }
        }
        
        /// <summary>
        /// Gets or Sets Count
        /// </summary>
        [DataMember(Name="count", EmitDefaultValue=false)]
        public int? Count { get; set; }

        /// <summary>
        /// Gets or Sets CostNetworkAttributeName
        /// </summary>
        [DataMember(Name="costNetworkAttributeName", EmitDefaultValue=false)]
        public string CostNetworkAttributeName { get; set; }

        /// <summary>
        /// Gets or Sets NearestCategories
        /// </summary>
        [DataMember(Name="nearestCategories", EmitDefaultValue=false)]
        public List<string> NearestCategories { get; set; }

        /// <summary>
        /// Gets or Sets NearestAssets
        /// </summary>
        [DataMember(Name="nearestAssets", EmitDefaultValue=false)]
        public List<string> NearestAssets { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class NearestNeighborParam {\n");
            sb.Append("  Count: ").Append(Count).Append("\n");
            sb.Append("  CostNetworkAttributeName: ").Append(CostNetworkAttributeName).Append("\n");
            sb.Append("  NearestCategories: ").Append(NearestCategories).Append("\n");
            sb.Append("  NearestAssets: ").Append(NearestAssets).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as NearestNeighborParam);
        }

        /// <summary>
        /// Returns true if NearestNeighborParam instances are equal
        /// </summary>
        /// <param name="input">Instance of NearestNeighborParam to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(NearestNeighborParam input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Count == input.Count ||
                    (this.Count != null &&
                    this.Count.Equals(input.Count))
                ) && 
                (
                    this.CostNetworkAttributeName == input.CostNetworkAttributeName ||
                    (this.CostNetworkAttributeName != null &&
                    this.CostNetworkAttributeName.Equals(input.CostNetworkAttributeName))
                ) && 
                (
                    this.NearestCategories == input.NearestCategories ||
                    this.NearestCategories != null &&
                    input.NearestCategories != null &&
                    this.NearestCategories.SequenceEqual(input.NearestCategories)
                ) && 
                (
                    this.NearestAssets == input.NearestAssets ||
                    this.NearestAssets != null &&
                    input.NearestAssets != null &&
                    this.NearestAssets.SequenceEqual(input.NearestAssets)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Count != null)
                    hashCode = hashCode * 59 + this.Count.GetHashCode();
                if (this.CostNetworkAttributeName != null)
                    hashCode = hashCode * 59 + this.CostNetworkAttributeName.GetHashCode();
                if (this.NearestCategories != null)
                    hashCode = hashCode * 59 + this.NearestCategories.GetHashCode();
                if (this.NearestAssets != null)
                    hashCode = hashCode * 59 + this.NearestAssets.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
