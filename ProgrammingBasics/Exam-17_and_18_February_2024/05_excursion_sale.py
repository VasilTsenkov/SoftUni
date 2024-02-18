number_of_sea_excursions = int(input())
number_of_mountain_excursions = int(input())

sea_excursion_price = 680
mountain_excursion_price = 499
firm_revenue = 0
everything_sold = False

while True:
    user_input = input()

    if user_input != "Stop":
        bought_packet = user_input
    else:
        break

    if bought_packet == "sea":

        if number_of_sea_excursions > 0:
            number_of_sea_excursions -= 1
            firm_revenue += sea_excursion_price

    elif bought_packet == "mountain":

        if number_of_mountain_excursions > 0:
            number_of_mountain_excursions -= 1
            firm_revenue += mountain_excursion_price

    if (number_of_sea_excursions == 0) and (number_of_mountain_excursions == 0):
        everything_sold = True
        break

if everything_sold:
    print("Good job! Everything is sold.")

print(f"Profit: {firm_revenue} leva.")
