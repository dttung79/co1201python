week_day = int(input('Enter weekday in number: '))
if week_day not in [1, 2, 3, 4, 5, 6, 7]:
    print('Invalid weekday')
elif week_day == 1:
    print('Sunday')
elif week_day == 2:
    print('Monday')
elif week_day == 3:
    print('Tuesday')
elif week_day == 4:
    print('Wednesday')
elif week_day == 5:
    print('Thursday')
elif week_day == 6:
    print('Friday')
else:
    print('Saturday')
