'''
Print Name N times using Recursion

Description: Given an integer N, write a program to print your name N times. 

Example: 
Input: N = 3
Output:- Medhaj Medhaj Medhaj
Explanation: Name is printed 3 times.
'''

#Code
class Solution:
    def printName(self, name, count, N):
        if count == N:
            return
        print(name)
        self.printName(name, count + 1, N)

if __name__ == "__main__":
    sol = Solution()
    N = 5
    name = "Medhaj"
    sol.printName(name, 0, N)
