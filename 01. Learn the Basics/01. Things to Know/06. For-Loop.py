#Python For Loops
'''
Python for loops are used for iterating over sequences like lists, tuples, strings and ranges. 
'''
'''
-> A for loop allows you to apply the same operation to every item within the loop.
-> Using a for loop avoids the need to manually manage the index.
-> A for loop can iterate over any iterable object, such as a dictionary, list or custom iterator.
'''
#Example:
s = ['This','Repo', 'Belongs', 'To', 'Medhaj']
for i in s:
    print(i)

#Using range() with for loop. 
for i in range(0 , 10, 2):
    print(i)

#Control Statements with For Loop.
'''
Loop control statements change execution from their normal sequence.
When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
Python supports the following control statements.
'''

#Continue with For Loop
for i in 'MedhajSarang':
    if i == 'h' or i == 'r':
        continue
    print(i)

#Break with For Loop
for i in 'MedhajSarang':
    if i == 'j':
        break
print(i)

#Pass Statement with For Loop
'''
The pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.
'''

#Else Statement with For Loop
for i in range(1, 4):
    print(i)
else: 
    print("No Break\n")

#Using Enumerate with for loop
'''
In Python enumerate() function is used with the for loop to iterate over an iterable while also keeping track of index of each item.
'''
li = ['eat', 'sleep', 'repeat']
for i, j in enumerate(li):
    print(i , j)

#Nested For Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

