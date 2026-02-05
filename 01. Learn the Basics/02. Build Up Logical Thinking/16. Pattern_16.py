'''
Problem 16: Alpha-Ramp Pattern

Expected Output: 

A 
B B
C C C
D D D D
E E E E E
'''

#Code: 
N = 5
for i in range(N):          #Logic for outer loop
    ch = chr(65 + i)        #Logic for alphabet per row
    for j in range(i + 1):  #Number of alphabets per row
        print(ch, end=" ")  #Print the alphabet in each row
    print()                 #Move to next row