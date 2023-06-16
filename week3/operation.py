number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))

operation = input('Enter operation: [+, -, *, /]')

if operation not in ['+', '-', '*', '/']:
    print('Invalid operation')
    exit()
elif operation == '+':
    answer = number1 + number2
elif operation == '-':
    answer = number1 - number2
elif operation == '*':
    answer = number1 * number2
else:
    answer = number1 / number2
    
print(f'{number1} {operation} {number2} = {answer}')

