''' 
Print all Divisors of a given Number

Problem Statement: Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.
'''

#Code

def getDivisors(self, n):
    res = []                    #Create a list to store the divisors
    for i in range(1, n + 1):   #Loop from 1 to n
        if n % i == 0:          #Check if i is a divisor of n
            res.append(i)       #Add the result
    return res                  #Return the list