from sys import maxsize

number_of_pastry = int(input())

max_points = -maxsize
baker_with_most_points = ""

for _ in range(number_of_pastry):
    baker_name = input()
    baker_points = 0
    baker_has_most_points = False

    while True:
        user_input = input()

        if user_input != "Stop":
            points_for_pastry = int(user_input)
        else:
            print(f"{baker_name} has {baker_points} points.")
            if baker_has_most_points:
                print(f"{baker_name} is the new number 1!")
            break

        baker_points += points_for_pastry

        if baker_points > max_points:
            max_points = baker_points
            baker_with_most_points = baker_name
            baker_has_most_points = True

print(f"{baker_with_most_points} won competition with {max_points} points!")
