number_of_floors = int(input())
number_of_rooms = int(input())

room_type = ""

for floor in range(number_of_floors, 0, -1):
    for room in range(0, number_of_rooms):

        if floor == number_of_floors:
            room_type = "L"
        elif floor % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"

        print(f"{room_type}{floor}{room}", end=" ")

    print()
