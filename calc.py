import pandas as pd

print('Calculator ready for input!')
str1=input('Enter first number: ')
try:
    num1=int(str1)
except:
    print('Invalid input')
action=input('Enter action (+, -, *, /): ')
if action not in ['+', '-', '*', '/']:
    print('Invalid input')
str2=input('Enter second number: ')
try:
    num2=int(str2)
except:
    print('Invalid input')
if action == '+':
    print(num1 + num2)
elif action == '-':
    print(num1 - num2)
elif action == '*':
    print(num1 * num2)
elif action == '/':
    if num2 == 0:
        print('Division by zero is not possible')
    else:
        print(num1 / num2)
        
