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
