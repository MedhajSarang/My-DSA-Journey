'''
Problem: Count Digits in a Number

Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
'''

#Code
class Solution:
    def countDigits(self, n):
        count = 0       #Initialize the count to 0
        while n > 0:    #Run a outer while loop to check the value of n > 0
            n = n // 10 #Remove one element from n and increment the count by 1 everytime
            count += 1
        return count    #Return the final count