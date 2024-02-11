from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

winner_count = 0
points = 0
sum_points = 0

for _ in range(number_of_tournaments):
    tournament_stage = input()

    if tournament_stage == "W":
        points = 2000
        winner_count += 1
    elif tournament_stage == "F":
        points = 1200
    elif tournament_stage == "SF":
        points = 720

    sum_points += points
    starting_points += points

final_percent = winner_count / number_of_tournaments
average_points = sum_points / number_of_tournaments

print(f"Final points: {starting_points}")
print(f"Average points: {floor(average_points)}")
print(f"{final_percent:.2%}")
