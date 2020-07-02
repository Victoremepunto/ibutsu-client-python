# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ibutsu_client
from ibutsu_client.api.artifact_api import ArtifactApi  # noqa: E501
from ibutsu_client.rest import ApiException


class TestArtifactApi(unittest.TestCase):
    """ArtifactApi unit test stubs"""

    def setUp(self):
        self.api = ibutsu_client.api.artifact_api.ArtifactApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_artifact(self):
        """Test case for delete_artifact

        Delete an artifact  # noqa: E501
        """
        pass

    def test_download_artifact(self):
        """Test case for download_artifact

        Download an artifact  # noqa: E501
        """
        pass

    def test_get_artifact(self):
        """Test case for get_artifact

        Get a single artifact  # noqa: E501
        """
        pass

    def test_get_artifact_list(self):
        """Test case for get_artifact_list

        Get a (filtered) list of artifacts  # noqa: E501
        """
        pass

    def test_upload_artifact(self):
        """Test case for upload_artifact

        Uploads a test run artifact  # noqa: E501
        """
        pass

    def test_view_artifact(self):
        """Test case for view_artifact

        Stream an artifact directly to the client/browser  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
