# coding: utf-8

"""
    Chain Query

    The LBRY blockchain is read into SQL where important structured information can be extracted through the Chain Query API.  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class QueryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def s_ql_query(self, query, values, **kwargs):  # noqa: E501
        """Use SQL in a RESTful way  # noqa: E501

        API exposed for sending SQL queries directly against the chainquery database. Since this is an exposed API there are limits to its use. These limits include queries per hour, read-only, limited to 60 second timeout.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.s_ql_query(query, values, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: The SQL query to be put against the chainquery database. (required)
        :param list[str] values: when passing in a query use '?' for values which will be replaced in order of appearance with this array. (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.s_ql_query_with_http_info(query, values, **kwargs)  # noqa: E501
        else:
            (data) = self.s_ql_query_with_http_info(query, values, **kwargs)  # noqa: E501
            return data

    def s_ql_query_with_http_info(self, query, values, **kwargs):  # noqa: E501
        """Use SQL in a RESTful way  # noqa: E501

        API exposed for sending SQL queries directly against the chainquery database. Since this is an exposed API there are limits to its use. These limits include queries per hour, read-only, limited to 60 second timeout.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.s_ql_query_with_http_info(query, values, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: The SQL query to be put against the chainquery database. (required)
        :param list[str] values: when passing in a query use '?' for values which will be replaced in order of appearance with this array. (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'values']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_ql_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `s_ql_query`")  # noqa: E501
        # verify the required parameter 'values' is set
        if ('values' not in params or
                params['values'] is None):
            raise ValueError("Missing the required parameter `values` when calling `s_ql_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501
        if 'values' in params:
            path_params['values'] = params['values']  # noqa: E501
            collection_formats['values'] = 'csv'  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sql', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
