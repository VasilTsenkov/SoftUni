interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_counter = 0
found_magic_number = False

for first_number in range(interval_start, interval_end + 1):
    for second_number in range(interval_start, interval_end + 1):

        combination_counter += 1
        number_sum = first_number + second_number

        if number_sum == magic_number:
            found_magic_number = True
            print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
            break

    if found_magic_number:
        break

else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
