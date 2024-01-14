from math import ceil

series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_length = break_length * 0.125
rest_length = break_length * 0.25
break_left = break_length - (lunch_length + rest_length)

if break_left >= episode_length:
    time_left = break_left - episode_length
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    time_exceeded = episode_length - break_left
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_exceeded)} more minutes.")
