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
from ibutsu_client.models.pagination import Pagination  # noqa: E501
from ibutsu_client.rest import ApiException

class TestPagination(unittest.TestCase):
    """Pagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Pagination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.pagination.Pagination()  # noqa: E501
        if include_optional :
            return Pagination(
                page = 2, 
                page_size = 25, 
                total_pages = 10, 
                total_items = 243
            )
        else :
            return Pagination(
        )

    def testPagination(self):
        """Test Pagination"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
