actor_name = input()
academy_points = float(input())
voters_count = int(input())

needed_points = 1250.5

for _ in range(voters_count):
    voter_name = input()
    voter_points = float(input())
    length_of_name_points = len(voter_name)
    total_points_from_one_voter = (length_of_name_points * voter_points) / 2
    academy_points += total_points_from_one_voter

    if academy_points > needed_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    points_difference = needed_points - academy_points
    print(f"Sorry, {actor_name} you need {points_difference:.1f} more!")
