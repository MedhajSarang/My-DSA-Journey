'''
Problem 15: Reverse Letter Triangle Pattern

Expected Output: 
A B C D E
A B C D
A B C
A B
A
'''

#Code

N = 5
for i in range(N):                  #Determines the total number of rows
    for j in range(N - i):          #Determines elements per row
        print(chr(65 + j), end=" ") #Prints characters starting from A in each row
    print()                         #Move to next row