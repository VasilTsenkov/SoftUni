integer = int(input())

integer_ends_in_five = False
integer_divides_by_three = False
found_combination = False

if integer % 10 == 5:
    integer_ends_in_five = True

if integer % 3 == 0:
    integer_divides_by_three = True

for a in range(1, 10):
    for b in range(9, (a - 1), -1):
        for c in range(0, 10):
            for d in range(9, (c - 1), -1):
                sum_of_combination = a + b + c + d
                product_of_combination = a * b * c * d

                if (sum_of_combination == product_of_combination) and integer_ends_in_five:
                    found_combination = True
                    print(f"{a}{b}{c}{d}")
                    break
                elif (product_of_combination // sum_of_combination == 3) and integer_divides_by_three:
                    found_combination = True
                    print(f"{d}{c}{b}{a}")
                    break

            if found_combination:
                break

        if found_combination:
            break

    if found_combination:
        break

if found_combination is False:
    print("Nothing found")
