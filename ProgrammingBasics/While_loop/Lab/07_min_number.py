from sys import maxsize

min_number = maxsize

while True:
    user_input = input()

    if user_input == "Stop":
        break
    else:
        number = int(user_input)

    if number < min_number:
        min_number = number

print(min_number)
