from math import ceil, floor

magnolia_quantity = int(input())
hyacinths_quantity = int(input())
roses_quantity = int(input())
cactus_quantity = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinths_price = 4.00
roses_price = 3.50
cactus_price = 8.00
tax = 0.05

revenue = (magnolia_quantity * magnolia_price) + (hyacinths_quantity * hyacinths_price) \
    + (roses_quantity * roses_price) + (cactus_quantity * cactus_price)
revenue_after_tax = revenue * (1 - tax)

difference = abs(gift_price - revenue_after_tax)

if revenue_after_tax >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
