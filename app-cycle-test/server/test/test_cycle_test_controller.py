# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from server.models.cycle_test_info import CycleTestInfo  # noqa: E501
from server.test import BaseTestCase


class TestCycleTestController(BaseTestCase):
    """CycleTestController integration test stubs"""

    def test_add_info(self):
        """Test case for add_info

        Add a new info to the server
        """
        body = CycleTestInfo()
        response = self.client.open(
            '/cycletest',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_info(self):
        """Test case for get_info

        Get the information
        """
        response = self.client.open(
            '/cycletest',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
