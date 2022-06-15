## Computing in Schools: Building Data Structures with OOP

A big part of the A-level Computing syllabus has content on different data types. Arrays, stacks, queues, linked lists, graphs and trees to name a few. Another aspect of the syllabus is [object orientated programming](https://www.educative.io/blog/object-oriented-programming). In this post I aim to use an object oirentated approach to build some of these data structures from scratch. I will be using Python as a programming language. All data structures will be built up from the basic data structures that python contains, i.e., lists, strings and integers. I will also be adding in a few software engineeing practices such as [unit testing](https://realpython.com/python-testing/), [linting](https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it), using [test runners](https://realpython.com/python-testing/),  and task runners. This post is not inteded to be a tutorial on Object Orientated Programming (OOP) or data structures. It is more an illustration of how OOP principles can be applied using structures that should be famiuliar to an A-level computing student. I have written a priliminary activity to this one using shapes as a concept.

This is a summary of all that will be covered

- Creating data structures for an Array, Stack and Queue
- Using Classes
- Inheritance
- Encapsulation 
- Magic methods 
- Writing tests using Unittest library
- Using a test runner
- Using a task runner
- The concept of [refactoring](https://www.techtarget.com/searchapparchitecture/definition/refactoring)
- Linting
- [Code Coverage](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage)

All resources will be hosted on my Github page. There is a table at the bottom of this post detailing which files are needed for each section of the tutorial.

### 0. Setting up our environment
A will be using a Linux based envirnment for much of this task. In school I would use [pythonanywhere](https://www.pythonanywhere.com/) which gives us an IDE for editing python code and a bash shell for running the code and any tests etc. This is by far the easiest option and has the advantage of working wherever you have access to a web browser. If you are on windows you might consider using the windows subsystem for linux. 

### 1. Creating the basic array class
We create the MyArray class with a constructor method (in python this is `__init__()`).  The constructor takes as input a number `given_i` (at the moment this is a one dimensional array) for the size of the array and a string `given_array_type` that specifies the type as either an 8 bit integer or a character. The constructor method sets the attributes 'i'and 'array_type' and also creates an empty list `array` to hold the array elements. The array is then populated with `None` values. We then run some tests by creating instances of the `MyArray` class to make sure there are no errors.  

```
class MyArray:
    def __init__(self, given_i, given_array_type):
        """Allowed types
             - int8: 8 bit unsigned integer 0 - 2^8 -1
             - char: a single character
        """
        self.i = given_size
        self.array_type = given_array_type
        self.array = []

        for _ in range(self.size):
            self.array.append(None)


print("""
Conduct Tests
________________________________________________________________________
""")
print("Check we can create a class, there should be no errors")
array_1 = MyArray(1,'int8')
array_2 = MyArray(5,'char')
```

In the bash console run the command `python3 my_array_1.py` to test the code.

In part 4 of this post the tests will be moved into a separate file and run separately.

Note that I am going to use a naming convention whereby all variable names passed into a function will be prefixed with the word "given". For example `given_i` is passed to the constructor so it can create the attribute `i`. In practice I would probably just use the same name for both, but the exam mark schemes seem to prefer different names.

### 2. Add a method to check the type of the array
We add a helper method called check_type. The method takes as input a value and then checks if this value is the same type as the array otherwise it returns `False`. The `isinstance()` function returns `True` if the value is of the specified type. Note that we have added a extra condition to check that an int8 type is of between 0 and 255 and a char type is of length 1. This method will be used later when we add values to the array.

```
def check_type(self, value):
        if self.array_type == 'int8':
            return isinstance(value, int) and 0 < value <= 255

        elif self.array_type == 'char':
            return isinstance(value, str) and len(value) == 1
        else:
            return False
```

A few tests have been added below. Notice that we have written some valid, invalid and edge case tests. Also not that we don't get very good feedback from the tests. This will be fixed when introduce proper test runners in section 4. 

```
print("Check the check_type function works correctly")
print(array_1.check_type(1))
print(array_1.check_type(0.5))
print(array_1.check_type(280))
print(array_1.check_type(255))
print(array_1.check_type(0))

print(array_2.check_type("a"))
print(array_2.check_type(0.5))
print(array_2.check_type("hello"))
```

### 3. Add an input method
In order to populate our arrays we need to add an input method to the MyArray class. This method takes as a parameter a list of values. It fist checks whether the length of this list is the correct length for the array. It then checks that the type of each value in the list is correct for the type of the array. If both of these are true then it will populate the array. I have not included any tests at the the end of this file. They will be included in the next iteration.

```
def input(self, values):
        if len(values) != self.size:
            return 'Incorrect data size'

        for value in values:
            if not self.check_type(value):
                return 'Incorrect data type'

        for index in range(self.self.size):
            self.array[index] = values[index]
```

### 4. Start using proper tests
Having all the tests at the bottom of the file is not an ideal practice. We will now remove these. We do not want to be running tests when we are using our Classes. Putting tests into a separate file and runnning them independently would be superior. We will start using the unittest library to run tests. Each set of tests will be defined as a class in a separate test file. Each class will have a `setUp()` method to create what it needs to perform the tests. For example, to instantiate an object for an array and populate it. We are testing that we cannot enter incorrect data types or an incorrect array size. Note that the name of each method within the class is descriptive of what the test performs. We are using the `assertEqual()` function which takes three parameters. The first two parameters need to be the same for the test to pass otherwise a message is printed (the third parameter).  

```
import unittest
from my_array_4 import MyArray

class TestArrayInput(unittest.TestCase):

    def setUp(self):
        self.my_empty_array = MyArray(3, 'int8')
        self.my_full_array = MyArray(3, 'int8')
        self.my_full_array.input([3 ,2, 1])

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

    def test_incorrect_data_correct(self):
        self.assertEqual(self.my_full_array.array, [3, 2, 1] , "Should be [3, 2, 1]")


if __name__ == '__main__':
    unittest.main()
```

To run these tests enter the command `python3 test_array_1.py` in bash. You should see something like:
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
```

Note that in this step we haven't really added any functionality to our code. What we have done is "refactored" it. This is the porocess of making changes to our code to make it "better". This could be more readable, faster, more robust. In this case adding a better system for running tests. As we add more functionality to our array class we will add more tests. 

### 5. Add a method to calculate the size of an array
We add a function that calculates the size of the array in bytes. The type of the array is taken in to consideration when doing this. We add a class to the test file to test the size of the array function.

```
def size(self):
        if self.array_type == 'int8':
            return self.i*8

        elif self.array_type == 'char':
            return self.i*4

        else:
            return "Incorrect type"
```

We add a test class to the test file as follows:

```
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
```
### 6. Add a print method
Add a method to print out the array. We won't bother writing any tests for this.
```
def my_print(self):
    for value in self.array:
        print(value)
```

### 7. Encaspulation
Before we go too much further, now woould be a good time to talk about encapsualtion as shortly we will have multiple classes inheriting from each other. In python adding a double underscore before an attribute or method name makes it inaccessible from outside of the class. If other classes need to access or change a protected variable they would need to do iut through a getter or setter method.

The underscore is used as an index in the for loop instead of a variable name as it will not be used within the loop. This prevents python from creating variables that are not used. We modify the `array` attribute within the constructor method to be private as we don't want any other classes to be able to modify it directly. This should be done through the `input()` method for example.

```
class MyArray:
    def __init__(self, i, array_type):
        """Allowed types
             - int8: 8 bit unsigned integer 0 - 2^8 -1
             - char: a single character
        """
        self.__array = []
        self.i = i
        self.array_type = array_type

        for _ in range(i):
            self.__array.append(None)
```
Note that all references to `array` attribute need to be modified to `__array` within the class. This is another example of refactoring our code.

### 8. Create a Stack Class
Create a Stack structure that inherits from an Array. We need to run the constructor for the Array. Relabel the size of the array as max_size and set the current size of the stck to be -1 for empty. The stack will not always take up the full size of the array. We add an atribute called structure that tells us we are dealing with a stack. This will be useful in future when we inherit from the Stack class to create a Queue.

```
from my_array_7 import MyArray

class MyStack(MyArray):
    def __init__(self, max_size, stack_type):
        MyArray.__init__(self, max_size, stack_type)
        self.stack_size = -1
        self.max_size = self.i
        self.structure = "stack"
```
We create a test file for the stack and run it with `python3 test_stack_1.py`

```
import unittest
from my_stack_1 import MyStack

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
```

### 9. Using a test runner
We now have multiple files and testfiles in our project so it will be useful to organise everything and employ the use of a test runner. A test runner is a programme that takes charge of running the tests and will add some functionality which you will see shortly. I am going be using nose which you might need to install with the command `pip3 install --user nosetests`. Before running tests we will put all of the older files into an archive directory so the only files we will have in our current directory at this point will be my_array_7.py, my_stack_1.py, test_array_2.py and test_stack_1.py. We can run all of our tests with `nosetests -v  --no-byte-compile`

The `-v` option makes the output more verbose, i.e., we get more information
The `--no-byte-compile` prevents nosetests from producing lots of .pyc files that get in the way. 

You should see something like the following output

```
test_incorrect_data_big (test_array_2.TestArrayInput) ... ok
test_incorrect_data_char (test_array_2.TestArrayInput) ... ok
test_incorrect_data_correct (test_array_2.TestArrayInput) ... ERROR
test_incorrect_data_edge (test_array_2.TestArrayInput) ... ok
test_incorrect_data_float (test_array_2.TestArrayInput) ... ok
test_incorrect_data_negative (test_array_2.TestArrayInput) ... ok
test_incorrect_data_size (test_array_2.TestArrayInput) ... ok
test_correct_char_size (test_array_2.TestArraySize) ... ok
test_correct_int_size (test_array_2.TestArraySize) ... ok
test_incorrect_data_big (test_stack_1.TestStackInput) ... ok
test_incorrect_data_char (test_stack_1.TestStackInput) ... ok
test_incorrect_data_edge (test_stack_1.TestStackInput) ... ok
test_incorrect_data_float (test_stack_1.TestStackInput) ... ok
test_incorrect_data_negative (test_stack_1.TestStackInput) ... ok
test_incorrect_data_size (test_stack_1.TestStackInput) ... ok
======================================================================
ERROR: test_incorrect_data_correct (test_array_2.TestArrayInput)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jpowell/Alevel/data_structures/version2/test_array_2.py", line 30, in test_incorrect_data_correct
    self.assertEqual(self.my_full_array.array, [3, 2, 1] , "Should be [3, 2, 1]")
AttributeError: MyArray instance has no attribute 'array'
----------------------------------------------------------------------
Ran 15 tests in 0.043s
FAILED (errors=1)
```

The test `test_incorrect_data_correct` from the file test_array_2.TestArrayInput has failed. 

If we look at the error message we can see that  `AttributeError: MyArray instance has no attribute 'array'` This is because we have made the attribute `array` private in the array class by giving it the double underscore. We have a few options to fix this test. We could add a getter method to the array class to access the array attribute and refactor the test to use this method. However, we don't really want or need the class to have a getter method. Maybe the best thing to do is remove this test as it is now not testing any functionality we can make use of. 

### 10. Methods to calculate the size/height of the stack
Before we can write push and pop methods for the stack we need to add some helper methods. `height()` returns the current size(height) of the stack. `isEmpty` returns true if the stack contains at least one value.

```
def height(self):
        return self.stack_size + 1
        
def isEmpty(self):
    return self.stack_size < 0
```

### 11. Adding push and pop methods
We add methods for push, pop and top. Push should put a value on to the top of the stack. Pop should remove a value from the top of the stack and return it. Top should return the value from the top of the stack without removing it.

```
def push(self, value):
    if self.stack_size + 1 == self.max_size:
        return(self.structure, 'is full')
    else:
        self.stack_size += 1
        self.stack.append(value)

def pop(self):
    if self.isEmpty():
        return(self.structure, 'is empty')
    else:
        temp = self.stack[self.stack_size]
        del self.stack[-1]
        self.stack_size -=1
        return temp

def top(self):
    if self.isEmpty():
        return(self.structure, 'is empty')
    else:
        return self.stack[-1]        
```

### 12. Adding magic methods
We add some magic methods to allow stacks to perform as normal data structures in python. For example if we create two stacks S1 and S2 that are the same and ask python S1 == S2 then we should get the reult True. This is performed by the `__eq__` method. If we perform `str(S1)` then `__str` will deal with this.

```
def __str__(self):
    output = [str(x) for x in self.stack]
    return ','.join(output)


def __eq__(self, other):
    if self.max_size != other.max_size:
        return False

    for i, j in zip(self.stack, other.stack):
        if i != j:
            return False
    return True
```


### 13. Linting our code
There are many different ways in which a programmer code structure their code. For example, they could use 2 spaces or 4 spaces for indentation. They could leave a space after a comma or not. They could capitalise class names or not etc, etc. In 2001 Guido van Rossum created a style guide for python and published it as PEP8. PEP's or Python Enhancement Proposals are documents people write to suggest changes to the language. The Python comunnity will then need to decide on whether to accept the proposal or not. PEP8 focuses on descibing certain rules on how python code should be written and it is now what most software engineers adopt as standard. This helps when multiple people are working on the same project or when programmers are reading a code that is not thiers. A linter is a programme that checks your code against the rules of PEP8 and produces a report offering suggestions. We are going to use a linter called flake8. We might need to install this first using `pip3 install --user flake8`. Then we can run flake8 on all the python files in our directory with the command `flake8 *.py`. We will then get a list of all the things in our files that do not follow the PEP8 rules. You might notice lots of the same the same things. For example 

```
E231 missing whitespace after ','
E501 line too long (86 > 79 characters)  
E265 block comment should start with '# '
```

You should fix all of these now and run the linter on your code from time to time to check you are following the rules. This has been done to this code base and the files updated to new versions. 

### 14.Setting up a task runner
We now have several commands that we are running on the bash terminal for executing the code, running our linter and running our tests. There might be more as the project grows. It can become awkward to remember what all the commands are for these tasks which is where a task runner comes in handy. I will be using invoke. We create a file called tasks.py and whenever we run `invoke "command name"` invoke will look in the file tasks.py for the command name and run it. So then all we need to remember is the name of the tasks to be run. 

Firstly we import the commands we need from the invoke library. The to create a task we simmply define a function and put the decorator `@task` on the line above it. 

```
from invoke import task, run

@task
def hello(ctx):
    print("Hello world!")
```

So now when we run `invoke hello' on the command line it should print "Hello world!" Note the ctx variable that the function takes as an input is a "context". Do not worry about this, it's just some thing the library needs. This isn't very usefull so now lets write some more. I will use the same basic structure for all tasks

```
@task
def template(ctx):
    cmd = []
    cmd.append("bash syntax for command 1")
    cmd.append("bash syntax for command 2")
    cmd.append("bash syntax for command 3")
    # as many commands as you want to run

    for command in cmd:
        run(command, hide=False, warn=False)
```

This is the task for running a linter

```
@task
def lint(ctx):
    cmd = []
    cmd.append("flake8 *.py ")

    for command in cmd:
        run(command, hide=False, warn=False)
```

A task for running our tests.

```
@task
def test(ctx):
    cmd = []
    cmd.append("clear")
    cmd.append("nosetests -v --rednose --with-coverage")

    for command in cmd:
        run(command, hide=False, warn=False)
```

A function (not a task) to print out a divider

```
def star_line(comment):
    print()
    print('*'*60)
    print(comment)
    print('*'*60)
    print()
```

A task for cleaning up our directory.

```
@task
def clean(ctx):
    cmd = []
    cmd.append("bash syntax for command 1")

    for command in cmd:
        run(command, hide=False, warn=False)
```

A task for performing a fulltest which runs unit tests and lints the code.

```
@task
def fulltest(ctx):
    clean(ctx)
    star_line('Running Unit Tests')
    test(ctx)
    star_line('Linting Code')
    lint(ctx)
```

### 15. Testing with coverage
```
nosetests -v --with-coverage --no-byte-compile
```

### 16. Adding a Queue class


### List of files required for each section
| Section Number | File | Test File |
| -------------- | ---- | --------- |
|1| my_array_1.py |                 |
|2| my_array_2.py |                 |
|3| my_array_3.py |                 |
|4| my_array_4.py | test_array_1.py |
|5| my_array_5.py | test_array_2.py |
|6| my_array_6.py |                 |
|7| my_array_7.py |                 |
|8| my_stack_1.py |test_stack_1.py  |                               
|9| my_array_7.py, my_stack_1.py | test_array_2.py, test_stack_1.py |
|10| my_array_7.py, my_stack_2.py | |
|11| my_array_7.py, my_stack_3.py | test_stack_2.py|
|12|  | |
|13|  | |
|14|  | |

### To do
- add links to websites
- a discussion about encapsulation
- installing nosetests on pythonanywhere
- include a section on invoke.
- Extend to linked lists, trees etc?


