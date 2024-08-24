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
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected value"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload
        url = "https://api.github.com/orgs/google/repos"
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value=url,
        ) as mock_repos_url:
            test_class = GithubOrgClient("google")
            result = test_class.public_repos()
            self.assertEqual(result, [repo["name"] for repo in mock_payload])
            mock_get_json.assert_called_once_with(url)
            mock_repos_url.assert_called_once()

    @parameterized.expand(
        [
            ({'license': {'key': 'my_license'}}, 'my_license', True),
            ({'license': {'key': 'license_2'}}, 'my_license', False),
            ({'license': {'key': 'license_3'}}, 'another_license', False),
            ({'license': {}}, 'my_license', False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected value"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.has_license(repo, license_key), expected)
        self.assertEqual(test_class.has_license, GithubOrgClient.has_license)
