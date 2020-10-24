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
    /// Feature
    /// </summary>
    [DataContract]
        public partial class Feature :  IEquatable<Feature>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Feature" /> class.
        /// </summary>
        /// <param name="networkSourceId">networkSourceId.</param>
        /// <param name="globalId">guid.</param>
        /// <param name="objectId">objectId.</param>
        /// <param name="terminalId">terminalId.</param>
        /// <param name="networkAttributes">networkAttributes.</param>
        /// <param name="assetGroup">assetGroup.</param>
        /// <param name="assetType">assetType.</param>
        public Feature(string networkSourceId = default(string), string globalId = default(string), decimal? objectId = default(decimal?), decimal? terminalId = default(decimal?), List<decimal?> networkAttributes = default(List<decimal?>), decimal? assetGroup = default(decimal?), decimal? assetType = default(decimal?))
        {
            this.NetworkSourceId = networkSourceId;
            this.GlobalId = globalId;
            this.ObjectId = objectId;
            this.TerminalId = terminalId;
            this.NetworkAttributes = networkAttributes;
            this.AssetGroup = assetGroup;
            this.AssetType = assetType;
        }
        
        /// <summary>
        /// networkSourceId
        /// </summary>
        /// <value>networkSourceId</value>
        [DataMember(Name="networkSourceId", EmitDefaultValue=false)]
        public string NetworkSourceId { get; set; }

        /// <summary>
        /// guid
        /// </summary>
        /// <value>guid</value>
        [DataMember(Name="globalId", EmitDefaultValue=false)]
        public string GlobalId { get; set; }

        /// <summary>
        /// objectId
        /// </summary>
        /// <value>objectId</value>
        [DataMember(Name="objectId", EmitDefaultValue=false)]
        public decimal? ObjectId { get; set; }

        /// <summary>
        /// terminalId
        /// </summary>
        /// <value>terminalId</value>
        [DataMember(Name="terminalId", EmitDefaultValue=false)]
        public decimal? TerminalId { get; set; }

        /// <summary>
        /// Gets or Sets NetworkAttributes
        /// </summary>
        [DataMember(Name="networkAttributes", EmitDefaultValue=false)]
        public List<decimal?> NetworkAttributes { get; set; }

        /// <summary>
        /// assetGroup
        /// </summary>
        /// <value>assetGroup</value>
        [DataMember(Name="assetGroup", EmitDefaultValue=false)]
        public decimal? AssetGroup { get; set; }

        /// <summary>
        /// assetType
        /// </summary>
        /// <value>assetType</value>
        [DataMember(Name="assetType", EmitDefaultValue=false)]
        public decimal? AssetType { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Feature {\n");
            sb.Append("  NetworkSourceId: ").Append(NetworkSourceId).Append("\n");
            sb.Append("  GlobalId: ").Append(GlobalId).Append("\n");
            sb.Append("  ObjectId: ").Append(ObjectId).Append("\n");
            sb.Append("  TerminalId: ").Append(TerminalId).Append("\n");
            sb.Append("  NetworkAttributes: ").Append(NetworkAttributes).Append("\n");
            sb.Append("  AssetGroup: ").Append(AssetGroup).Append("\n");
            sb.Append("  AssetType: ").Append(AssetType).Append("\n");
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
            return this.Equals(input as Feature);
        }

        /// <summary>
        /// Returns true if Feature instances are equal
        /// </summary>
        /// <param name="input">Instance of Feature to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Feature input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.NetworkSourceId == input.NetworkSourceId ||
                    (this.NetworkSourceId != null &&
                    this.NetworkSourceId.Equals(input.NetworkSourceId))
                ) && 
                (
                    this.GlobalId == input.GlobalId ||
                    (this.GlobalId != null &&
                    this.GlobalId.Equals(input.GlobalId))
                ) && 
                (
                    this.ObjectId == input.ObjectId ||
                    (this.ObjectId != null &&
                    this.ObjectId.Equals(input.ObjectId))
                ) && 
                (
                    this.TerminalId == input.TerminalId ||
                    (this.TerminalId != null &&
                    this.TerminalId.Equals(input.TerminalId))
                ) && 
                (
                    this.NetworkAttributes == input.NetworkAttributes ||
                    this.NetworkAttributes != null &&
                    input.NetworkAttributes != null &&
                    this.NetworkAttributes.SequenceEqual(input.NetworkAttributes)
                ) && 
                (
                    this.AssetGroup == input.AssetGroup ||
                    (this.AssetGroup != null &&
                    this.AssetGroup.Equals(input.AssetGroup))
                ) && 
                (
                    this.AssetType == input.AssetType ||
                    (this.AssetType != null &&
                    this.AssetType.Equals(input.AssetType))
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
                if (this.NetworkSourceId != null)
                    hashCode = hashCode * 59 + this.NetworkSourceId.GetHashCode();
                if (this.GlobalId != null)
                    hashCode = hashCode * 59 + this.GlobalId.GetHashCode();
                if (this.ObjectId != null)
                    hashCode = hashCode * 59 + this.ObjectId.GetHashCode();
                if (this.TerminalId != null)
                    hashCode = hashCode * 59 + this.TerminalId.GetHashCode();
                if (this.NetworkAttributes != null)
                    hashCode = hashCode * 59 + this.NetworkAttributes.GetHashCode();
                if (this.AssetGroup != null)
                    hashCode = hashCode * 59 + this.AssetGroup.GetHashCode();
                if (this.AssetType != null)
                    hashCode = hashCode * 59 + this.AssetType.GetHashCode();
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