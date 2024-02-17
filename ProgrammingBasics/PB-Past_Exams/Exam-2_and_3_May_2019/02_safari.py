budget = float(input())
liters_fuel_needed = float(input())
day_from_week = input()

liter_fuel_price = 2.10
tour_guide = 100
discount = 0.00

total_cost = liters_fuel_needed * liter_fuel_price + tour_guide

if day_from_week == "Saturday":
    discount = 0.10
elif day_from_week == "Sunday":
    discount = 0.20

safari_cost = total_cost * (1 - discount)
difference = abs(budget - safari_cost)

if budget >= safari_cost:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
