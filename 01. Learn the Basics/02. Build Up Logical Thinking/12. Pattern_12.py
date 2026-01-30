'''
Problem 12:- Number Crown Pattern

Expected Output:- 
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1 
'''

#Code
N = 5
for i in range(1, N):               #Determine the number of rows
    for j in range(1, i + 1):
        print(j, end=" ")
    for s in range(2 * (N - 1) + 1):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()
  