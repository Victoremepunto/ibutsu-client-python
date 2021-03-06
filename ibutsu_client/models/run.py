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


class Run(object):
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
        'id': 'str',
        'created': 'str',
        'duration': 'float',
        'source': 'str',
        'start_time': 'float',
        'summary': 'object',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'duration': 'duration',
        'source': 'source',
        'start_time': 'start_time',
        'summary': 'summary',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, created=None, duration=None, source=None, start_time=None, summary=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """Run - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._duration = None
        self._source = None
        self._start_time = None
        self._summary = None
        self._metadata = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if duration is not None:
            self.duration = duration
        if source is not None:
            self.source = source
        if start_time is not None:
            self.start_time = start_time
        if summary is not None:
            self.summary = summary
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this Run.  # noqa: E501

        Unique ID of the test run  # noqa: E501

        :return: The id of this Run.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Run.

        Unique ID of the test run  # noqa: E501

        :param id: The id of this Run.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this Run.  # noqa: E501

        The time this record was created  # noqa: E501

        :return: The created of this Run.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Run.

        The time this record was created  # noqa: E501

        :param created: The created of this Run.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def duration(self):
        """Gets the duration of this Run.  # noqa: E501

        Duration of tests in seconds  # noqa: E501

        :return: The duration of this Run.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Run.

        Duration of tests in seconds  # noqa: E501

        :param duration: The duration of this Run.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def source(self):
        """Gets the source of this Run.  # noqa: E501

        A source for this test run  # noqa: E501

        :return: The source of this Run.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Run.

        A source for this test run  # noqa: E501

        :param source: The source of this Run.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def start_time(self):
        """Gets the start_time of this Run.  # noqa: E501

        The time the test run started  # noqa: E501

        :return: The start_time of this Run.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Run.

        The time the test run started  # noqa: E501

        :param start_time: The start_time of this Run.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def summary(self):
        """Gets the summary of this Run.  # noqa: E501

        A summary of the test results  # noqa: E501

        :return: The summary of this Run.  # noqa: E501
        :rtype: object
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Run.

        A summary of the test results  # noqa: E501

        :param summary: The summary of this Run.  # noqa: E501
        :type: object
        """

        self._summary = summary

    @property
    def metadata(self):
        """Gets the metadata of this Run.  # noqa: E501

        Extra data for this run  # noqa: E501

        :return: The metadata of this Run.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Run.

        Extra data for this run  # noqa: E501

        :param metadata: The metadata of this Run.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

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
        if not isinstance(other, Run):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Run):
            return True

        return self.to_dict() != other.to_dict()
