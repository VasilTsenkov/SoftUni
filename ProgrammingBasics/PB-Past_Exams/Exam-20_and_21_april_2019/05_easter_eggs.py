from sys import maxsize

number_of_colored_eggs = int(input())

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
max_eggs_count = -maxsize
max_eggs_color = ""

for _ in range(number_of_colored_eggs):
    color_of_egg = input()

    if color_of_egg == "red":
        red_count += 1
    elif color_of_egg == "orange":
        orange_count += 1
    elif color_of_egg == "blue":
        blue_count += 1
    elif color_of_egg == "green":
        green_count += 1

    if red_count > max_eggs_count:
        max_eggs_count = red_count
        max_eggs_color = "red"

    if orange_count > max_eggs_count:
        max_eggs_count = orange_count
        max_eggs_color = "orange"

    if blue_count > max_eggs_count:
        max_eggs_count = blue_count
        max_eggs_color = "blue"

    if green_count > max_eggs_count:
        max_eggs_count = green_count
        max_eggs_color = "green"

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_eggs_count} -> {max_eggs_color}")
