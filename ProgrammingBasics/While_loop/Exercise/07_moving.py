room_width = int(input())
room_length = int(input())
room_height = int(input())

room_available = room_width * room_length * room_height
boxes_size = 0
user_typed_done = False

while room_available > boxes_size:
    user_input = input()

    if user_input != "Done":
        box_size = int(user_input)
        boxes_size += box_size
    else:
        user_typed_done = True
        break

size_difference = abs(room_available - boxes_size)

if user_typed_done:
    print(f"{size_difference} Cubic meters left.")
else:
    print(f"No more free space! You need {size_difference} Cubic meters more.")
