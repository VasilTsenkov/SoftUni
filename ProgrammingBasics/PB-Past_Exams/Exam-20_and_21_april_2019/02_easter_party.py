number_of_guests = int(input())
price_per_guest = float(input())
budget = float(input())

discount = 0.00

if 10 <= number_of_guests <= 15:
    discount = 0.15
elif 15 < number_of_guests <= 20:
    discount = 0.20
elif number_of_guests > 20:
    discount = 0.25

price_per_guest *= (1 - discount)
cake_price = budget * 0.10
total_cost = price_per_guest * number_of_guests + cake_price
difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
