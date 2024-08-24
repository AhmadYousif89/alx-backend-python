#!/usr/bin/env python3
"""
Unittests for client module
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """

    @parameterized.expand([("google",), ("abc",)])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(test_class.org, mock_get_json.return_value)

    def test_public_repos_url(self):
        """Test that _public_repos_url method returns the expected result"""
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
        ) as mock_org:
            test_class = GithubOrgClient("google")
            self.assertEqual(
                test_class._public_repos_url,
                mock_org.return_value["repos_url"],
            )

    @patch('client.get_json')
    def test_repos_payload(self, mock_get_json):
        """Test that repos_payload returns the expected value"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos",
        ) as mock_repos_url:
            test_class = GithubOrgClient("google")
            result = test_class.repos_payload
            self.assertEqual(result, mock_payload)
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )
            mock_repos_url.assert_called_once()
