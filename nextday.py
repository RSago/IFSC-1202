months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input('Enter month:'))
day = int(input('Enter day: '))
if month <= 0 or month > 12:
    print('invalid month...')
else:
if day <= 0 or day > months_days[month-1]:
    print('invalid day...')
    else:
    if day == months_days[month-1]:
        day = 1
if month == 12:
    month = 1
else:
    month += 1
else:
    day += 1
    print('Next Day: {0}/{1}'.format(month, day))