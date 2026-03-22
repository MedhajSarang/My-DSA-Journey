'''
Description: Given an integer N, write a program to print numbers from 1 to N.

Examples:

Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.
'''

#Code
class Solution:
    def printNumbers(self, current, n):     #Recursive Function
        if current > n:                     #Base Case
            return
        print(current, end=' ')             #Print Current Number

        self.printNumbers(current + 1, n)   #Recursive call

if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(1, n)
    print()
