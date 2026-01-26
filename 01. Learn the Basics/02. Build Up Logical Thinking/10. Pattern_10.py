'''
Problem 10:- Half Diamond Star Pattern

Expected Output:- 
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
#Code
N = 5
for i in range(1, N + 1):       #For the top half
    for j in range(i):          #Logic for printing stars
        print("*",end=" ")      #Printing the stars
    print()                     #Move to next line
for i in range(N - 1, 0, -1):   #Logic for bottom half
    for j in range(i):          #logic for printing the stars
        print("*",end=" ")      #Printing the stars
    print()                     #Move to next line