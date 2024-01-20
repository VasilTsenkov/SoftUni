hour_of_day = int(input())
day_from_week = input()

if 10 <= hour_of_day <= 18 and (day_from_week == 'Monday'
                                or day_from_week == 'Tuesday'
                                or day_from_week == 'Wednesday'
                                or day_from_week == 'Thursday'
                                or day_from_week == 'Friday'
                                or day_from_week == 'Saturday'):
    print('open')
else:
    print('closed')
