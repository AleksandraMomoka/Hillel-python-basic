user_number = int(input("Type integer: "))

while user_number > 9:
    counter = 1
    for digit in str(user_number):
        counter *= int(digit)
    user_number = counter

print(user_number)
