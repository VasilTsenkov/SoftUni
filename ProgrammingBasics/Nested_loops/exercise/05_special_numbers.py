n = int(input())

for number in range(1111, 10_000):

    number_to_string = str(number)
    length_of_number = len(number_to_string)
    is_special = True

    for index in range(length_of_number):

        digit = int(number_to_string[index])

        if digit == 0:
            is_special = False
            break

        elif n % digit != 0:
            is_special = False
            break

    if is_special:
        print(number, end=" ")
