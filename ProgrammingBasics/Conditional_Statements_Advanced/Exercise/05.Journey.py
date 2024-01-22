budget = float(input())
season = input()

destination = ''
trip_type = ''
total_bill = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        trip_type = 'Camp'
        total_bill = budget * 0.30
    elif season == 'winter':
        trip_type = 'Hotel'
        total_bill = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        trip_type = 'Camp'
        total_bill = budget * 0.40
    elif season == 'winter':
        trip_type = 'Hotel'
        total_bill = budget * 0.80
if budget > 1000:
    destination = 'Europe'
    total_bill = budget * 0.90
    trip_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{trip_type} - {total_bill:.2f}')
