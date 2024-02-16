number_of_clients = int(input())

basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7.00
revenue = 0

for _ in range(number_of_clients):

    client_bill = 0
    purchased_items = 0

    while True:
        user_input = input()

        if user_input != "Finish":
            purchased_item = user_input
        else:
            if purchased_items % 2 == 0:
                discount = 0.20
                client_bill *= (1 - discount)

            print(f"You purchased {purchased_items} items for {client_bill:.2f} leva.")

            break

        if purchased_item == "basket":
            client_bill += basket_price
        elif purchased_item == "wreath":
            client_bill += wreath_price
        elif purchased_item == "chocolate bunny":
            client_bill += chocolate_bunny_price

        purchased_items += 1

    revenue += client_bill

average_client_bill = revenue / number_of_clients

print(f"Average bill per client is: {average_client_bill:.2f} leva.")
