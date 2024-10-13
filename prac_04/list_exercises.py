numbers = []
value = 1
runs = 0
print('Enter numbers below (Enter value < 0 to finish, this value will not be included.)')
while value > 0:
    runs += 1
    value = int(input(f"Number {runs}: "))
    numbers.append(value)
if value >= 0:
    numbers = numbers[:-1]
    print('Finished.')
print(f'The first number is: {numbers[0]}')
print(f'The last number is: {numbers[-1]}')
print(f'The smallest number is: {min(numbers)}')
print(f'The largest number is: {max(numbers)}')
print(f'The average of the numbers is: {sum(numbers) / len(numbers)}')

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter username: ")
if user_input in usernames:
    print('Access Granted.')
else:
    print('Access Denied.')