quantity_of_eggs_in_store = int(input())

sold_eggs = 0

while True:
    user_input = input()

    if user_input != "Close":
        action = user_input
    else:
        print("Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break

    if action == "Buy":
        eggs_demanded = int(input())

        if quantity_of_eggs_in_store >= eggs_demanded:
            sold_eggs += eggs_demanded
            quantity_of_eggs_in_store -= eggs_demanded
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {quantity_of_eggs_in_store}.")
            break

    elif action == "Fill":
        eggs_supplied = int(input())
        quantity_of_eggs_in_store += eggs_supplied
