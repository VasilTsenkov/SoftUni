from sys import maxsize

n = int(input())

max_number = -maxsize
total_sum = 0

for _ in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    total_sum += number

sum_without_max = total_sum - max_number

if sum_without_max == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(sum_without_max - max_number)
    print("No")
    print(f"Diff = {difference}")
