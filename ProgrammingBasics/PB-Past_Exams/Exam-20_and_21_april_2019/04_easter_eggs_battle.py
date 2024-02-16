player1_egg_count = int(input())
player2_egg_count = int(input())

while True:
    user_input = input()

    if user_input != "End":
        winner = user_input
    else:
        print(f"Player one has {player1_egg_count} eggs left.")
        print(f"Player two has {player2_egg_count} eggs left.")
        break

    if winner == "one":
        player2_egg_count -= 1
    elif winner == "two":
        player1_egg_count -= 1

    if player1_egg_count == 0:
        print(f"Player one is out of eggs. Player two has {player2_egg_count} eggs left.")
        break
    elif player2_egg_count == 0:
        print(f"Player two is out of eggs. Player one has {player1_egg_count} eggs left.")
        break
