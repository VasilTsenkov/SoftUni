time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_time = time_first + time_second + time_third

minutes = sum_time // 60
seconds = sum_time % 60

if seconds >= 10:
    print(f'{minutes}:{seconds}')
else:
    print(f'{minutes}:0{seconds}')
