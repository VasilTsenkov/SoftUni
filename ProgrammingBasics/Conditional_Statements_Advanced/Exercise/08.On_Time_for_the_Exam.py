exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_total_minutes = (exam_hour * 60) + exam_minutes
arrival_total_minutes = (arrival_hour * 60) + arrival_minutes

difference = abs(arrival_total_minutes - exam_total_minutes)
hour_difference = difference // 60
minutes_difference = difference % 60

if exam_total_minutes < arrival_total_minutes:
    print('Late')
    if hour_difference >= 1:
        print(f'{hour_difference}:{minutes_difference:02d} hours after the start')
    else:
        print(f'{minutes_difference} minutes after the start')
elif (exam_total_minutes == arrival_total_minutes) or (hour_difference == 0 and minutes_difference <= 30):
    print('On time')
    if exam_total_minutes == arrival_total_minutes:
        pass
    else:
        print(f'{minutes_difference} minutes before the start')
else:
    print('Early')
    if hour_difference >= 1:
        print(f'{hour_difference}:{minutes_difference:02d} hours before the start')
    else:
        print(f'{minutes_difference} minutes before the start')
