company_name = input()
adult_tickets_count = int(input())
kids_tickets_count = int(input())
adult_ticket_price = float(input())
service_cost = float(input())

kids_ticket_price = (0.30 * adult_ticket_price) + service_cost
adult_ticket_price += service_cost

revenue_from_tickets = (adult_ticket_price * adult_tickets_count) + (kids_ticket_price * kids_tickets_count)
agency_revenue = 0.20 * revenue_from_tickets

print(f"The profit of your agency from {company_name} tickets is {agency_revenue:.2f} lv.")
