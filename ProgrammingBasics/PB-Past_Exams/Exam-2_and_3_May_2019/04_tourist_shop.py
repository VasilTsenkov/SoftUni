budget = float(input())

product_counter = 0
purchase_amount = 0
user_stopped = False
not_enough_money = False
money_needed = 0

while True:
    user_input = input()

    if user_input != "Stop":
        product_name = user_input
    else:
        user_stopped = True
        break

    product_price = float(input())
    product_counter += 1

    if product_counter % 3 == 0:
        product_price /= 2

    if budget >= product_price:
        budget -= product_price
        purchase_amount += product_price
    else:
        money_needed = product_price - budget
        not_enough_money = True
        break

if user_stopped:
    print(f"You bought {product_counter} products for {purchase_amount:.2f} leva.")
elif not_enough_money:
    print("You don't have enough money!")
    print(f"You need {money_needed:.2f} leva!")
