weather = input().lower()

report = 0

if weather == 'sunny':
    report = 'warm'
else:
    report = 'cold'

print(f"It's {report} outside!")
