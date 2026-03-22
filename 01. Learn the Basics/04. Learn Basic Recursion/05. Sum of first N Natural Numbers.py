'''
Sum of first N Natural Numbers

Problem Statement: Given a number 'N', find out the sum of the first N natural numbers.

Examples:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
'''

#Code
class Solution:
    def sumOfNaturalNumbers(self, N):               #Recursive Function
        if N == 1:                                  #Base Case
            return 1
        return N + self.sumOfNaturalNumbers(N - 1)  #Recursive Case

# Driver code
if __name__ == "__main__":
    obj = Solution()
    N = int(input())
    print(obj.sumOfNaturalNumbers(N))