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
for i in range(0, N):           #Code for top half
  for j in range(0, N - i - 1): #Logic for blank spaces 
    print(" ", end=" ")         #Printing the blank spaces
  for j in range(0, 2*i + 1):   #Logic for stars in the top half
    print("*",end=" ")          #Printing the stars
  print()                       #Move to next row
for i in range(N,0,-1):         #Code for bottom half
  for j in range(0, N - i):     #Logic for blank spaces
    print(" ", end=" ")         #Print blank spaces
  for j in range(0, 2*i - 1):   #Logic for stars in the bottom half
    print("*",end=" ")          #Print the stars in bottom half
  print()                       #Move to next row