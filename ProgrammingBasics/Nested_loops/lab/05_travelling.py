while True:
    user_input = input()

    if user_input != "End":
        destination = user_input
    else:
        break

    budget = float(input())

    while budget > 0:
        savings = float(input())

        budget -= savings

    print(f"Going to {destination}!")
