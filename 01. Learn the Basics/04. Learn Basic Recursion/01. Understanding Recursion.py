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
1. Simplifies Code: Complex problems can be sovled in fewer lines of code compares to iterative solutions.

2. Natural representation: Problems that are recursive in nature are easier to express.

3. Reduces code complexity: Avoids writing nested loops, making the logic more readable and elegant.

4. Useful in divide-and-conquer algorithms: Essential for algorithms like QuickSort, MergeSort, Binary Search and Dynamic Programming.
'''

'''
Disadvantages of Recursion:
1. High memory usage: Each recursive call adds a new layer to the function call stack, which may lead to memory overhead.

2. Risk of stack overflow: Without proper base cases, infinite recursion can occur and crash the program. 

3. Slower execution: Function calls and returns add extra overhead compared to simple loops. 

4. Harder to debug: Tracing recursive calls can be confusing, especially in deep recursion.
'''