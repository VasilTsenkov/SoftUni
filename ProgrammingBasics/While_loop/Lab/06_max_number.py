from sys import maxsize

max_number = -maxsize

while True:
    user_input = input()

    if user_input == "Stop":
        break
    else:
        number = int(user_input)

    if number > max_number:
        max_number = number

print(max_number)
