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
for i in range(0, N):           #Number of rows
    for j in range(0, N):       #Stars per row
        print("*",end = " ")    #Stars in the same row
    print()                     #Move to next row
