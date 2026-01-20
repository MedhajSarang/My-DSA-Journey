'''
Problem 6:- Inverted Numbered Right Pyramid

Expected Output:- 

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

#Code

N = 5
for i in range(0, N + 1):           #Outer Loop -> Number of Rows
    for j in range(1, N + 1 - i):   #Inner Loop -> Structure of Pyramid, number of characters in each row
        print(j, end=" ")           #Print the row
    print()                         #Move to next row