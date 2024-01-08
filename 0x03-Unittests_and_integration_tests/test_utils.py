#!/usr/bin/env python3
"""
test file
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
from typing import Dict, Mapping, Sequence, Tuple, Union
from unittest.mock import patch
from unittest.mock import Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    class that tests the acess to nested map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected_result: Union[Dict, int]) -> None:
        """
        method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, exception: Exception
    ) -> None:
        """
        method that testsd access to nested map exception
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    class to test test_get_json method
    """
    @patch('utils.requests.get')
    @patch('utils.get_json')
    def test_get_json(self, mock_get_json, mock_requests_get):
        # type: (Mock, Mock)  -> None:
        """
        mock function to test getting urls
        """
        test_cases = [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
                ]
        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_requests_get.return_value = mock_response

            result = get_json(test_url)
            mock_requests_get.assert_called_with(test_url)
            self.assertEqual(result, test_payload)
