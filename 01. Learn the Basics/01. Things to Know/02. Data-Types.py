'''Data types in Python are a way to classify data items.'''

#The following are standard or built-in data types in Python: 

'''
Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview
'''

# 01. Numeric Data Types
'''
Python numbers represent data that has a numeric value. A numeric value can be an integer, 
a floating number or even a complex number. These values are defined as int, float and complex classes.
'''

a = 5 
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# 02. Sequence Data Types
'''
A sequence is an ordered collection of items, which can be of similar or different data types. 
Sequences allow storing of multiple values in an organized and efficient fashion. 
There are several sequence data types of Python.
'''

s = 'Welcome to this repository'
print(s)
print(type(s))

# 2.1. List Data Type
'''
Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items. 
It is very flexible as items in a list do not need to be of the same type.
'''

d = []
d = ["Medhaj", "Sarang", 18, 11, 3]
print(d)

# 2.2. Tuple Data Type
'''
Tuple is an ordered collection of Python objects. 
The only difference between a tuple and a list is that tuples are immutable. 
Tuples cannot be modified after it is created.
'''

tup1 = ('Medhaj', 'Sarang')
print(tup1)

# 03. Boolean Data Type
'''
Boolean Data type is one of the two built-in values, True or False. 
Boolean objects that are equal to True are (true) and those equal to False are (false). 
However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false.
'''

print(type(True))
print(type(False))

# 04. Set Data Type
'''
In Python Data Types, Set is an unordered collection of data types that is iterable, 
mutable and has no duplicate elements. The order of elements in a set is undefined 
though it may consist of various elements.
'''

s1 = set(["Hello","How","Are","You"])
print("Set with the use of list: ", s1)

# 05. Dictionary Data Type
'''
A dictionary in Python is a collection of data values, used to store data values like a map,
 unlike other Data Types, a dictionary holds a key: value pair. Key-value is provided in dictionary to make it more optimized. 
 Each key-value pair in a dictionary is separated by a colon :, whereas each key is separated by a 'comma'.
 '''

d = {}

d = {1: 'Hello', 2: 'World'}
print(d)

# 5.1 Creating a dictionary using dict() constructor

d1 = dict({1: 'Hello', 2: 'World'})
print(d1)

