while True:
    first_number = int(input('Type first number: '))
    operation = (input('Choose type of math operation(+,-,*,/): '))
    second_number = int(input('Type second number: '))



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

    continue_calculation = input('Do you want to continue? (yes/no):')

    if continue_calculation != 'y' and continue_calculation.lower() != 'yes':
        print('Thank you for using the calculator!')
        break
