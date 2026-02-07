'''
Problem 18: Alpha-Triangle Pattern

Expected Output:
E
D E
C D E
B C D E 
A B C D E
'''

#Code: 

N = 5
for i in range(N):                                          #Number of rows
    for ch in range(ord('A') + N - 1 - i, ord('A') + N):    #Prints elements in each row, from characters A + N - 1 - i to A + N - 1
        print(chr(ch), end=" ")                             #Prints the characters
    print()                                                 #Move to next row