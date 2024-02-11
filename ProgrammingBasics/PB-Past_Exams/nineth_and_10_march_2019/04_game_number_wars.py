player_1 = input()
player_2 = input()

score_player_1 = 0
score_player_2 = 0
end_of_game = False

while True:
    user_input = input()

    if user_input != "End of game":
        card_1 = int(user_input)
    else:
        end_of_game = True
        break

    card_2 = int(input())

    if card_1 > card_2:
        score_player_1 += (card_1 - card_2)
    elif card_1 < card_2:
        score_player_2 += (card_2 - card_1)
    else:
        print("Number wars!")

        card_1 = int(input())
        card_2 = int(input())

        if card_1 > card_2:
            print(f"{player_1} is winner with {score_player_1} points")
        elif card_1 < card_2:
            print(f"{player_2} is winner with {score_player_2} points")

        break

if end_of_game:
    print(f"{player_1} has {score_player_1} points")
    print(f"{player_2} has {score_player_2} points")
