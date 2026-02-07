'''
Reverse a Number

Input: N = 12345
Output:54321
Explanation: The reverse of 12345 is 54321.

Input: N = 7789                
Output: 9877
Explanation: The reverse of number 7789 is 9877.
'''

#Code

class Solution:
    def reverse(self, N: int) -> int:
        if N < 0:                       #Logic to deal with a negative number
            sign = -1
            N = -N
        else:
            sign = 1
        newNum = 0                      #Initialize the reversed number
        while N > 0:
            a = N % 10                  #a is the last digit
            newNum = newNum * 10 + a    #the last digit is appended to the new reversed number
            N = N // 10                 #Logic to remove the last digit from n
        return newNum * sign