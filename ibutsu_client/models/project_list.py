# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ibutsu_client.configuration import Configuration


class ProjectList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'projects': 'list[Project]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'projects': 'projects',
        'pagination': 'pagination'
    }

    def __init__(self, projects=None, pagination=None, local_vars_configuration=None):  # noqa: E501
        """ProjectList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._projects = None
        self._pagination = None
        self.discriminator = None

        if projects is not None:
            self.projects = projects
        if pagination is not None:
            self.pagination = pagination

    @property
    def projects(self):
        """Gets the projects of this ProjectList.  # noqa: E501


        :return: The projects of this ProjectList.  # noqa: E501
        :rtype: list[Project]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ProjectList.


        :param projects: The projects of this ProjectList.  # noqa: E501
        :type: list[Project]
        """

        self._projects = projects

    @property
    def pagination(self):
        """Gets the pagination of this ProjectList.  # noqa: E501


        :return: The pagination of this ProjectList.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ProjectList.


        :param pagination: The pagination of this ProjectList.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectList):
            return True

        return self.to_dict() != other.to_dict()
