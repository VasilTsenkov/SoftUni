cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width
pieces_taken = 0
user_typed_stop = False

while cake_pieces >= pieces_taken:
    user_input = input()

    if user_input != "STOP":
        pieces_taken_by_guest = int(user_input)
        pieces_taken += pieces_taken_by_guest
    else:
        user_typed_stop = True
        break

pieces_difference = abs(cake_pieces - pieces_taken)

if user_typed_stop:
    print(f"{pieces_difference} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_difference} pieces more.")
