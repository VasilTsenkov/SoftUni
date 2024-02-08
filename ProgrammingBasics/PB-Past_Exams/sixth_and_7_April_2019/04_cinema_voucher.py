voucher_value = int(input())

user_input = input()
ticket_counter = 0
misc_counter = 0

while user_input != "End":
    purchase = user_input

    len_of_purchase = len(purchase)

    if len_of_purchase > 8:
        sum_purchase = ord(purchase[0]) + ord(purchase[1])
        if sum_purchase <= voucher_value:
            ticket_counter += 1
        else:
            break
    else:
        sum_purchase = ord(purchase[0])
        if sum_purchase <= voucher_value:
            misc_counter += 1
        else:
            break

    voucher_value -= sum_purchase

    user_input = input()

print(f"{ticket_counter}")
print(f"{misc_counter}")
