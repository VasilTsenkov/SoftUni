film_budget = float(input())
number_employees = int(input())
price_outfit_per_employee = float(input())

decor_price = 0.1 * film_budget

price_outfit_total = number_employees * price_outfit_per_employee

if number_employees > 150:
    price_outfit_total *= 0.9

total_costs = decor_price + price_outfit_total

if film_budget >= total_costs:
    budget_left = film_budget - total_costs
    print('Action!')
    print(f'Wingard starts filming with {budget_left:.2f} leva left.')
else:
    budget_exceeded = total_costs - film_budget
    print('Not enough money!')
    print(f'Wingard needs {budget_exceeded:.2f} leva more.')
