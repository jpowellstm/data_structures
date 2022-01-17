# data_structures
Building Stacks and Queues in Python

The files in this repository detail how we can build up the data structures for an array, stack and queue from the basic dat structures that python has. It uses an object oriented apprach covering concepts such as inheritance. The following is a summary of the files.

### Create the basic array class

files: myarray_1.py

Create the MyArray class with a constructor method. At the moment this is a
one dimensional array. The class takes as input a number i for the size of the
array and a string that specifies the type as either an integer or a character.
The constructor metho sets the variables i and array_type and also creates an
empty list to hold the array elemnets. The array is then populated with None
values. We test there are no errors by creating an instance of the array.

### Add a method to check type of array

files: myarray_2.py

Add a helper method called check_type to check a value is of the correct type.
For example to check a number is an integer between 0 and 255. This method will
be used later when we add values to the array. A few tests have been added below.


### Add an input method

files: myarray_3.py

In order to populate our arrays we need an input method. This method takes as
a paraeter a list of values. It fist checks whether the length of this list is
the correct length for the array. It then checks that the type of each value
in the list is correct for the type of the array. If both of these are true then
it will populate the array. I have not included any tests at the the end of this
file. They will be included i the next iteration.


### Start using proper tests

files: test_array_3.py

Start using the unittest library to run tests. Each set of sets will be defined
as a class. Each class will have a method to set up what it needs to perform
the tests. For example, a populated array. We are testing that we cannot enter
incorrect data types or an incorrect array size. The version number on this file
matches the version number on the myarray file.

### Add a method to calculate the size of an array

files: array_4.py, test_array_4.py

Add a function that calculates the size of the array in bytes. The type of
the array is taken in to consideration when doing this. Add a class to the test
file to test the size of the array function.

### Add a print method

files: array_5.py

Add a method to print out the array. We won't bother writing any tests for this.






