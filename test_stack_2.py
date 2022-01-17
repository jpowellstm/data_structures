import unittest
from mystack_2 import MyStack


class TestStackInput(unittest.TestCase):

    def setUp(self):
        self.my_empty_stack = MyStack(3, 'int8')

    def test_incorrect_data_char(self):
        self.assertEqual(self.my_empty_stack.input(['a',2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_float(self):
        self.assertEqual(self.my_empty_stack.input([3.2, 2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_big(self):
        self.assertEqual(self.my_empty_stack.input([3.2, 2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_negative(self):
        self.assertEqual(self.my_empty_stack.input([3, -2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_edge(self):
        self.assertEqual(self.my_empty_stack.input([0, -2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_size(self):
        self.assertEqual(self.my_empty_stack.input([5, -2, 1, 4]), 'Incorrect data size', "Should be Incorrect data size")


if __name__ == '__main__':
    unittest.main()

