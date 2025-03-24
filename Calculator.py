# what operators we can use? >
operators = 'choose from the following: + , - , * , / '
print(operators)

# what hte user chooses >
op = input('Enter operator here: ')

# actual math >
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# if statements >
if op == '+':
    print(round(num1 + num2, 3))

elif op == '-':
    print(round(num1 - num2,3))

elif op == '*':
    print(round(num1 * num2,3))

elif op == '/':
    print(round(num1 / num2,3))

else:
    print('Invalid input.. \nPlease select from the given options!')
    