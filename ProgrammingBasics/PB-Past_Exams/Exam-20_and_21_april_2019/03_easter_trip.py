destination = input()
reserved_dates = input()
nights_booked = int(input())

price_per_night = 0

if destination == "France":
    if reserved_dates == "21-23":
        price_per_night = 30
    elif reserved_dates == "24-27":
        price_per_night = 35
    elif reserved_dates == "28-31":
        price_per_night = 40

elif destination == "Italy":
    if reserved_dates == "21-23":
        price_per_night = 28
    elif reserved_dates == "24-27":
        price_per_night = 32
    elif reserved_dates == "28-31":
        price_per_night = 39

elif destination == "Germany":
    if reserved_dates == "21-23":
        price_per_night = 32
    elif reserved_dates == "24-27":
        price_per_night = 37
    elif reserved_dates == "28-31":
        price_per_night = 43

total_cost = price_per_night * nights_booked

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")
