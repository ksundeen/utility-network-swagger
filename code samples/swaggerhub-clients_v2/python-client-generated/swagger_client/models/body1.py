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

class Body1(object):
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
        'f': 'str',
        'gdb_version': 'str',
        'session_id': 'str',
        'moment': 'str',
        'trace_type': 'str',
        'trace_locations': 'list',
        'trace_configuration': 'object',
        'result_types': 'list'
    }

    attribute_map = {
        'f': 'f',
        'gdb_version': 'gdbVersion',
        'session_id': 'sessionId',
        'moment': 'moment',
        'trace_type': 'traceType',
        'trace_locations': 'traceLocations',
        'trace_configuration': 'traceConfiguration',
        'result_types': 'resultTypes'
    }

    def __init__(self, f='json', gdb_version='sde.DEFAULT', session_id='', moment=None, trace_type=None, trace_locations=None, trace_configuration=None, result_types=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._f = None
        self._gdb_version = None
        self._session_id = None
        self._moment = None
        self._trace_type = None
        self._trace_locations = None
        self._trace_configuration = None
        self._result_types = None
        self.discriminator = None
        self.f = f
        if gdb_version is not None:
            self.gdb_version = gdb_version
        if session_id is not None:
            self.session_id = session_id
        if moment is not None:
            self.moment = moment
        self.trace_type = trace_type
        self.trace_locations = trace_locations
        self.trace_configuration = trace_configuration
        self.result_types = result_types

    @property
    def f(self):
        """Gets the f of this Body1.  # noqa: E501

        Optional parameter representing the output format of the response (default is JSON).  # noqa: E501

        :return: The f of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._f

    @f.setter
    def f(self, f):
        """Sets the f of this Body1.

        Optional parameter representing the output format of the response (default is JSON).  # noqa: E501

        :param f: The f of this Body1.  # noqa: E501
        :type: str
        """
        if f is None:
            raise ValueError("Invalid value for `f`, must not be `None`")  # noqa: E501

        self._f = f

    @property
    def gdb_version(self):
        """Gets the gdb_version of this Body1.  # noqa: E501

        The name of the geodatabase version.  # noqa: E501

        :return: The gdb_version of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._gdb_version

    @gdb_version.setter
    def gdb_version(self, gdb_version):
        """Sets the gdb_version of this Body1.

        The name of the geodatabase version.  # noqa: E501

        :param gdb_version: The gdb_version of this Body1.  # noqa: E501
        :type: str
        """

        self._gdb_version = gdb_version

    @property
    def session_id(self):
        """Gets the session_id of this Body1.  # noqa: E501

        Optional parameter representing the token (guid) used to lock the version. If the calling client has previously started a service session (editing) and holds an exclusive lock on the specified version, the request will fail if the sessionId is not provided. If the specified version is currently locked by any other session, the request will fail if the sessionId is not provided or does not match the sessionId which holds the exclusive lock.  # noqa: E501

        :return: The session_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this Body1.

        Optional parameter representing the token (guid) used to lock the version. If the calling client has previously started a service session (editing) and holds an exclusive lock on the specified version, the request will fail if the sessionId is not provided. If the specified version is currently locked by any other session, the request will fail if the sessionId is not provided or does not match the sessionId which holds the exclusive lock.  # noqa: E501

        :param session_id: The session_id of this Body1.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def moment(self):
        """Gets the moment of this Body1.  # noqa: E501

        Optional parameter representing the session moment (the default is the version current moment). This should only be specified by the client when they do not want to use the current moment.  # noqa: E501

        :return: The moment of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._moment

    @moment.setter
    def moment(self, moment):
        """Sets the moment of this Body1.

        Optional parameter representing the session moment (the default is the version current moment). This should only be specified by the client when they do not want to use the current moment.  # noqa: E501

        :param moment: The moment of this Body1.  # noqa: E501
        :type: str
        """

        self._moment = moment

    @property
    def trace_type(self):
        """Gets the trace_type of this Body1.  # noqa: E501

        The trace type.  # noqa: E501

        :return: The trace_type of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        """Sets the trace_type of this Body1.

        The trace type.  # noqa: E501

        :param trace_type: The trace_type of this Body1.  # noqa: E501
        :type: str
        """
        if trace_type is None:
            raise ValueError("Invalid value for `trace_type`, must not be `None`")  # noqa: E501
        allowed_values = ["upstream", "downstream", "connected", "subnetwork", "unknown", "loops", "shortestpath", "subnetworkcontroller"]  # noqa: E501
        if trace_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trace_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trace_type, allowed_values)
            )

        self._trace_type = trace_type

    @property
    def trace_locations(self):
        """Gets the trace_locations of this Body1.  # noqa: E501

        ***Curently a workaround until figure out how to gen**The locations for starting and stopping points, as well as barriers. Optional parameter for subnetwork trace type, required parameter for all other trace types.  # noqa: E501

        :return: The trace_locations of this Body1.  # noqa: E501
        :rtype: list
        """
        return self._trace_locations

    @trace_locations.setter
    def trace_locations(self, trace_locations):
        """Sets the trace_locations of this Body1.

        ***Curently a workaround until figure out how to gen**The locations for starting and stopping points, as well as barriers. Optional parameter for subnetwork trace type, required parameter for all other trace types.  # noqa: E501

        :param trace_locations: The trace_locations of this Body1.  # noqa: E501
        :type: list
        """
        if trace_locations is None:
            raise ValueError("Invalid value for `trace_locations`, must not be `None`")  # noqa: E501

        self._trace_locations = trace_locations

    @property
    def trace_configuration(self):
        """Gets the trace_configuration of this Body1.  # noqa: E501

        The locations for starting and stopping points, as well as barriers. Optional parameter for subnetwork trace type, required parameter for all other trace types.  # noqa: E501

        :return: The trace_configuration of this Body1.  # noqa: E501
        :rtype: object
        """
        return self._trace_configuration

    @trace_configuration.setter
    def trace_configuration(self, trace_configuration):
        """Sets the trace_configuration of this Body1.

        The locations for starting and stopping points, as well as barriers. Optional parameter for subnetwork trace type, required parameter for all other trace types.  # noqa: E501

        :param trace_configuration: The trace_configuration of this Body1.  # noqa: E501
        :type: object
        """
        if trace_configuration is None:
            raise ValueError("Invalid value for `trace_configuration`, must not be `None`")  # noqa: E501

        self._trace_configuration = trace_configuration

    @property
    def result_types(self):
        """Gets the result_types of this Body1.  # noqa: E501

        Optional parameter representing the types of results to return.  # noqa: E501

        :return: The result_types of this Body1.  # noqa: E501
        :rtype: list
        """
        return self._result_types

    @result_types.setter
    def result_types(self, result_types):
        """Sets the result_types of this Body1.

        Optional parameter representing the types of results to return.  # noqa: E501

        :param result_types: The result_types of this Body1.  # noqa: E501
        :type: list
        """
        if result_types is None:
            raise ValueError("Invalid value for `result_types`, must not be `None`")  # noqa: E501

        self._result_types = result_types

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other