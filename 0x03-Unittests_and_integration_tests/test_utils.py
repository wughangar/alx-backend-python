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
from utils import memoize


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
        # type: (str, Dict)  -> None:
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


class TestMemoize(unittest.TestCase):
    """
    class to test memoize
    """

    class TestClass:
        """ test class"""

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        test_obj = self.TestClass()

        with patch.object(test_obj, 'a_method') as mock_a_method:
            result_1 = test_obj.a_property()
            result_2 = test_obj.a_property()

            mock_a_method.assert_called_once()
            self.assertEqual(result_1, result_2)
