'''
Problem 3:- Right-Angled Number Triangle

Expected Output:- 

1 
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''

#Code

N = 5
for i in range(1, N + 1):       #Decides rows
    for j in range(1, i + 1):   #Decides the number going in rows; by default starts at 0 so the range needs to be modified
        print(j, end= " ")      #Prints the number in rows
    print()                     #Moves to next line
