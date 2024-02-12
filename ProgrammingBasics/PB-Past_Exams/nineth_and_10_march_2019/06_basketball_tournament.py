end_of_tournaments = False
matches_counter = 0
win_counter = 0
loss_counter = 0

while True:
    user_input = input()

    if user_input != "End of tournaments":
        tournament_name = user_input
    else:
        end_of_tournaments = True
        break

    number_of_matches = int(input())

    matches_counter += number_of_matches

    for game in range(1, number_of_matches + 1):
        score_of_team1 = int(input())
        score_of_team2 = int(input())

        score_difference = abs(score_of_team1 - score_of_team2)

        if score_of_team1 > score_of_team2:
            win_counter += 1
            print(f"Game {game} of tournament {tournament_name}: win with {score_difference} points.")
        else:
            loss_counter += 1
            print(f"Game {game} of tournament {tournament_name}: lost with {score_difference} points.")

win_percent = win_counter / matches_counter
loss_percent = loss_counter / matches_counter

if end_of_tournaments:
    print(f"{win_percent:.2%} matches win")
    print(f"{loss_percent:.2%} matches lost")
