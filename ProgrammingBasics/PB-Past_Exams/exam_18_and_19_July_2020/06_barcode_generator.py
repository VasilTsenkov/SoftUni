barcode_lower_bound = int(input())
barcode_upper_bound = int(input())

string_lower = str(barcode_lower_bound)
string_upper = str(barcode_upper_bound)

first_digit_lower = int(string_lower[0])
second_digit_lower = int(string_lower[1])
third_digit_lower = int(string_lower[2])
fourth_digit_lower = int(string_lower[3])

first_digit_upper = int(string_upper[0])
second_digit_upper = int(string_upper[1])
third_digit_upper = int(string_upper[2])
fourth_digit_upper = int(string_upper[3])

for first in range(first_digit_lower, first_digit_upper + 1):
    if first % 2 == 0:
        continue
    for second in range(second_digit_lower, second_digit_upper + 1):
        if second % 2 == 0:
            continue
        for third in range(third_digit_lower, third_digit_upper + 1):
            if third % 2 == 0:
                continue
            for fourth in range(fourth_digit_lower, fourth_digit_upper + 1):
                if fourth % 2 == 0:
                    continue
                print(f"{first}{second}{third}{fourth}", end=" ")
