'''
Factorial of a Number: Iterative and Recursive

Problem Statement: Given a number X, print its factorial

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it.

Note: X is always a positive number

Examples:
Example 1:
Input:
 X = 5
Output:
 120
Explanation:
 5! = 5*4*3*2*1

Example 2:
Input:
 X = 3
Output:
 6
Explanation:
 3!=3*2*1
'''

#Code
def factorial(n):                   #Recursive Function
    if n == 0:                      #Base Case
        return 1
    return n * factorial(n - 1)     #Recursive Case

n = 3
print(factorial(n))