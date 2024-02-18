number_of_tourists = int(input())
season = input()

price_per_tourist = 0
discount = 0.00

if season == "spring":
    if number_of_tourists <= 5:
        price_per_tourist = 50.00
    else:
        price_per_tourist = 48.00

elif season == "summer":
    discount = 0.15
    if number_of_tourists <= 5:
        price_per_tourist = 48.50
    else:
        price_per_tourist = 45.00

elif season == "autumn":
    if number_of_tourists <= 5:
        price_per_tourist = 60.00
    else:
        price_per_tourist = 49.50

elif season == "winter":
    discount = -0.08
    if number_of_tourists <= 5:
        price_per_tourist = 86.00
    else:
        price_per_tourist = 85.00

total_bill = (price_per_tourist * number_of_tourists) * (1 - discount)

print(f"{total_bill:.2f} leva.")
