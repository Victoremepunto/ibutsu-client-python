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
from ibutsu_client.models.widget_config import WidgetConfig  # noqa: E501
from ibutsu_client.rest import ApiException

class TestWidgetConfig(unittest.TestCase):
    """WidgetConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WidgetConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.widget_config.WidgetConfig()  # noqa: E501
        if include_optional :
            return WidgetConfig(
                id = 'd41d8cd98f00b204e980', 
                type = 'widget', 
                widget = 'jenkins-heatmap', 
                project = 'my-project', 
                weight = 0, 
                params = {"job_name":"integration_tests","builds":5,"group_field":"metadata.component","sort_field":"starttime"}, 
                title = 'Job Health'
            )
        else :
            return WidgetConfig(
        )

    def testWidgetConfig(self):
        """Test WidgetConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
