'''Understanding input and output operations is fundamental to Python programming. With the print() function, we can display output in various formats, while the input() function enables interaction with users by gathering input during program execution'''

#Taking Input in Python

name = input("Enter you name: ")
print("Hello,",name, "Welcome!")

#Printing Output using print() in Python

print("Hello, World!")

#Printing single variable
s = "Medhaj"
print(s)

#Printing multiple variables 
age = 22
city = "Mumbai"
print(name, age, city)

#Taking multiple inputs
'''We are taking multiple input from the user in a single line, splitting the values entered by the user into separate variables for each value using the split() method.'''
x, y = input("Enter two values: ").split()
print("Number of Boys: ", x)
print("Number of Girls: ", y)

