film_name = input()
cinema_room = input()
bought_tickets = int(input())

price = 0

if cinema_room == "normal":
    if film_name == "A Star Is Born":
        price = 7.5
    elif film_name == "Bohemian Rhapsody":
        price = 7.35
    elif film_name == "Green Book":
        price = 8.15
    elif film_name == "The Favourite":
        price = 8.75

elif cinema_room == "luxury":
    if film_name == "A Star Is Born":
        price = 10.5
    elif film_name == "Bohemian Rhapsody":
        price = 9.45
    elif film_name == "Green Book":
        price = 10.25
    elif film_name == "The Favourite":
        price = 11.55

elif cinema_room == "ultra luxury":
    if film_name == "A Star Is Born":
        price = 13.5
    elif film_name == "Bohemian Rhapsody":
        price = 12.75
    elif film_name == "Green Book":
        price = 13.25
    elif film_name == "The Favourite":
        price = 13.95

revenue = price * bought_tickets

print(f"{film_name} -> {revenue:.2f} lv.")
