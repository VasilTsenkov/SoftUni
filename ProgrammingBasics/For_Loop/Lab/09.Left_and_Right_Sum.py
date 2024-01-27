n = int(input())

left_sum = 0
right_sum = 0

for _ in range(0, n):
    left_numbers = int(input())
    left_sum += left_numbers

for _ in range(0, n):
    right_numbers = int(input())
    right_sum += right_numbers

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
