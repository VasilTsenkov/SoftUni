budget = float(input())
category = input()
people_in_group = int(input())

transport_percentage = 0
ticket_price = 0

if people_in_group <= 4:
    transport_percentage = 0.75
elif people_in_group <= 9:
    transport_percentage = 0.60
elif people_in_group <= 24:
    transport_percentage = 0.50
elif people_in_group <= 49:
    transport_percentage = 0.40
else:
    transport_percentage = 0.25

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

budget = budget * (1 - transport_percentage)
ticket_price_group = ticket_price * people_in_group
budget_difference = abs(budget - ticket_price_group)

if budget >= ticket_price_group:
    print(f"Yes! You have {budget_difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {budget_difference:.2f} leva.")
