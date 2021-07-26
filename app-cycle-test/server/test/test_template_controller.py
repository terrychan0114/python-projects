# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from server.models.template_info import TemplateInfo  # noqa: E501
from server.test import BaseTestCase


class TestTemplateController(BaseTestCase):
    """TemplateController integration test stubs"""

    def test_add_info(self):
        """Test case for add_info

        Add a new info to the server
        """
        body = TemplateInfo()
        response = self.client.open(
            '/information',
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
            '/information',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_num(self):
        """Test case for get_num

        Get the information of a number
        """
        query_string = [('number', 'number_example')]
        response = self.client.open(
            '/information/number',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_info(self):
        """Test case for update_info

        Update info
        """
        body = TemplateInfo()
        response = self.client.open(
            '/information',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
