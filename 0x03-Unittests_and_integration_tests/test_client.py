#!/usr/bin/env python3
"""
Unittests for client module
"""

import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient.public_repos method in an integration test.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the test environment by mocking requests.get"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url: str):
            """Return different mock responses based on the URL"""
            mock = Mock()
            if url == cls.org_payload["repos_url"]:
                mock.json.return_value = cls.repos_payload
            else:
                mock.json.return_value = cls.org_payload
            return mock

        cls.mock_get.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down for the test"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test integration for the public repos method"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("404"), [])

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter 'apache-2.0'"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
