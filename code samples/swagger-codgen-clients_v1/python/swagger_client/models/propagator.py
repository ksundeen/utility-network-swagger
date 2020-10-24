# coding: utf-8

"""
    Swagger for Utility Network

    Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network]( https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.6.1 using [NSwagStudio](https://github.com/RSuter/NSwag/wiki/NSwagStudio) C# code gen .   # noqa: E501

    OpenAPI spec version: 0.13
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Propagator(object):
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
        'network_attribute_name': 'str',
        'function_type': 'str',
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'network_attribute_name': 'networkAttributeName',
        'function_type': 'functionType',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, network_attribute_name=None, function_type=None, operator=None, value=None):  # noqa: E501
        """Propagator - a model defined in Swagger"""  # noqa: E501

        self._network_attribute_name = None
        self._function_type = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self.network_attribute_name = network_attribute_name
        self.function_type = function_type
        self.operator = operator
        self.value = value

    @property
    def network_attribute_name(self):
        """Gets the network_attribute_name of this Propagator.  # noqa: E501


        :return: The network_attribute_name of this Propagator.  # noqa: E501
        :rtype: str
        """
        return self._network_attribute_name

    @network_attribute_name.setter
    def network_attribute_name(self, network_attribute_name):
        """Sets the network_attribute_name of this Propagator.


        :param network_attribute_name: The network_attribute_name of this Propagator.  # noqa: E501
        :type: str
        """
        if network_attribute_name is None:
            raise ValueError("Invalid value for `network_attribute_name`, must not be `None`")  # noqa: E501

        self._network_attribute_name = network_attribute_name

    @property
    def function_type(self):
        """Gets the function_type of this Propagator.  # noqa: E501


        :return: The function_type of this Propagator.  # noqa: E501
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this Propagator.


        :param function_type: The function_type of this Propagator.  # noqa: E501
        :type: str
        """
        if function_type is None:
            raise ValueError("Invalid value for `function_type`, must not be `None`")  # noqa: E501
        allowed_values = ["bitwiseAnd", "min", "max"]  # noqa: E501
        if function_type not in allowed_values:
            raise ValueError(
                "Invalid value for `function_type` ({0}), must be one of {1}"  # noqa: E501
                .format(function_type, allowed_values)
            )

        self._function_type = function_type

    @property
    def operator(self):
        """Gets the operator of this Propagator.  # noqa: E501


        :return: The operator of this Propagator.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Propagator.


        :param operator: The operator of this Propagator.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = ["equal", "notEqual", "bitwiseAnd", "greater", "greaterEqual", "less", "lessEqual"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this Propagator.  # noqa: E501

        string (numeric)  # noqa: E501

        :return: The value of this Propagator.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Propagator.

        string (numeric)  # noqa: E501

        :param value: The value of this Propagator.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(Propagator, dict):
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
        if not isinstance(other, Propagator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other