'''
Problem 13: Increasing Number Triangle Pattern

Expected Output: 
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

#Code:

N = 5
num = 1                         #Starting number
for i in range(1, N + 1):       #Number of Rows
    for j in range(1, i + 1):   #Elements per row
        print(num, end=" ")     
        num += 1                #Increment the number
    print()                     #Move to next line