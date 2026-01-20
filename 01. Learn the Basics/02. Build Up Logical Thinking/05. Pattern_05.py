'''
Problem 5:- Inverted Right Pyramid

Expected Output:- 

* * * * *
* * * * 
* * * 
* * 
*
'''

#Code

N = 5
for i in range(0, N):           #Outer loop -> decides the number of rows.
    for j in range(0, N-i):     #Inner loop -> handles the columns, a more dynamic approach. Eg, 5 - 0 = 5; 5 - 1 = 0; and so on.
        print("*", end=" ")     #Print the star
    print()                     #Move to next line