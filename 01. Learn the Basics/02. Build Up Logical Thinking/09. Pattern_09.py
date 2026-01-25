'''
Problem 9:- Diamond Star Pattern

Expected Output:- 
        *
      * * * 
    * * * * *
  * * * * * * *  
* * * * * * * * * 
* * * * * * * * *
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
#Status - Still solving this one
#Code
N = 5
for i in range(0, N*2):
    for j in range(0, N - i - 1):
        print(" ", end=" ")
    for j in range(0, 2 * i - 1):
        print("*",end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(0, 2 * N - (2 * i + 1)):
        print("*",end=" ")
    print()