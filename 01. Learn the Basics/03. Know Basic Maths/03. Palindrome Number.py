'''
Check if a number is Palindrome or Not

Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

'''

#Code

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:                               #Logic to elimiante negative numbers as they are not palindromes
            return False
        else: 
            oriNum = x                          #Used to compare at the end as the value of x will become 0
            newNum = 0
            while x > 0:
                newNum = newNum * 10 + (x % 10) #Logic to reverse the number
                x //= 10
            return oriNum == newNum