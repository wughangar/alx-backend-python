#!/usr/bin/env python3
"""
4. Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    test class for client file
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        method to test the class
        """
        expected_value = {"id": "281472839687280"}

        mock_response = Mock()
        mock_response.json.return_value = expected_value

        mock_get_json.return_value = mock_response

        github_org_client = GithubOrgClient(org_name)
        result = github_org_client.org()
        api_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(api_url)
