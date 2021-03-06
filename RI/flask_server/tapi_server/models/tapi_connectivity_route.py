# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_local_class import TapiCommonLocalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_connection_end_point_ref import TapiConnectivityConnectionEndPointRef  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityRoute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, local_id=None, connection_end_point=None):  # noqa: E501
        """TapiConnectivityRoute - a model defined in OpenAPI

        :param name: The name of this TapiConnectivityRoute.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param local_id: The local_id of this TapiConnectivityRoute.  # noqa: E501
        :type local_id: str
        :param connection_end_point: The connection_end_point of this TapiConnectivityRoute.  # noqa: E501
        :type connection_end_point: List[TapiConnectivityConnectionEndPointRef]
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'local_id': str,
            'connection_end_point': List[TapiConnectivityConnectionEndPointRef]
        }

        self.attribute_map = {
            'name': 'name',
            'local_id': 'local-id',
            'connection_end_point': 'connection-end-point'
        }

        self._name = name
        self._local_id = local_id
        self._connection_end_point = connection_end_point

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityRoute':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.Route of this TapiConnectivityRoute.  # noqa: E501
        :rtype: TapiConnectivityRoute
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiConnectivityRoute.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiConnectivityRoute.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiConnectivityRoute.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiConnectivityRoute.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def local_id(self):
        """Gets the local_id of this TapiConnectivityRoute.

        none  # noqa: E501

        :return: The local_id of this TapiConnectivityRoute.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this TapiConnectivityRoute.

        none  # noqa: E501

        :param local_id: The local_id of this TapiConnectivityRoute.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def connection_end_point(self):
        """Gets the connection_end_point of this TapiConnectivityRoute.

        none  # noqa: E501

        :return: The connection_end_point of this TapiConnectivityRoute.
        :rtype: List[TapiConnectivityConnectionEndPointRef]
        """
        return self._connection_end_point

    @connection_end_point.setter
    def connection_end_point(self, connection_end_point):
        """Sets the connection_end_point of this TapiConnectivityRoute.

        none  # noqa: E501

        :param connection_end_point: The connection_end_point of this TapiConnectivityRoute.
        :type connection_end_point: List[TapiConnectivityConnectionEndPointRef]
        """

        self._connection_end_point = connection_end_point
