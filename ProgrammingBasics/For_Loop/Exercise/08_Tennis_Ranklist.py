from math import floor

tournament_participation = int(input())
points_starting = int(input())

winner_count = 0
winner_points = 0
finalist_points = 0
semi_final_points = 0

for _ in range(tournament_participation):
    tournament_stage = input()
    if tournament_stage == "W":
        points_starting += 2000
        winner_points += 2000
        winner_count += 1
    elif tournament_stage == "F":
        points_starting += 1200
        finalist_points += 1200
    elif tournament_stage == "SF":
        points_starting += 720
        semi_final_points += 720


average_points = (winner_points + finalist_points + semi_final_points) / tournament_participation
winner_percentage = winner_count / tournament_participation

print(f"Final points: {points_starting}")
print(f"Average points: {floor(average_points)}")
print(f"{winner_percentage:.2%}")
