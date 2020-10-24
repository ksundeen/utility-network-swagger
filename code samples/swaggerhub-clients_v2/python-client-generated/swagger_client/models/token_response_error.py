# coding: utf-8

"""
    Swagger for Utility Network

    Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network](https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.8.1 using OpenAPI Specification (OAC) written in [SwaggerEditor](https://github.com/swagger-api/swagger-editor)   and [SwaggerHub](https://app.swaggerhub.com/) for C# and Typescript-Angular code generation.    # noqa: E501

    OpenAPI spec version: 3.0
    Contact: kim.sundeen@sspinnovations.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TokenResponseError(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'float',
        'message': 'str',
        'details': 'list[str]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, code=None, message=None, details=None):  # noqa: E501
        """TokenResponseError - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._details = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details

    @property
    def code(self):
        """Gets the code of this TokenResponseError.  # noqa: E501


        :return: The code of this TokenResponseError.  # noqa: E501
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TokenResponseError.


        :param code: The code of this TokenResponseError.  # noqa: E501
        :type: float
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this TokenResponseError.  # noqa: E501


        :return: The message of this TokenResponseError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TokenResponseError.


        :param message: The message of this TokenResponseError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """Gets the details of this TokenResponseError.  # noqa: E501


        :return: The details of this TokenResponseError.  # noqa: E501
        :rtype: list[str]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this TokenResponseError.


        :param details: The details of this TokenResponseError.  # noqa: E501
        :type: list[str]
        """

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TokenResponseError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokenResponseError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
