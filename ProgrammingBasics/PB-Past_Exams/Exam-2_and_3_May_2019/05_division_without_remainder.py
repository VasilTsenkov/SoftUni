number_of_integers = int(input())

division_by_two = 0
division_by_three = 0
division_by_four = 0

for _ in range(number_of_integers):
    integer = int(input())

    if integer % 2 == 0:
        division_by_two += 1

    if integer % 3 == 0:
        division_by_three += 1

    if integer % 4 == 0:
        division_by_four += 1

percent_divisible_by_two = division_by_two / number_of_integers
percent_divisible_by_three = division_by_three / number_of_integers
percent_divisible_by_four = division_by_four / number_of_integers

print(f"{percent_divisible_by_two:.2%}")
print(f"{percent_divisible_by_three:.2%}")
print(f"{percent_divisible_by_four:.2%}")
