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

from swagger_client.models.condition_barrier import ConditionBarrier  # noqa: F401,E501
from swagger_client.models.function_barrier import FunctionBarrier  # noqa: F401,E501
from swagger_client.models.nearest_neighbor_param import NearestNeighborParam  # noqa: F401,E501
from swagger_client.models.output_filter import OutputFilter  # noqa: F401,E501
from swagger_client.models.propagator import Propagator  # noqa: F401,E501
from swagger_client.models.trace_output_condition import TraceOutputCondition  # noqa: F401,E501


class TraceConfiguration(object):
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
        'include_containers': 'bool',
        'include_content': 'bool',
        'include_structures': 'bool',
        'include_barriers': 'bool',
        'validate_consistency': 'bool',
        'domain_network_name': 'str',
        'tier_name': 'str',
        'target_tier_name': 'str',
        'subnetwork_name': 'str',
        'diagram_template_name': 'str',
        'shortest_path_network_attribute_name': 'str',
        'filter_bitset_network_attribute_name': 'str',
        'traversability_scope': 'str',
        'condition_barriers': 'list[ConditionBarrier]',
        'category_barriers': 'list[str]',
        'function_barriers': 'list[FunctionBarrier]',
        'arcade_expression_barrier': 'str',
        'filter_barriers': 'list[str]',
        'filter_function_barriers': 'list[str]',
        'filter_scope': 'str',
        'functions': 'object',
        'nearest_neighbor': 'NearestNeighborParam',
        'output_filters': 'list[TraceOutputCondition]',
        'output_conditions': 'list[OutputFilter]',
        'propagators': 'list[Propagator]'
    }

    attribute_map = {
        'include_containers': 'includeContainers',
        'include_content': 'includeContent',
        'include_structures': 'includeStructures',
        'include_barriers': 'includeBarriers',
        'validate_consistency': 'validateConsistency',
        'domain_network_name': 'domainNetworkName',
        'tier_name': 'tierName',
        'target_tier_name': 'targetTierName',
        'subnetwork_name': 'subnetworkName',
        'diagram_template_name': 'diagramTemplateName',
        'shortest_path_network_attribute_name': 'shortestPathNetworkAttributeName',
        'filter_bitset_network_attribute_name': 'filterBitsetNetworkAttributeName',
        'traversability_scope': 'traversabilityScope',
        'condition_barriers': 'conditionBarriers',
        'category_barriers': 'categoryBarriers',
        'function_barriers': 'functionBarriers',
        'arcade_expression_barrier': 'arcadeExpressionBarrier',
        'filter_barriers': 'filterBarriers',
        'filter_function_barriers': 'filterFunctionBarriers',
        'filter_scope': 'filterScope',
        'functions': 'functions',
        'nearest_neighbor': 'nearestNeighbor',
        'output_filters': 'outputFilters',
        'output_conditions': 'outputConditions',
        'propagators': 'propagators'
    }

    def __init__(self, include_containers=False, include_content=False, include_structures=False, include_barriers=True, validate_consistency=False, domain_network_name='REPLACE_WITH_EMPTY_STRING', tier_name='REPLACE_WITH_EMPTY_STRING', target_tier_name='REPLACE_WITH_EMPTY_STRING', subnetwork_name='REPLACE_WITH_EMPTY_STRING', diagram_template_name='REPLACE_WITH_EMPTY_STRING', shortest_path_network_attribute_name='REPLACE_WITH_EMPTY_STRING', filter_bitset_network_attribute_name='REPLACE_WITH_EMPTY_STRING', traversability_scope='junctionsAndEdges', condition_barriers=None, category_barriers=None, function_barriers=None, arcade_expression_barrier='""', filter_barriers=None, filter_function_barriers=None, filter_scope='junctionsAndEdges', functions=None, nearest_neighbor=None, output_filters=None, output_conditions=None, propagators=None):  # noqa: E501
        """TraceConfiguration - a model defined in Swagger"""  # noqa: E501

        self._include_containers = None
        self._include_content = None
        self._include_structures = None
        self._include_barriers = None
        self._validate_consistency = None
        self._domain_network_name = None
        self._tier_name = None
        self._target_tier_name = None
        self._subnetwork_name = None
        self._diagram_template_name = None
        self._shortest_path_network_attribute_name = None
        self._filter_bitset_network_attribute_name = None
        self._traversability_scope = None
        self._condition_barriers = None
        self._category_barriers = None
        self._function_barriers = None
        self._arcade_expression_barrier = None
        self._filter_barriers = None
        self._filter_function_barriers = None
        self._filter_scope = None
        self._functions = None
        self._nearest_neighbor = None
        self._output_filters = None
        self._output_conditions = None
        self._propagators = None
        self.discriminator = None

        if include_containers is not None:
            self.include_containers = include_containers
        if include_content is not None:
            self.include_content = include_content
        if include_structures is not None:
            self.include_structures = include_structures
        if include_barriers is not None:
            self.include_barriers = include_barriers
        if validate_consistency is not None:
            self.validate_consistency = validate_consistency
        if domain_network_name is not None:
            self.domain_network_name = domain_network_name
        if tier_name is not None:
            self.tier_name = tier_name
        if target_tier_name is not None:
            self.target_tier_name = target_tier_name
        if subnetwork_name is not None:
            self.subnetwork_name = subnetwork_name
        if diagram_template_name is not None:
            self.diagram_template_name = diagram_template_name
        if shortest_path_network_attribute_name is not None:
            self.shortest_path_network_attribute_name = shortest_path_network_attribute_name
        if filter_bitset_network_attribute_name is not None:
            self.filter_bitset_network_attribute_name = filter_bitset_network_attribute_name
        if traversability_scope is not None:
            self.traversability_scope = traversability_scope
        self.condition_barriers = condition_barriers
        if category_barriers is not None:
            self.category_barriers = category_barriers
        self.function_barriers = function_barriers
        if arcade_expression_barrier is not None:
            self.arcade_expression_barrier = arcade_expression_barrier
        self.filter_barriers = filter_barriers
        self.filter_function_barriers = filter_function_barriers
        if filter_scope is not None:
            self.filter_scope = filter_scope
        self.functions = functions
        self.nearest_neighbor = nearest_neighbor
        self.output_filters = output_filters
        self.output_conditions = output_conditions
        self.propagators = propagators

    @property
    def include_containers(self):
        """Gets the include_containers of this TraceConfiguration.  # noqa: E501

        Optional parameter representing whether or not to include containers in the trace result (default is false).  # noqa: E501

        :return: The include_containers of this TraceConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._include_containers

    @include_containers.setter
    def include_containers(self, include_containers):
        """Sets the include_containers of this TraceConfiguration.

        Optional parameter representing whether or not to include containers in the trace result (default is false).  # noqa: E501

        :param include_containers: The include_containers of this TraceConfiguration.  # noqa: E501
        :type: bool
        """

        self._include_containers = include_containers

    @property
    def include_content(self):
        """Gets the include_content of this TraceConfiguration.  # noqa: E501

        Optional parameter representing whether or not to include content in the trace result (default is false).  # noqa: E501

        :return: The include_content of this TraceConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._include_content

    @include_content.setter
    def include_content(self, include_content):
        """Sets the include_content of this TraceConfiguration.

        Optional parameter representing whether or not to include content in the trace result (default is false).  # noqa: E501

        :param include_content: The include_content of this TraceConfiguration.  # noqa: E501
        :type: bool
        """

        self._include_content = include_content

    @property
    def include_structures(self):
        """Gets the include_structures of this TraceConfiguration.  # noqa: E501

        Optional parameter representing whether or not to include structures in the trace result (default is false).  # noqa: E501

        :return: The include_structures of this TraceConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._include_structures

    @include_structures.setter
    def include_structures(self, include_structures):
        """Sets the include_structures of this TraceConfiguration.

        Optional parameter representing whether or not to include structures in the trace result (default is false).  # noqa: E501

        :param include_structures: The include_structures of this TraceConfiguration.  # noqa: E501
        :type: bool
        """

        self._include_structures = include_structures

    @property
    def include_barriers(self):
        """Gets the include_barriers of this TraceConfiguration.  # noqa: E501

        Optional parameter representing whether or not to include barrier features that stop a trace in the trace result (default is true).  # noqa: E501

        :return: The include_barriers of this TraceConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._include_barriers

    @include_barriers.setter
    def include_barriers(self, include_barriers):
        """Sets the include_barriers of this TraceConfiguration.

        Optional parameter representing whether or not to include barrier features that stop a trace in the trace result (default is true).  # noqa: E501

        :param include_barriers: The include_barriers of this TraceConfiguration.  # noqa: E501
        :type: bool
        """

        self._include_barriers = include_barriers

    @property
    def validate_consistency(self):
        """Gets the validate_consistency of this TraceConfiguration.  # noqa: E501

        Optional parameter representing whether or not to validate the consistency of the trace results (default is false).  # noqa: E501

        :return: The validate_consistency of this TraceConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._validate_consistency

    @validate_consistency.setter
    def validate_consistency(self, validate_consistency):
        """Sets the validate_consistency of this TraceConfiguration.

        Optional parameter representing whether or not to validate the consistency of the trace results (default is false).  # noqa: E501

        :param validate_consistency: The validate_consistency of this TraceConfiguration.  # noqa: E501
        :type: bool
        """

        self._validate_consistency = validate_consistency

    @property
    def domain_network_name(self):
        """Gets the domain_network_name of this TraceConfiguration.  # noqa: E501

        Optional parameter that specifies the name of the domain network where the trace is starting.  # noqa: E501

        :return: The domain_network_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._domain_network_name

    @domain_network_name.setter
    def domain_network_name(self, domain_network_name):
        """Sets the domain_network_name of this TraceConfiguration.

        Optional parameter that specifies the name of the domain network where the trace is starting.  # noqa: E501

        :param domain_network_name: The domain_network_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._domain_network_name = domain_network_name

    @property
    def tier_name(self):
        """Gets the tier_name of this TraceConfiguration.  # noqa: E501

        Optional parameter that specifies the name of the tier where the trace is starting.  # noqa: E501

        :return: The tier_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._tier_name

    @tier_name.setter
    def tier_name(self, tier_name):
        """Sets the tier_name of this TraceConfiguration.

        Optional parameter that specifies the name of the tier where the trace is starting.  # noqa: E501

        :param tier_name: The tier_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._tier_name = tier_name

    @property
    def target_tier_name(self):
        """Gets the target_tier_name of this TraceConfiguration.  # noqa: E501

        Optional parameter representing the name of the tier where upstream or downstream trace ends.  # noqa: E501

        :return: The target_tier_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._target_tier_name

    @target_tier_name.setter
    def target_tier_name(self, target_tier_name):
        """Sets the target_tier_name of this TraceConfiguration.

        Optional parameter representing the name of the tier where upstream or downstream trace ends.  # noqa: E501

        :param target_tier_name: The target_tier_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._target_tier_name = target_tier_name

    @property
    def subnetwork_name(self):
        """Gets the subnetwork_name of this TraceConfiguration.  # noqa: E501

        Optional parameter representing the name of the subnetwork that will be traced - the starting points of the trace will be the controllers of this subnetwork .  # noqa: E501

        :return: The subnetwork_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._subnetwork_name

    @subnetwork_name.setter
    def subnetwork_name(self, subnetwork_name):
        """Sets the subnetwork_name of this TraceConfiguration.

        Optional parameter representing the name of the subnetwork that will be traced - the starting points of the trace will be the controllers of this subnetwork .  # noqa: E501

        :param subnetwork_name: The subnetwork_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._subnetwork_name = subnetwork_name

    @property
    def diagram_template_name(self):
        """Gets the diagram_template_name of this TraceConfiguration.  # noqa: E501

        Optional parameter representing the name of the diagram template.  # noqa: E501

        :return: The diagram_template_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._diagram_template_name

    @diagram_template_name.setter
    def diagram_template_name(self, diagram_template_name):
        """Sets the diagram_template_name of this TraceConfiguration.

        Optional parameter representing the name of the diagram template.  # noqa: E501

        :param diagram_template_name: The diagram_template_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._diagram_template_name = diagram_template_name

    @property
    def shortest_path_network_attribute_name(self):
        """Gets the shortest_path_network_attribute_name of this TraceConfiguration.  # noqa: E501

        Required parameter for shortest path trace ; optional otherwise. It represents the network attribute name used for determining cost when calulating the shortest path.  # noqa: E501

        :return: The shortest_path_network_attribute_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._shortest_path_network_attribute_name

    @shortest_path_network_attribute_name.setter
    def shortest_path_network_attribute_name(self, shortest_path_network_attribute_name):
        """Sets the shortest_path_network_attribute_name of this TraceConfiguration.

        Required parameter for shortest path trace ; optional otherwise. It represents the network attribute name used for determining cost when calulating the shortest path.  # noqa: E501

        :param shortest_path_network_attribute_name: The shortest_path_network_attribute_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._shortest_path_network_attribute_name = shortest_path_network_attribute_name

    @property
    def filter_bitset_network_attribute_name(self):
        """Gets the filter_bitset_network_attribute_name of this TraceConfiguration.  # noqa: E501

        Optional parameter. Used during loops trace to only return loops with the same bit set all around the loop. Used during upstream/downstream traces to ensure that trace results include any bit that is set in the starting points for the network attribute.  # noqa: E501

        :return: The filter_bitset_network_attribute_name of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._filter_bitset_network_attribute_name

    @filter_bitset_network_attribute_name.setter
    def filter_bitset_network_attribute_name(self, filter_bitset_network_attribute_name):
        """Sets the filter_bitset_network_attribute_name of this TraceConfiguration.

        Optional parameter. Used during loops trace to only return loops with the same bit set all around the loop. Used during upstream/downstream traces to ensure that trace results include any bit that is set in the starting points for the network attribute.  # noqa: E501

        :param filter_bitset_network_attribute_name: The filter_bitset_network_attribute_name of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._filter_bitset_network_attribute_name = filter_bitset_network_attribute_name

    @property
    def traversability_scope(self):
        """Gets the traversability_scope of this TraceConfiguration.  # noqa: E501

        Optional parameters representing which network element types the condition, category, or function barriers apply to (default is junctionsAndEdges).  # noqa: E501

        :return: The traversability_scope of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._traversability_scope

    @traversability_scope.setter
    def traversability_scope(self, traversability_scope):
        """Sets the traversability_scope of this TraceConfiguration.

        Optional parameters representing which network element types the condition, category, or function barriers apply to (default is junctionsAndEdges).  # noqa: E501

        :param traversability_scope: The traversability_scope of this TraceConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["junctions", "edges", "junctionsAndEdges"]  # noqa: E501
        if traversability_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `traversability_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(traversability_scope, allowed_values)
            )

        self._traversability_scope = traversability_scope

    @property
    def condition_barriers(self):
        """Gets the condition_barriers of this TraceConfiguration.  # noqa: E501

        Optional parameter containing an array of objects (representing network attribute conditions) that serve as barriers - default is null. If isTypeSpecificValue is true, the network attribute is being compared with a specific value ; otherwise the network attribute is being compared with another network attribute.  # noqa: E501

        :return: The condition_barriers of this TraceConfiguration.  # noqa: E501
        :rtype: list[ConditionBarrier]
        """
        return self._condition_barriers

    @condition_barriers.setter
    def condition_barriers(self, condition_barriers):
        """Sets the condition_barriers of this TraceConfiguration.

        Optional parameter containing an array of objects (representing network attribute conditions) that serve as barriers - default is null. If isTypeSpecificValue is true, the network attribute is being compared with a specific value ; otherwise the network attribute is being compared with another network attribute.  # noqa: E501

        :param condition_barriers: The condition_barriers of this TraceConfiguration.  # noqa: E501
        :type: list[ConditionBarrier]
        """
        if condition_barriers is None:
            raise ValueError("Invalid value for `condition_barriers`, must not be `None`")  # noqa: E501

        self._condition_barriers = condition_barriers

    @property
    def category_barriers(self):
        """Gets the category_barriers of this TraceConfiguration.  # noqa: E501

        The categories that serve as barriers (default is none) : optional parameter.  # noqa: E501

        :return: The category_barriers of this TraceConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_barriers

    @category_barriers.setter
    def category_barriers(self, category_barriers):
        """Sets the category_barriers of this TraceConfiguration.

        The categories that serve as barriers (default is none) : optional parameter.  # noqa: E501

        :param category_barriers: The category_barriers of this TraceConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._category_barriers = category_barriers

    @property
    def function_barriers(self):
        """Gets the function_barriers of this TraceConfiguration.  # noqa: E501

        optional parameter.  # noqa: E501

        :return: The function_barriers of this TraceConfiguration.  # noqa: E501
        :rtype: list[FunctionBarrier]
        """
        return self._function_barriers

    @function_barriers.setter
    def function_barriers(self, function_barriers):
        """Sets the function_barriers of this TraceConfiguration.

        optional parameter.  # noqa: E501

        :param function_barriers: The function_barriers of this TraceConfiguration.  # noqa: E501
        :type: list[FunctionBarrier]
        """
        if function_barriers is None:
            raise ValueError("Invalid value for `function_barriers`, must not be `None`")  # noqa: E501

        self._function_barriers = function_barriers

    @property
    def arcade_expression_barrier(self):
        """Gets the arcade_expression_barrier of this TraceConfiguration.  # noqa: E501


        :return: The arcade_expression_barrier of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._arcade_expression_barrier

    @arcade_expression_barrier.setter
    def arcade_expression_barrier(self, arcade_expression_barrier):
        """Sets the arcade_expression_barrier of this TraceConfiguration.


        :param arcade_expression_barrier: The arcade_expression_barrier of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._arcade_expression_barrier = arcade_expression_barrier

    @property
    def filter_barriers(self):
        """Gets the filter_barriers of this TraceConfiguration.  # noqa: E501

        A second pass is done over the trace results and all results after these categories are encountered are filtered (default is none) : optional parameter.  # noqa: E501

        :return: The filter_barriers of this TraceConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_barriers

    @filter_barriers.setter
    def filter_barriers(self, filter_barriers):
        """Sets the filter_barriers of this TraceConfiguration.

        A second pass is done over the trace results and all results after these categories are encountered are filtered (default is none) : optional parameter.  # noqa: E501

        :param filter_barriers: The filter_barriers of this TraceConfiguration.  # noqa: E501
        :type: list[str]
        """
        if filter_barriers is None:
            raise ValueError("Invalid value for `filter_barriers`, must not be `None`")  # noqa: E501

        self._filter_barriers = filter_barriers

    @property
    def filter_function_barriers(self):
        """Gets the filter_function_barriers of this TraceConfiguration.  # noqa: E501


        :return: The filter_function_barriers of this TraceConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_function_barriers

    @filter_function_barriers.setter
    def filter_function_barriers(self, filter_function_barriers):
        """Sets the filter_function_barriers of this TraceConfiguration.


        :param filter_function_barriers: The filter_function_barriers of this TraceConfiguration.  # noqa: E501
        :type: list[str]
        """
        if filter_function_barriers is None:
            raise ValueError("Invalid value for `filter_function_barriers`, must not be `None`")  # noqa: E501

        self._filter_function_barriers = filter_function_barriers

    @property
    def filter_scope(self):
        """Gets the filter_scope of this TraceConfiguration.  # noqa: E501


        :return: The filter_scope of this TraceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._filter_scope

    @filter_scope.setter
    def filter_scope(self, filter_scope):
        """Sets the filter_scope of this TraceConfiguration.


        :param filter_scope: The filter_scope of this TraceConfiguration.  # noqa: E501
        :type: str
        """

        self._filter_scope = filter_scope

    @property
    def functions(self):
        """Gets the functions of this TraceConfiguration.  # noqa: E501

        Optional parameter ; an array of objects representing functions. Each function may have an optional array of network attribute conditions.  # noqa: E501

        :return: The functions of this TraceConfiguration.  # noqa: E501
        :rtype: object
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this TraceConfiguration.

        Optional parameter ; an array of objects representing functions. Each function may have an optional array of network attribute conditions.  # noqa: E501

        :param functions: The functions of this TraceConfiguration.  # noqa: E501
        :type: object
        """
        if functions is None:
            raise ValueError("Invalid value for `functions`, must not be `None`")  # noqa: E501

        self._functions = functions

    @property
    def nearest_neighbor(self):
        """Gets the nearest_neighbor of this TraceConfiguration.  # noqa: E501


        :return: The nearest_neighbor of this TraceConfiguration.  # noqa: E501
        :rtype: NearestNeighborParam
        """
        return self._nearest_neighbor

    @nearest_neighbor.setter
    def nearest_neighbor(self, nearest_neighbor):
        """Sets the nearest_neighbor of this TraceConfiguration.


        :param nearest_neighbor: The nearest_neighbor of this TraceConfiguration.  # noqa: E501
        :type: NearestNeighborParam
        """
        if nearest_neighbor is None:
            raise ValueError("Invalid value for `nearest_neighbor`, must not be `None`")  # noqa: E501

        self._nearest_neighbor = nearest_neighbor

    @property
    def output_filters(self):
        """Gets the output_filters of this TraceConfiguration.  # noqa: E501


        :return: The output_filters of this TraceConfiguration.  # noqa: E501
        :rtype: list[TraceOutputCondition]
        """
        return self._output_filters

    @output_filters.setter
    def output_filters(self, output_filters):
        """Sets the output_filters of this TraceConfiguration.


        :param output_filters: The output_filters of this TraceConfiguration.  # noqa: E501
        :type: list[TraceOutputCondition]
        """
        if output_filters is None:
            raise ValueError("Invalid value for `output_filters`, must not be `None`")  # noqa: E501

        self._output_filters = output_filters

    @property
    def output_conditions(self):
        """Gets the output_conditions of this TraceConfiguration.  # noqa: E501

        The categories associated with the output filter (default is none) ; optional parameter.  # noqa: E501

        :return: The output_conditions of this TraceConfiguration.  # noqa: E501
        :rtype: list[OutputFilter]
        """
        return self._output_conditions

    @output_conditions.setter
    def output_conditions(self, output_conditions):
        """Sets the output_conditions of this TraceConfiguration.

        The categories associated with the output filter (default is none) ; optional parameter.  # noqa: E501

        :param output_conditions: The output_conditions of this TraceConfiguration.  # noqa: E501
        :type: list[OutputFilter]
        """
        if output_conditions is None:
            raise ValueError("Invalid value for `output_conditions`, must not be `None`")  # noqa: E501

        self._output_conditions = output_conditions

    @property
    def propagators(self):
        """Gets the propagators of this TraceConfiguration.  # noqa: E501


        :return: The propagators of this TraceConfiguration.  # noqa: E501
        :rtype: list[Propagator]
        """
        return self._propagators

    @propagators.setter
    def propagators(self, propagators):
        """Sets the propagators of this TraceConfiguration.


        :param propagators: The propagators of this TraceConfiguration.  # noqa: E501
        :type: list[Propagator]
        """
        if propagators is None:
            raise ValueError("Invalid value for `propagators`, must not be `None`")  # noqa: E501

        self._propagators = propagators

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
        if issubclass(TraceConfiguration, dict):
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
        if not isinstance(other, TraceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
