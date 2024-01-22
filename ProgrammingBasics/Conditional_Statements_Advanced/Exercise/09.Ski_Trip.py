trip_days = int(input())
trip_stay = input()
trip_review = input()

trip_days -= 1
price = 0
discount = 0
extra_discount = 0

if trip_stay == 'room for one person':
    price = 18
elif trip_stay == 'apartment':
    price = 25
    if trip_days < 10:
        discount = 0.30
    elif trip_days <= 15:
        discount = 0.35
    elif trip_days > 15:
        discount = 0.50
elif trip_stay == 'president apartment':
    price = 35
    if trip_days < 10:
        discount = 0.10
    elif trip_days <= 15:
        discount = 0.15
    elif trip_days > 15:
        discount = 0.20

total_bill = (price * trip_days) * (1 - discount)

if trip_review == 'positive':
    extra_discount = -0.25
elif trip_review == 'negative':
    extra_discount = 0.10

total_bill *= (1 - extra_discount)

print(f'{total_bill:.2f}')
