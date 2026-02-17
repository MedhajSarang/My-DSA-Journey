'''
Find GCD of two numbers

Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

Example 1:
Input: N1 = 9, N2 = 12

Output: 3
Explanation:
Factors of 9: 1, 3, 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3
Greatest common factor: 3 (GCD)

Example 2:
Input: N1 = 20, N2 = 15

Output: 5
Explanation:
Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 15: 1, 3, 5, 15
Common Factors: 1, 5
Greatest common factor: 5 (GCD)

'''

#Code

def gcd(self, a, b):                        
        for i in range(min(a,b),0,-1):      #Loop to check find the smaller number and go down by 1
            if a % i == 0 and b % i == 0:   #Checks if i divides both the numbers, and is used to ensure both cases are true together
                return i                    #Return the greatest value of i as we are looping from largest to smallest
        return 1                            #Returns 1 if no common divisor greater than 1 is found