#!/usr/bin/env python3
"""
4. Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import MagicMock
from typing import Dict
from parameterized import parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    test class for client file
    """

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
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

    def test_public_repos_url(self):
        """
        test method for public repos url
        """
        k_payload = {"repos_url": "https://api.github.com/orgs/someorg/repos"}
        with patch("client.GithubOrgClient.org") as mock_org:
            mock_org.return_value = k_payload
            github_org_client = GithubOrgClient("someorg")
            expected_repos_url = "https://api.github.com/orgs/someorg/repos"

    @patch("client.get_json")
    @patch(
        "client.GithubOrgClient._public_repos_url",
        new_callable=unittest.mock.PropertyMock,
    )
    def test_public_repos(
            self,
            mock_public_repos_url: MagicMock,
            mock_get_json: MagicMock
            ) -> None:
        known_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_public_repos_url.return_value = "https://api.github.com/orgs/someorg/repos"
        mock_get_json.return_value = known_payload
        github_org_client = GithubOrgClient("someorg")
        repos = github_org_client.public_repos()
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()
        expected_repos = ["repo1", "repo2"]
        self.assertEqual(repos, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: Dict,
            license_key: str,
            expected_result: bool):
        github_client = GithubOrgClient("org_name")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)
