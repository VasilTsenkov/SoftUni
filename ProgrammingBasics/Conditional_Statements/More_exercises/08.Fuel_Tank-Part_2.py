fuel_type = input()
fuel_quantity = float(input())
has_club_card = input()

price_per_liter = 0.00
discount_per_liter = 0.00
bill_discount = 0.00

if fuel_type == "Gas":
    price_per_liter = 0.93
    if has_club_card == "Yes":
        discount_per_liter = 0.08
elif fuel_type == "Gasoline":
    price_per_liter = 2.22
    if has_club_card == "Yes":
        discount_per_liter = 0.18
elif fuel_type == "Diesel":
    price_per_liter = 2.33
    if has_club_card == "Yes":
        discount_per_liter = 0.12

if 20 <= fuel_quantity <= 25:
    bill_discount = 0.08
elif fuel_quantity > 25:
    bill_discount = 0.10

bill = (fuel_quantity * (price_per_liter - discount_per_liter)) * (1 - bill_discount)

print(f"{bill:.2f} lv.")
