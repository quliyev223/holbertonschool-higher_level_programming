#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max is at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_at_end(self):
        """Test when the max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_one_element_list(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 0, 4, -5]), 4)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_duplicates(self):
        """Test a list with duplicate max values"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_strings_in_list(self):
        """Test list with non-integer values should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

if __name__ == '__main__':
    unittest.main()

