'''
Problem 2:- Right-Angled Triangle Pattern

Expected Pattern:- 
*
* *
* * *
* * * *
* * * * *
'''

#Code:-

N = 5
for i in range(0, N + 1):      #Decides the total number of rows
    for j in range(i):         #Decides stars per rows
        print("*", end = " ")  #Prints the star on the same line
    print()                    #Move to next line