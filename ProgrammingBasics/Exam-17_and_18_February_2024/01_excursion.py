number_of_people = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())

night_price = 20.00
transport_card_price = 1.60
museum_ticket_price = 6.00

nights_bill_per_person = number_of_nights * night_price
transport_bill_per_person = number_of_transport_cards * transport_card_price
museum_tickets_bill_per_person = number_of_museum_tickets * museum_ticket_price

total_bill_per_person = nights_bill_per_person + transport_bill_per_person + museum_tickets_bill_per_person
total_bill_for_group = total_bill_per_person * number_of_people

unexpected_costs = total_bill_for_group * 0.25

total_bill_for_group += unexpected_costs

print(f"{total_bill_for_group:.2f}")
