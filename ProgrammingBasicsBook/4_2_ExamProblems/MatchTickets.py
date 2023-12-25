budget = float(input())
category = str(input()).lower()
people = int(input())

if 1 <= people <= 4:
    transport = 0.75 * budget
    leftBudget = budget - transport
    if category == "normal":
        price = 249.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
    if category == "vip":
        price = 499.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
elif 5 <= people <= 9:
    transport = 0.60 * budget
    leftBudget = budget - transport
    if category == "normal":
        price = 249.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
    if category == "vip":
        price = 499.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
elif 10 <= people <= 24:
    transport = 0.50 * budget
    leftBudget = budget - transport
    if category == "normal":
        price = 249.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
    if category == "vip":
        price = 499.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
elif 25 <= people <= 49:
    transport = 0.40 * budget
    leftBudget = budget - transport
    if category == "normal":
        price = 249.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
    if category == "vip":
        price = 499.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
elif people >= 50:
    transport = 0.25 * budget
    leftBudget = budget - transport
    if category == "normal":
        price = 249.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
    if category == "vip":
        price = 499.99 * people
        if price <= leftBudget:
            n = leftBudget - price
            print(f"Yes! You have {n:.2f} leva left.")
        elif price > leftBudget:
            n = price - leftBudget
            print(f"Not enough money! You need {n:.2f} leva.")
