film = input()
days = int(input())
tickets = int(input())
price_tickets = float(input())
cinema_percent = int(input()) / 100

revenue_per_day = tickets * price_tickets
total_revenue = revenue_per_day * days
cinema_revenue = total_revenue * cinema_percent
studio_revenue = total_revenue - cinema_revenue

print(f"The profit from the movie {film} is {studio_revenue:.2f} lv.")
