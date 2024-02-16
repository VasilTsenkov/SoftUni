from sys import maxsize
from math import ceil

number_of_pastry = int(input())

total_sugar_needed = 0
total_flour_needed = 0
max_sugar_used = -maxsize
max_flour_used = -maxsize

for _ in range(number_of_pastry):
    sugar_quantity = int(input())
    flour_quantity = int(input())

    total_sugar_needed += sugar_quantity
    total_flour_needed += flour_quantity

    if sugar_quantity > max_sugar_used:
        max_sugar_used = sugar_quantity

    if flour_quantity > max_flour_used:
        max_flour_used = flour_quantity

sugar_packs = ceil(total_sugar_needed / 950)
flour_packs = ceil(total_flour_needed / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
