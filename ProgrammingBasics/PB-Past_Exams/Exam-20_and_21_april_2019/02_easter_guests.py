from math import ceil

number_of_guests = int(input())
budget = int(input())

pastry_price = 4
pastry_quantity = ceil(number_of_guests / 3)
egg_price = 0.45
egg_quantity = number_of_guests * 2

total_cost = pastry_price * pastry_quantity + egg_price * egg_quantity
difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Lyubo bought {pastry_quantity} Easter bread and {egg_quantity} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
