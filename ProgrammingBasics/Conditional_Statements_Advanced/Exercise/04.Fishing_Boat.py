budget = int(input())
season = input()
fishermen = int(input())

ship_price = 0
discount = 0

if season == 'Spring':
    ship_price = 3000
    if fishermen <= 6:
        discount = 0.10
    elif fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25
elif season == 'Summer' or season == 'Autumn':
    ship_price = 4200
    if fishermen <= 6:
        discount = 0.10
    elif fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25
elif season == 'Winter':
    ship_price = 2600
    if fishermen <= 6:
        discount = 0.10
    elif fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25

total_bill = ship_price * (1 - discount)

if (fishermen % 2 == 0) and (season != 'Autumn'):
    total_bill *= 0.95

if budget >= total_bill:
    budget_left = budget - total_bill
    print(f'Yes! You have {budget_left:.2f} leva left.')
else:
    budget_exceeded = total_bill - budget
    print(f'Not enough money! You need {budget_exceeded:.2f} leva.')
    