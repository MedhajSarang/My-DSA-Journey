'''
Problem 17: Alpha-Hill Pattern

Expected Output: 

      A
    A B A
  A B C B A
A B C D C B A 
'''

#Code: 

N = 5
for i in range(N): 
    print(" " * (N - i - 1), end=" ")
    ch = chr(65 + i)
    
