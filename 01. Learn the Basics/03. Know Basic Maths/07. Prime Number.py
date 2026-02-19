'''
Check if a number is prime or not

Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2..

Example 1:
Input:N = 2
               
Output:True
                
Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).
                                        
Example 2:
Input:N =10                
                
Output: False
                
Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.
'''

#Code

def isPrime(self, n):
        if n <= 1:              #Logic to reject numbers less than 1
            return False        
        for i in range(2, n):   #Try dividing every number from 2 to n - 1
            if n % i == 0:      #If divisible then n is not prime
                return False
        return True             #If not divisible then number is prime