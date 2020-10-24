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

class NearestNeighborParam(object):
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
        'count': 'int',
        'cost_network_attribute_name': 'str',
        'nearest_categories': 'list[str]',
        'nearest_assets': 'list[str]'
    }

    attribute_map = {
        'count': 'count',
        'cost_network_attribute_name': 'costNetworkAttributeName',
        'nearest_categories': 'nearestCategories',
        'nearest_assets': 'nearestAssets'
    }

    def __init__(self, count=None, cost_network_attribute_name='', nearest_categories=None, nearest_assets=None):  # noqa: E501
        """NearestNeighborParam - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._cost_network_attribute_name = None
        self._nearest_categories = None
        self._nearest_assets = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if cost_network_attribute_name is not None:
            self.cost_network_attribute_name = cost_network_attribute_name
        self.nearest_categories = nearest_categories
        self.nearest_assets = nearest_assets

    @property
    def count(self):
        """Gets the count of this NearestNeighborParam.  # noqa: E501


        :return: The count of this NearestNeighborParam.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NearestNeighborParam.


        :param count: The count of this NearestNeighborParam.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cost_network_attribute_name(self):
        """Gets the cost_network_attribute_name of this NearestNeighborParam.  # noqa: E501


        :return: The cost_network_attribute_name of this NearestNeighborParam.  # noqa: E501
        :rtype: str
        """
        return self._cost_network_attribute_name

    @cost_network_attribute_name.setter
    def cost_network_attribute_name(self, cost_network_attribute_name):
        """Sets the cost_network_attribute_name of this NearestNeighborParam.


        :param cost_network_attribute_name: The cost_network_attribute_name of this NearestNeighborParam.  # noqa: E501
        :type: str
        """

        self._cost_network_attribute_name = cost_network_attribute_name

    @property
    def nearest_categories(self):
        """Gets the nearest_categories of this NearestNeighborParam.  # noqa: E501


        :return: The nearest_categories of this NearestNeighborParam.  # noqa: E501
        :rtype: list[str]
        """
        return self._nearest_categories

    @nearest_categories.setter
    def nearest_categories(self, nearest_categories):
        """Sets the nearest_categories of this NearestNeighborParam.


        :param nearest_categories: The nearest_categories of this NearestNeighborParam.  # noqa: E501
        :type: list[str]
        """
        if nearest_categories is None:
            raise ValueError("Invalid value for `nearest_categories`, must not be `None`")  # noqa: E501

        self._nearest_categories = nearest_categories

    @property
    def nearest_assets(self):
        """Gets the nearest_assets of this NearestNeighborParam.  # noqa: E501


        :return: The nearest_assets of this NearestNeighborParam.  # noqa: E501
        :rtype: list[str]
        """
        return self._nearest_assets

    @nearest_assets.setter
    def nearest_assets(self, nearest_assets):
        """Sets the nearest_assets of this NearestNeighborParam.


        :param nearest_assets: The nearest_assets of this NearestNeighborParam.  # noqa: E501
        :type: list[str]
        """
        if nearest_assets is None:
            raise ValueError("Invalid value for `nearest_assets`, must not be `None`")  # noqa: E501

        self._nearest_assets = nearest_assets

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
        if issubclass(NearestNeighborParam, dict):
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
        if not isinstance(other, NearestNeighborParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
