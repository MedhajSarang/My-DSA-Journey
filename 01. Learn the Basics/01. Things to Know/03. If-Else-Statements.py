#If-Else Statements

'''Conditional statements are a fundamental concept in programming that allows you to make decisions based on certain conditions. These statements enable your code to execute different blocks of code depending on whether specific conditions are met or not.'''

#if statement
'''It is used to execute a block of code only if a certain condition is met. It allows us to conditionally execute code based on whether the specified condition is true.'''

#else statement
'''This on the other hand, is an optional companion to the if statement. It specifies what code to execute if the condition in the if statement is not met.'''

#Code

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

#Explanation: 
'''Here, we take the user's age as input and use the if statement to check if the age is greater than or equal to 18. If this condition satisfies then it prints, "You are an adult" and if the condition is false, then the else condition is satisfied and it prints, "You are not an adult".'''

#Code: 

marks = 70

if marks < 40:
    print("Grade F")
elif marks >= 40 and marks < 60:
    print("Grade B")
elif marks >= 60 and marks < 90:
    print("Grade A")
elif marks >= 90 and marks < 100:
    print("Grade O")
else:
    print("Invalid Input")

