hour = int(input())
minutes = int(input())

total_minutes_plus_15 = (hour * 60) + minutes + 15

updated_hour = total_minutes_plus_15 // 60
updated_minutes = total_minutes_plus_15 % 60

if updated_hour > 23:
    updated_hour = 0

if updated_minutes < 10:
    print(f'{updated_hour}:0{updated_minutes}')
else:
    print(f'{updated_hour}:{updated_minutes}')
