#!/usr/bin/env python3
"""
test file
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class that tests the acess to nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
