'''
Problem 17: Alpha-Hill Pattern

Expected Output: 

      A
    A B A
  A B C B A
A B C D C B A 
'''

#Code: 

N = 4
for i in range(N):                     #Total number of rows
    print("  " * (N - i - 1), end=" ") #Logic to print the spaces before the pattern
    ch = ord('A')                      #Returns the ordinal value of a character
    breakpoint = (2 * i + 1) // 2
    for j in range(1, 2 * i + 2):      #Logic for the inner loop
        print(chr(ch), end=" ")        #Print the characters in the rows
        if j <= breakpoint:            
            ch += 1
        else: 
            ch -= 1
    print()
