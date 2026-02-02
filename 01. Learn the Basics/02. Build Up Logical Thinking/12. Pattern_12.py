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
    for j in range(1, i + 1):       #Logic for the left side
        print(j, end=" ")           
    for s in range(2 * (N - 1 - i)):#Logic for the spaces, using N - 1 here as N is 5 but the pattern maxes out at 4. 
        print(" ", end=" ")
    for j in range(i, 0, -1):       #Logic to print to numbers on the right side in reverse order.
        print(j, end=" ")
    print()                         #Move to then next line 
  