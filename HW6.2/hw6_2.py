user_time = int(input('Type the number of second:'))

if 0 <= user_time < 8640000:
    days, rest_time = divmod(user_time, 86400)
    hours, rest_time2 = divmod(rest_time, 3600)
    minutes, seconds = divmod(rest_time2, 60)

    day_word = 'днів'
    if days % 10 == 1 and days != 11:
        day_word = 'день'
    elif days % 10 in range(2,4):
        day_word = 'дні'

    result = f'{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'
    print(result)
else:
    print('The number must be in the range 0 to 8640000')