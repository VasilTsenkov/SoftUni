import math

price_rocket = float(input())
quantity_rockets = int(input())
quantity_shoes = int(input())

price_shoes = price_rocket * 1/6
total_shoes = price_shoes * quantity_shoes
total_rockets = price_rocket * quantity_rockets
other_equipment = (total_shoes + total_rockets) * 0.2
total_bill = total_rockets + total_shoes + other_equipment
bill_djokovic = total_bill * 1/8
bill_sponsors = total_bill * 7/8

print(f'Price to be paid by Djokovic {math.floor(bill_djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(bill_sponsors)}')
