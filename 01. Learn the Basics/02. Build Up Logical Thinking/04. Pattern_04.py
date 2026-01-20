'''
Problem 4:- Right-Angled Number Pyramid-II

Expected Output:- 
1 
2 2 
3 3 3 
4 4 4 4
5 5 5 5 5
'''

#Code:

N = 5
for i in range(0, N+1):         #Number of Rows
    for j in range(1, i + 1):   #Number of elements per row
        print(i, end=" ")       #Printing logic in each row, as i remains constant print the value of i
    print()                     #Move to next line