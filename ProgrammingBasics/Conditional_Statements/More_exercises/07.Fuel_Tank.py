fuel_type = input()
liters_in_tank = float(input())

if (fuel_type != "Diesel") and (fuel_type != "Gasoline") and (fuel_type != "Gas"):
    print("Invalid fuel!")
else:
    if liters_in_tank < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
    else:
        print(f"You have enough {fuel_type.lower()}.")
