charity_target = int(input())

charity_sum = 0
counter_for_cash_or_card = 0
cash_counter = 0
cash_total = 0
card_counter = 0
card_total = 0
user_input = input()
collected_money = False

while user_input != "End":
    price = int(user_input)

    # Case for cash payment and credit payment
    if counter_for_cash_or_card % 2 == 0 and price <= 100:
        charity_sum += price
        cash_counter += 1
        cash_total += price
        print("Product sold!")
    elif counter_for_cash_or_card % 2 != 0 and price >= 10:
        charity_sum += price
        card_counter += 1
        card_total += price
        print("Product sold!")
    else:
        print("Error in transaction!")

    # Check for charity money
    if charity_sum >= charity_target:
        collected_money = True
        break

    counter_for_cash_or_card += 1
    user_input = input()

cash_average = 0
card_average = 0
if cash_counter > 0 and card_counter > 0:
    cash_average = cash_total / cash_counter
    card_average = card_total / card_counter

if collected_money:
    print(f"Average CS: {cash_average:.2f}")
    print(f"Average CC: {card_average:.2f}")
else:
    print("Failed to collect required money for charity.")
