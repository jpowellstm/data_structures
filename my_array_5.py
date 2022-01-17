"""
Add a method to print out the array. We won't bother writing any tests for this.
"""

class MyArray:
    def __init__(self, i, array_type):
        """Allowed types
             - int8: 8 bit signed integer 0 - 2^8 -1
             - char: a single character
        """
        self.array = []
        self.i = i
        self.array_type = array_type

        for _ in range(self.i):
            self.array.append(None)

    def check_type(self, value):
        if self.array_type == 'int8':
            return isinstance(value ,int) and 0 < value < 255

        elif self.array_type == 'char':
            return isinstance(value, str) and len(value) == 1

    def input(self, values):
        if len(values) != self.i:
            return 'Incorrect data size'

        for value in values:
            if not self.check_type(value):
                return 'Incorrect data type'

        for i in range(self.i):
            self.array[i] = values[i]

    def size(self):
        if self.array_type == 'int8':
            return self.i*8

        elif self.array_type == 'char':
            return self.i*4

        else:
            return "Incorrect type"

    def my_print(self):
        for value in self.array:
            print(value)
