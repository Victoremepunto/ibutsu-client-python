# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ibutsu_client
from ibutsu_client.models.widget_type_list import WidgetTypeList  # noqa: E501
from ibutsu_client.rest import ApiException

class TestWidgetTypeList(unittest.TestCase):
    """WidgetTypeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WidgetTypeList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.widget_type_list.WidgetTypeList()  # noqa: E501
        if include_optional :
            return WidgetTypeList(
                types = [
                    {"id":"jenkins-heatmap","title":"Jenkins Pipeline Heatmap","description":"A heatmap of test runs and trends from a Jenkins pipeline","params":[{"name":"job_name","description":"The Jenkins job name","type":"string"},{"name":"builds","description":"The number of Jenkins builds to analyze","type":"integer"},{"name":"group_field","description":"The field in a result to group by","type":"string"},{"name":"sort_field","description":"The field to sort results by","type":"string"}]}
                    ], 
                pagination = {"page":2,"pageSize":25,"totalPages":10,"totalItems":243}
            )
        else :
            return WidgetTypeList(
        )

    def testWidgetTypeList(self):
        """Test WidgetTypeList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
