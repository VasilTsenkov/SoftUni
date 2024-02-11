darts_player = input()

successful_shots = 0
unsuccessful_shots = 0
starting_points = 301
player_won = False

while True:
    user_input = input()

    if user_input != "Retire":
        sector = user_input
    else:
        break

    points = int(input())

    if sector == "Double":
        points *= 2
    elif sector == "Triple":
        points *= 3

    if points > starting_points:
        unsuccessful_shots += 1
    else:
        successful_shots += 1
        starting_points -= points

    if starting_points == 0:
        player_won = True
        break

if player_won:
    print(f"{darts_player} won the leg with {successful_shots} shots.")
else:
    print(f"{darts_player} retired after {unsuccessful_shots} unsuccessful shots.")
