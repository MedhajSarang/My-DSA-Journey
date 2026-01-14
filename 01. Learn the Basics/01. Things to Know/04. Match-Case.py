# Match Case in Python

'''
-> match-case is used for structural pattern matching. 
-> Introduced in Python 3.10
-> It compares a value against different patterns. 
-> Works like swithc-case but is more powerful.
'''

#Key concepts
'''
match -> evaluates the expression
case -> checks patterns against the expression
_ (underscore) -> wildcard (default case)
No break statement needed
First matching case is executed
'''

#Code

day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Input")

'''
In the above example, if the user provides the input as 3, it will print "Wednesday" since it matches with the case 3 statement.
'''