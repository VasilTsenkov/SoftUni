price_for_luggage_above_20kg = float(input())
luggage_kilos = float(input())
remaining_days_till_travel = int(input())
number_of_luggage = int(input())

luggage_price = 0

if luggage_kilos < 10:
    luggage_price = 0.20 * price_for_luggage_above_20kg
elif luggage_kilos <= 20:
    luggage_price = 0.50 * price_for_luggage_above_20kg
else:
    luggage_price = price_for_luggage_above_20kg

if remaining_days_till_travel < 7:
    luggage_price *= 1.40
elif remaining_days_till_travel <= 30:
    luggage_price *= 1.15
else:
    luggage_price *= 1.10

luggage_bill = luggage_price * number_of_luggage

print(f"The total price of bags is: {luggage_bill:.2f} lv.")
