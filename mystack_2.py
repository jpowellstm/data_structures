"""
Before we can write the push and pop methods we need to add some helper methods.
size returns the current size of the stack. isEmpty returns true if the stack
contains at least one value.

"""

from myarray_5 import MyArray

class MyStack(MyArray):
    def __init__(self, max_size, stack_type):
        MyArray.__init__(self, max_size, stack_type)
        self.stack_size = -1
        self.max_size = self.i

    def height(self):
        return self.stack_size + 1

    def isEmpty(self):
        return self.stack_size < 0


