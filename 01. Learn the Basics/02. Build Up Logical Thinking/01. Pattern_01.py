'''
Problem: Pattern - 1: Rectangular Star Pattern

Expected Pattern:- 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

#Code
N = 5
for i in range(0, N):
    for j in range(0, N):
        print("*",end = " ")
    print()
