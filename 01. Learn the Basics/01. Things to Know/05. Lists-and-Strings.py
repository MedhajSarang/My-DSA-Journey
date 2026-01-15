#Python Lists

'''
A list is a built-in data structure that can hold an ordered collection of items.
-> Can contain duplicate items.
-> Items can be modified, replaced or removed. 
-> Items are accessed using their position.
-> Can store mixed data types.
'''

#Creating a list
a = [1, 'Hello', 3.14, True]
print(a)

#Using list Constructor
b = list((1, 2, 3, 'apple', 4.5))
print(b)

#Creating list with Repeated Elements
c = [2]*7
print(c)

#Accessing List Elements
d = [10, 20, 30, 40, 50]
print(d[2])
print(d[-1])
print(d[1:4])

#Adding Elements into List
e = []

e.append(10)

e.insert(0,20)

e.extend([30, 40, 50])

print(e)

#Updating Elements into List
f = [10,20,30,40,50]
f[1] = 60
print(f)

#Removing Elements from List
g = [10,20,30,40,50]

g.remove(30)

pop_val = g.pop(1)

del g[0]

print(g)

#Iterating Over Lists
h = ['apple', 'banana', 'cherry']
for item in h:
    print(item)

#Nested Lists
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][2])

#List Comprehension
'''
It is a concise way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list of range.
'''
squares = [x**2 for x in range(1, 6)]
print(squares)

