'''
Problem 11:- Binary Number Triangle Pattern

Expected Output:- 

1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

#Code
N = 5
for i in range(N):              #Number of rows
    if i % 2 == 0:              #Decides the number by which the row should start
        start = 1               
    else:
        start = 0
    for j in range(i + 1):      #Determines the number that are printed in each row
        print(start, end=" ")   #Print the current value of start
        start = 1 - start       #Flip between 1 and 0 after each print execution
    print()                     #Move to next row