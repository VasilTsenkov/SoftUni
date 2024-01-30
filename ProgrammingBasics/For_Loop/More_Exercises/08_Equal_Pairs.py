from sys import maxsize

numbers_count = int(input())
first_number = int(input())
second_number = int(input())

max_sum = -maxsize
current_sum = first_number + second_number
difference = 0

for i in range(numbers_count - 1):
    first_number = int(input())
    second_number = int(input())

    previous_sum = current_sum
    current_sum = first_number + second_number
    difference = abs(current_sum - previous_sum)

    if difference > max_sum:
        max_sum = difference


if difference == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={max_sum}")
