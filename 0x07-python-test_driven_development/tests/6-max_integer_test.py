#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test when the list has regular integers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max(self):
        """Test a list with a beginning max value."""
        result = [4, 3, 2, 1]
        self.assertEqual(max_integer(result), 4)

    def test_reverse_order_list(self):
        """Test when the list has integers in reverse order."""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test when the list is empty."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test when the list has a single element."""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_negative_numbers_list(self):
        """Test when the list has negative numbers."""
        result = max_integer([-1, -5, -3, -2])
        self.assertEqual(result, -1)

    def test_mixed_numbers_list(self):
        """Test when the list has mixed positive and negative numbers."""
        result = max_integer([-1, 5, -3, 2])
        self.assertEqual(result, 5)

    def test_float_numbers_list(self):
        """Test when the list has float numbers."""
        result = max_integer([1.5, 3.7, 2.1, 1.0, -9.2, 0.6])
        self.assertEqual(result, 3.7)

    def test_string_elements_list(self):
        """Test when the list has string elements."""
        result = max_integer(["abc", "def", "ghi"])
        self.assertEqual(result, "ghi")

    def test_empty_string(self):
        """Test when the string is empty."""
        result = max_integer("")
        self.assertIsNone(result, None)
