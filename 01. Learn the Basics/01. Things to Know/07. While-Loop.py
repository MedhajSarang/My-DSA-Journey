#Python While Loop

'''
Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.
'''

count = 0
while count < 3:
    count = count + 1
    print("Hello!")

#Infinite While Loop
'''
age = 28

while age > 19:
    print("Infinite loop")
'''

'''
Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
'''

#While loop with continue statement

i = 0
a = 'Medhajsarang'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print(a[i])
    i += 1

#While loop with break statement

i = 0
a = 'Medhajsarang'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break

    print(a[i])
    i += 1

#While loop with pass statement

a = 'Medhajsarang'
i = 0
while i < len(a):
    i += 1
    pass

print('Value of i :', i)

#While loop with else

i = 0
while i < 4:
    i += 1
    print(i)
else: 
    print('No Break\n')

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print('No Break')
