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


class TraceResultsSetTraceResultsElements(object):
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
        'network_source_id': 'float',
        'global_id': 'str',
        'object_id': 'float',
        'terminal_id': 'float',
        'asset_group_code': 'float',
        'asset_type_code': 'float'
    }

    attribute_map = {
        'network_source_id': 'networkSourceId',
        'global_id': 'globalId',
        'object_id': 'objectId',
        'terminal_id': 'terminalId',
        'asset_group_code': 'assetGroupCode',
        'asset_type_code': 'assetTypeCode'
    }

    def __init__(self, network_source_id=None, global_id=None, object_id=None, terminal_id=None, asset_group_code=None, asset_type_code=None):  # noqa: E501
        """TraceResultsSetTraceResultsElements - a model defined in Swagger"""  # noqa: E501

        self._network_source_id = None
        self._global_id = None
        self._object_id = None
        self._terminal_id = None
        self._asset_group_code = None
        self._asset_type_code = None
        self.discriminator = None

        if network_source_id is not None:
            self.network_source_id = network_source_id
        if global_id is not None:
            self.global_id = global_id
        if object_id is not None:
            self.object_id = object_id
        if terminal_id is not None:
            self.terminal_id = terminal_id
        if asset_group_code is not None:
            self.asset_group_code = asset_group_code
        if asset_type_code is not None:
            self.asset_type_code = asset_type_code

    @property
    def network_source_id(self):
        """Gets the network_source_id of this TraceResultsSetTraceResultsElements.  # noqa: E501


        :return: The network_source_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :rtype: float
        """
        return self._network_source_id

    @network_source_id.setter
    def network_source_id(self, network_source_id):
        """Sets the network_source_id of this TraceResultsSetTraceResultsElements.


        :param network_source_id: The network_source_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :type: float
        """

        self._network_source_id = network_source_id

    @property
    def global_id(self):
        """Gets the global_id of this TraceResultsSetTraceResultsElements.  # noqa: E501


        :return: The global_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :rtype: str
        """
        return self._global_id

    @global_id.setter
    def global_id(self, global_id):
        """Sets the global_id of this TraceResultsSetTraceResultsElements.


        :param global_id: The global_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :type: str
        """

        self._global_id = global_id

    @property
    def object_id(self):
        """Gets the object_id of this TraceResultsSetTraceResultsElements.  # noqa: E501


        :return: The object_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :rtype: float
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this TraceResultsSetTraceResultsElements.


        :param object_id: The object_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :type: float
        """

        self._object_id = object_id

    @property
    def terminal_id(self):
        """Gets the terminal_id of this TraceResultsSetTraceResultsElements.  # noqa: E501


        :return: The terminal_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :rtype: float
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this TraceResultsSetTraceResultsElements.


        :param terminal_id: The terminal_id of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :type: float
        """

        self._terminal_id = terminal_id

    @property
    def asset_group_code(self):
        """Gets the asset_group_code of this TraceResultsSetTraceResultsElements.  # noqa: E501


        :return: The asset_group_code of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :rtype: float
        """
        return self._asset_group_code

    @asset_group_code.setter
    def asset_group_code(self, asset_group_code):
        """Sets the asset_group_code of this TraceResultsSetTraceResultsElements.


        :param asset_group_code: The asset_group_code of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :type: float
        """

        self._asset_group_code = asset_group_code

    @property
    def asset_type_code(self):
        """Gets the asset_type_code of this TraceResultsSetTraceResultsElements.  # noqa: E501


        :return: The asset_type_code of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :rtype: float
        """
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, asset_type_code):
        """Sets the asset_type_code of this TraceResultsSetTraceResultsElements.


        :param asset_type_code: The asset_type_code of this TraceResultsSetTraceResultsElements.  # noqa: E501
        :type: float
        """

        self._asset_type_code = asset_type_code

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
        if issubclass(TraceResultsSetTraceResultsElements, dict):
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
        if not isinstance(other, TraceResultsSetTraceResultsElements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
