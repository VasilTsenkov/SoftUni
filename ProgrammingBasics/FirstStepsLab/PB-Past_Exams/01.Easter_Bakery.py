price_flour = float(input())
quantity_flour = float(input())
quantity_sugar = float(input())
quantity_egg_boxes = int(input())
quantity_maq = int(input())

price_sugar = 0.75 * price_flour
price_egg_boxes = 1.1 * price_flour
price_maq = 0.20 * price_sugar

total_bill = price_flour * quantity_flour \
             + price_sugar * quantity_sugar \
             + price_egg_boxes * quantity_egg_boxes \
             + price_maq * quantity_maq

print(f'{total_bill:.2f}')
