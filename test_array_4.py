"""
Add a class to test the size of the array function
"""

import unittest
from myarray_4 import MyArray


class TestArrayInput(unittest.TestCase):

    def setUp(self):
        self.my_empty_array = MyArray(3, 'int8')

    def test_incorrect_data_char(self):
        self.assertEqual(self.my_empty_array.input(['a',2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_float(self):
        self.assertEqual(self.my_empty_array.input([3.2, 2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_big(self):
        self.assertEqual(self.my_empty_array.input([3.2, 2, 300]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_negative(self):
        self.assertEqual(self.my_empty_array.input([3, -2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_edge(self):
        self.assertEqual(self.my_empty_array.input([0, -2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_size(self):
        self.assertEqual(self.my_empty_array.input([5, -2, 1, 4]), 'Incorrect data size', "Should be Incorrect data size")


class TestArraySize(unittest.TestCase):

    def setUp(self):
        self.my_int_array = MyArray(3, 'int8')
        self.my_int_array.input([5 ,2, 1])

        self.my_char_array = MyArray(4, 'char')
        self.my_char_array.input(['a' ,'b', 'c', 'd'])

    def test_correct_int_size(self):
        self.assertEqual(self.my_int_array.size(), 24, "Should be 24")

    def test_correct_char_size(self):
        self.assertEqual(self.my_char_array.size(), 16, "Should be 16")

if __name__ == '__main__':
    unittest.main()
