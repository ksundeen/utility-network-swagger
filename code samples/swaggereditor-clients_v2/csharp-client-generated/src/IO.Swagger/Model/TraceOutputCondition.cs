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
    /// TraceOutputCondition
    /// </summary>
    [DataContract]
        public partial class TraceOutputCondition :  IEquatable<TraceOutputCondition>, IValidatableObject
    {
        /// <summary>
        /// Defines Type
        /// </summary>
        [JsonConverter(typeof(StringEnumConverter))]
                public enum TypeEnum
        {
            /// <summary>
            /// Enum NetworkAttribute for value: networkAttribute
            /// </summary>
            [EnumMember(Value = "networkAttribute")]
            NetworkAttribute = 1,
            /// <summary>
            /// Enum Category for value: category
            /// </summary>
            [EnumMember(Value = "category")]
            Category = 2        }
        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name="type", EmitDefaultValue=false)]
        public TypeEnum Type { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="TraceOutputCondition" /> class.
        /// </summary>
        /// <param name="name">name (required).</param>
        /// <param name="type">type (required).</param>
        /// <param name="_operator">_operator (required).</param>
        /// <param name="value">value.</param>
        /// <param name="combineUsingOr">combineUsingOr.</param>
        /// <param name="isSpecificValue">isSpecificValue (required).</param>
        public TraceOutputCondition(string name = default(string), TypeEnum type = default(TypeEnum), string _operator = default(string), decimal? value = default(decimal?), bool? combineUsingOr = default(bool?), bool? isSpecificValue = default(bool?))
        {
            // to ensure "name" is required (not null)
            if (name == null)
            {
                throw new InvalidDataException("name is a required property for TraceOutputCondition and cannot be null");
            }
            else
            {
                this.Name = name;
            }
            // to ensure "type" is required (not null)
            if (type == null)
            {
                throw new InvalidDataException("type is a required property for TraceOutputCondition and cannot be null");
            }
            else
            {
                this.Type = type;
            }
            // to ensure "_operator" is required (not null)
            if (_operator == null)
            {
                throw new InvalidDataException("_operator is a required property for TraceOutputCondition and cannot be null");
            }
            else
            {
                this.Operator = _operator;
            }
            // to ensure "isSpecificValue" is required (not null)
            if (isSpecificValue == null)
            {
                throw new InvalidDataException("isSpecificValue is a required property for TraceOutputCondition and cannot be null");
            }
            else
            {
                this.IsSpecificValue = isSpecificValue;
            }
            this.Value = value;
            this.CombineUsingOr = combineUsingOr;
        }
        
        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }


        /// <summary>
        /// Gets or Sets Operator
        /// </summary>
        [DataMember(Name="operator", EmitDefaultValue=false)]
        public string Operator { get; set; }

        /// <summary>
        /// Gets or Sets Value
        /// </summary>
        [DataMember(Name="value", EmitDefaultValue=false)]
        public decimal? Value { get; set; }

        /// <summary>
        /// Gets or Sets CombineUsingOr
        /// </summary>
        [DataMember(Name="combineUsingOr", EmitDefaultValue=false)]
        public bool? CombineUsingOr { get; set; }

        /// <summary>
        /// Gets or Sets IsSpecificValue
        /// </summary>
        [DataMember(Name="isSpecificValue", EmitDefaultValue=false)]
        public bool? IsSpecificValue { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TraceOutputCondition {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Operator: ").Append(Operator).Append("\n");
            sb.Append("  Value: ").Append(Value).Append("\n");
            sb.Append("  CombineUsingOr: ").Append(CombineUsingOr).Append("\n");
            sb.Append("  IsSpecificValue: ").Append(IsSpecificValue).Append("\n");
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
            return this.Equals(input as TraceOutputCondition);
        }

        /// <summary>
        /// Returns true if TraceOutputCondition instances are equal
        /// </summary>
        /// <param name="input">Instance of TraceOutputCondition to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TraceOutputCondition input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                ) && 
                (
                    this.Operator == input.Operator ||
                    (this.Operator != null &&
                    this.Operator.Equals(input.Operator))
                ) && 
                (
                    this.Value == input.Value ||
                    (this.Value != null &&
                    this.Value.Equals(input.Value))
                ) && 
                (
                    this.CombineUsingOr == input.CombineUsingOr ||
                    (this.CombineUsingOr != null &&
                    this.CombineUsingOr.Equals(input.CombineUsingOr))
                ) && 
                (
                    this.IsSpecificValue == input.IsSpecificValue ||
                    (this.IsSpecificValue != null &&
                    this.IsSpecificValue.Equals(input.IsSpecificValue))
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
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.Operator != null)
                    hashCode = hashCode * 59 + this.Operator.GetHashCode();
                if (this.Value != null)
                    hashCode = hashCode * 59 + this.Value.GetHashCode();
                if (this.CombineUsingOr != null)
                    hashCode = hashCode * 59 + this.CombineUsingOr.GetHashCode();
                if (this.IsSpecificValue != null)
                    hashCode = hashCode * 59 + this.IsSpecificValue.GetHashCode();
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
