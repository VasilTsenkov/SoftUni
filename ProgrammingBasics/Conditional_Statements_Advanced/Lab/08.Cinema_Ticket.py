day_from_week = input()

price_of_ticket = 0

if (day_from_week == 'Monday'
        or day_from_week == 'Tuesday'
        or day_from_week == 'Friday'):
    price_of_ticket = 12

elif day_from_week == 'Wednesday' or day_from_week == 'Thursday':
    price_of_ticket = 14

else:
    price_of_ticket = 16

print(price_of_ticket)
