first_number = int(input('Type first number: '))
second_number = int(input('Type second number: '))
operation = (input('Choose type of math operation(+,-,*,/): '))


if operation == '/' and second_number == 0:
        print('Error, you can`t use 0 as second number')
elif operation == '/':
    print(first_number/second_number)
elif operation == '+':
    print(first_number+second_number)
elif operation == '-':
    print(first_number-second_number)
elif operation == '*':
    print(first_number*second_number)
else:
    print('This type of operation is not supported.')

