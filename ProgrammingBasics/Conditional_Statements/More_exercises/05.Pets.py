from math import floor, ceil

days_gone = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food_grams = float(input())

turtle_food = turtle_food_grams / 1000
total_food_needed = days_gone * (dog_food + cat_food + turtle_food)

difference = abs(food_left - total_food_needed)

if food_left >= total_food_needed:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
    