''' 
Problem 7:- Star Pyramid

Expected Output:- 

        * 
      * * * 
    * * * * * 
  * * * * * * *
* * * * * * * * *
'''

#Code:- 
N = 5
for i in range(1,N + 1):    #Number of Rows
  for j in range(N - i):    #Spaces Before
    print(" ", end=" ")     #Print the blank spaces
  for j in range(2 * i - 1):#Number of stars per row
    print("*", end=" ")     #Print the stars
  print(" ")                #Move to next row