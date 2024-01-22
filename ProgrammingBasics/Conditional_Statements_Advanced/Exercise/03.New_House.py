flower_type = input()
quantity_flowers = int(input())
budget = int(input())

price_flower = 0.00
discount = 0.00

if flower_type == 'Roses':
    price_flower = 5
    if quantity_flowers > 80:
        discount = 0.10
elif flower_type == 'Dahlias':
    price_flower = 3.80
    if quantity_flowers > 90:
        discount = 0.15
elif flower_type == 'Tulips':
    price_flower = 2.80
    if quantity_flowers > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    price_flower = 3
    if quantity_flowers < 120:
        discount = -0.15
elif flower_type == 'Gladiolus':
    price_flower = 2.50
    if quantity_flowers < 80:
        discount = -0.20

total_bill = (price_flower * quantity_flowers) * (1 - discount)

if budget >= total_bill:
    budget_left = budget - total_bill
    print(f'Hey, you have a great garden with {quantity_flowers} {flower_type} and {budget_left:.2f} leva left.')
else:
    budget_exceeded = total_bill - budget
    print(f'Not enough money, you need {budget_exceeded:.2f} leva more.')
