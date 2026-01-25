'''
Problem 8:- Inverted Star Pyramid

Expected Output:

* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
'''

#Code

N = 5
for i in range(0, N):                       #Number of Rows
    for j in range(0, i):                   #Determine the blank spaces before the stars
        print(" ", end=" ")                 #Print the blank spaces
    for j in range(0, 2 * N - (2 * i + 1)): #Determine the number of stars in each row
        print("*",end=" ")                  #Print the stars
    print()                                 #Move to the next row