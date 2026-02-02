'''
Problem 14: Increasing Letter Triangle Pattern

Expected Output: 
A
A B
A B C
A B C D 
A B C D E
'''

#Code: 
N = 5
for i in range(1, N + 1):           #Number of Rows
    for j in range(0, i):           #Elements in each row
        print(chr(65 + j),end=" ")  #Logic to print the characters
    print()                         #Move to next line