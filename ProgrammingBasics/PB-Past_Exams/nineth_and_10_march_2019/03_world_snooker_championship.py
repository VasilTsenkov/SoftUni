tournament_stage = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_photo = input()

ticket_price = 0.00
free_photo = False

if tournament_stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif tournament_stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif tournament_stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400.00

full_price = ticket_price * number_of_tickets

if 2500 < full_price <= 4000:
    discount = 0.10
    full_price *= (1 - discount)
elif full_price > 4000:
    discount = 0.25
    if trophy_photo == "Y":
        free_photo = True
    full_price *= (1 - discount)

if trophy_photo == "Y":
    if free_photo:
        pass
    else:
        full_price += (40 * number_of_tickets)

print(f"{full_price:.2f}")
