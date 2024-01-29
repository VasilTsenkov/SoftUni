budget = float(input())
season = input()

car_class = ""
car_type = ""
car_price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.35 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.65 * budget
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.45 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.80 * budget
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    car_price = 0.90 * budget

print(f"{car_class}")
print(f"{car_type} - {car_price:.2f}")
