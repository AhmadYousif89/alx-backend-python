#!/usr/bin/env python3
"""
Unit tests for the utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)]
    )
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception
    ):
        """Test access_nested_map function with exception"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, payload):
        """Test get_json function"""
        mock = Mock()
        mock.json.return_value = payload
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """Test memoize decorator functionality."""

    def test_memoize(self):
        """Test memoize function."""

        class TestClass:
            """Test class"""

            def a_method(self):
                """A method"""
                return 42

            @memoize
            def a_property(self):
                """A property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_obj = TestClass()

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
