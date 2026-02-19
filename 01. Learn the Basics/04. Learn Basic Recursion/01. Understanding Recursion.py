#Introduction to Recursion - Understand Recursion by printing something N times. 

'''
What is Recursion?

Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem,
by breaking it down into smaller subproblems until it reaches a base case that stops further calls.
'''

'''
What is Stack Overflow in Recursion?

Whenever recursion calls are executed, they're simultaneously stored in a recursion stack where they wait for the completion of therecursive function.
A recursive function can only be completed if a base condition is fulfilled and the control returns to the parent function. 

But, when there is no base condition given for a particular recursive function, it gets called indefinitely which results in a Stack Overflow
i.e., exceeding the memory limit of the recursion stack and hence the program terminates giving a Segmentation Fault error.
'''

'''
Base Condition

It is the condition that is written in a recursive function in order for it to get completed and not run infinitely.
After encountering the base condition, the function terminates and returns back to its parent function simultaneously.
'''

'''
Recursive Tree

A recursive tree is basically a representative form of recursion which depicts how functions are called and returned as a series of events happening consecutively.
When a recursive call gets completed, the control returns back to its parent function which is then further executed until the last function waiting in the recursive stack returns.
'''

'''
Advantages of Recursion:

'''