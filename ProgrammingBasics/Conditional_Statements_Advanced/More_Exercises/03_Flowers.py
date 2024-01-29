chrysanthemums_quantity = int(input())
roses_quantity = int(input())
tulips_quantity = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

bill = ((chrysanthemums_quantity * chrysanthemums_price)
        + (roses_quantity * roses_price)
        + (tulips_quantity * tulips_price))

if holiday == "Y":
    holiday_discount = -0.15
    bill *= (1 - holiday_discount)

if tulips_quantity > 7 and season == "Spring":
    discount = 0.05
    bill *= (1 - discount)
elif roses_quantity >= 10 and season == "Winter":
    discount = 0.10
    bill *= (1 - discount)

if (tulips_quantity + roses_quantity + chrysanthemums_quantity) > 20:
    quantity_discount = 0.20
    bill *= (1 - quantity_discount)

bill += 2

print(f"{bill:.2f}")
