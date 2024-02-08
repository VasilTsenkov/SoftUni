film_budget = float(input())
employees = int(input())
clothing_price_per_employee = float(input())

decor = 0.10 * film_budget
discount = 0

if employees > 150:
    discount = 0.10

clothing_price = clothing_price_per_employee * employees * (1 - discount)
total_cost = decor + clothing_price

budget_difference = abs(film_budget - total_cost)

if total_cost > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {budget_difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget_difference:.2f} leva left.")
    