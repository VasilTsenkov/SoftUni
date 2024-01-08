celsius = float(input())

weather = 0

if 26.00 <= celsius <= 35.00:
    weather = 'Hot'
elif 20.1 <= celsius <= 25.9:
    weather = 'Warm'
elif 15.00 <= celsius <= 20.00:
    weather = 'Mild'
elif 12.00 <= celsius <= 14.9:
    weather = 'Cool'
elif 5.00 <= celsius <= 11.9:
    weather = 'Cold'
else:
    weather = 'unknown'

print(weather)
