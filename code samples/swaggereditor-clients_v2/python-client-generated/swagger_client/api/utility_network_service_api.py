# coding: utf-8

"""
    Swagger for Utility Network

    Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network](https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.8.1 using OpenAPI Specification (OAC) written in [SwaggerEditor](https://github.com/swagger-api/swagger-editor)   and [SwaggerHub](https://app.swaggerhub.com/) for C# and Typescript-Angular code generation.    # noqa: E501

    OpenAPI spec version: 3.0
    Contact: kim.sundeen@sspinnovations.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UtilityNetworkServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def portal_web_adaptor_sharing_rest_generate_token_post(self, body, portal_web_adaptor, **kwargs):  # noqa: E501
        """generateToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portal_web_adaptor_sharing_rest_generate_token_post(body, portal_web_adaptor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body2 body: (required)
        :param str portal_web_adaptor: (required)
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.portal_web_adaptor_sharing_rest_generate_token_post_with_http_info(body, portal_web_adaptor, **kwargs)  # noqa: E501
        else:
            (data) = self.portal_web_adaptor_sharing_rest_generate_token_post_with_http_info(body, portal_web_adaptor, **kwargs)  # noqa: E501
            return data

    def portal_web_adaptor_sharing_rest_generate_token_post_with_http_info(self, body, portal_web_adaptor, **kwargs):  # noqa: E501
        """generateToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portal_web_adaptor_sharing_rest_generate_token_post_with_http_info(body, portal_web_adaptor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body2 body: (required)
        :param str portal_web_adaptor: (required)
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'portal_web_adaptor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method portal_web_adaptor_sharing_rest_generate_token_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `portal_web_adaptor_sharing_rest_generate_token_post`")  # noqa: E501
        # verify the required parameter 'portal_web_adaptor' is set
        if ('portal_web_adaptor' not in params or
                params['portal_web_adaptor'] is None):
            raise ValueError("Missing the required parameter `portal_web_adaptor` when calling `portal_web_adaptor_sharing_rest_generate_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'portal_web_adaptor' in params:
            path_params['PortalWebAdaptor'] = params['portal_web_adaptor']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{PortalWebAdaptor}/sharing/rest/generateToken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trace(self, body, token, server_web_adaptor, utility_network_name, **kwargs):  # noqa: E501
        """trace  # noqa: E501

        Trace  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trace(body, token, server_web_adaptor, utility_network_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body1 body: (required)
        :param str token: (required)
        :param str server_web_adaptor: (required)
        :param str utility_network_name: (required)
        :return: TraceResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trace_with_http_info(body, token, server_web_adaptor, utility_network_name, **kwargs)  # noqa: E501
        else:
            (data) = self.trace_with_http_info(body, token, server_web_adaptor, utility_network_name, **kwargs)  # noqa: E501
            return data

    def trace_with_http_info(self, body, token, server_web_adaptor, utility_network_name, **kwargs):  # noqa: E501
        """trace  # noqa: E501

        Trace  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trace_with_http_info(body, token, server_web_adaptor, utility_network_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body1 body: (required)
        :param str token: (required)
        :param str server_web_adaptor: (required)
        :param str utility_network_name: (required)
        :return: TraceResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'token', 'server_web_adaptor', 'utility_network_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `trace`")  # noqa: E501
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `trace`")  # noqa: E501
        # verify the required parameter 'server_web_adaptor' is set
        if ('server_web_adaptor' not in params or
                params['server_web_adaptor'] is None):
            raise ValueError("Missing the required parameter `server_web_adaptor` when calling `trace`")  # noqa: E501
        # verify the required parameter 'utility_network_name' is set
        if ('utility_network_name' not in params or
                params['utility_network_name'] is None):
            raise ValueError("Missing the required parameter `utility_network_name` when calling `trace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_web_adaptor' in params:
            path_params['ServerWebAdaptor'] = params['server_web_adaptor']  # noqa: E501
        if 'utility_network_name' in params:
            path_params['UtilityNetworkName'] = params['utility_network_name']  # noqa: E501

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{ServerWebAdaptor}/rest/services/{UtilityNetworkName}/UtilityNetworkServer/trace', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TraceResultsSet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
