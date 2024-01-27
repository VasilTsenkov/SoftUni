holidays = int(input())

holidays_playtime = 127
total_holidays_playtime = holidays * holidays_playtime

workdays = 365 - holidays
workdays_playtime = 63
total_workdays_playtime = workdays * workdays_playtime

total_playtime = total_holidays_playtime + total_workdays_playtime
Tom_sleep_norm = 30000

difference = abs(Tom_sleep_norm - total_playtime)
hours = difference // 60
minutes = difference % 60

if Tom_sleep_norm >= total_playtime:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
