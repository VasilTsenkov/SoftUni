age = int(input())
dishwasher_price = float(input())
toy_price = int(input())

toy_quantity = 0
gift_cash = 0
money_saved = 0

for birthday in range(1, age + 1):
    if birthday % 2 != 0:
        toy_quantity += 1
    else:
        gift_cash += 10
        money_saved += gift_cash - 1

budget = money_saved + (toy_price * toy_quantity)
budget_difference = abs(budget - dishwasher_price)

if budget >= dishwasher_price:
    print(f"Yes! {budget_difference:.2f}")
else:
    print(f"No! {budget_difference:.2f}")
    