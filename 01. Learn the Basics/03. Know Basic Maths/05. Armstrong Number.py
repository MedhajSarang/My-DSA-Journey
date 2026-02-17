'''
Check if a number is Armstrong Number or not

Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
Example 2:
Input:N = 371                
Output: True
Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371
'''

#Code

def armstrongNumber (self, n):
        power = len(str(n))         #Converts number to string and counts the digits present
        sum = 0                     #Initialize a sum variable to 0 to store and compare the value later
        num = n                     
        
        while n > 0:                #Outer loop checks for condition when n > 0
            digit = n % 10          #Extracts the last digit of the number
            sum += digit ** power   #Raises the digit to the required power and adds to the total
            n //= 10                #Removes the last digit from the number
        return num == sum           #If both are equal its an Armstrong number returns true otherwise false