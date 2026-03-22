'''
Print N to 1 using Recursion

Description: Given an integer N, write a program to print numbers from N to 1.

Examples:
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.
'''

#Code
class Solution:
    def printNumbers(self, current):        #Recursive Function
        if current < 1:                     #Base Case
            return
        print(current, end=' ')             #Print current number
        self.printNumbers(current - 1)      #Recursive Call

if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(n)
    print()