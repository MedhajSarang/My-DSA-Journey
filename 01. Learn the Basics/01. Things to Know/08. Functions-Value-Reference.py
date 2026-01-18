#Functions

'''
Functions are blocks of reusable code defined using def and are used to perform a specific task. 
You pass data to a function using arguments, and Python handles them using an object-reference model.
'''

#Pass by Value v/s Pass by Reference in Python:

'''
Python is often described as pass by object reference.
For immutable objects (int, float, string, tuple), changes inside the funtion do not affect the original variable. 
For mutable objects (list, dictionary, set), changes inside the function do affect the original object - this feels like pass by reference.
'''

#Code: 

def change_num(x):
    x = 10

def change_list(lst):
    lst.append(4)

a = 5

nums = [1, 2, 3]

change_num(a)
change_list(nums)

print(a)
print(nums)

#Summary
'''
Immutable -> Behaves like pass by value.
Mutable -> Behaves like pass by reference.
'''