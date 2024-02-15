from sys import maxsize

player_with_most_goals = ""
most_goals = -maxsize
made_hat_trick = False

while True:
    user_input = input()

    if user_input != "END":
        player = user_input
    else:
        break

    number_of_goals = int(input())

    if number_of_goals >= 10:
        made_hat_trick = True
        player_with_most_goals = player
        most_goals = number_of_goals
        break
    elif number_of_goals >= 3:
        made_hat_trick = True

    if number_of_goals > most_goals:
        player_with_most_goals = player
        most_goals = number_of_goals

print(f"{player_with_most_goals} is the best player!")

if made_hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
