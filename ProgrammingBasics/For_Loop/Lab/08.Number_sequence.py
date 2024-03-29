from sys import maxsize

n = int(input())

max_number = -maxsize
min_number = maxsize

for _ in range(0, n):
    number = int(input())

    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
