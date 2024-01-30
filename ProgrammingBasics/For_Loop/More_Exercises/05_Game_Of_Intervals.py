moves_number = int(input())

points = 0
count_0_to_9 = 0
count_10_to_19 = 0
count_20_to_29 = 0
count_30_to_39 = 0
count_40_to_50 = 0
count_invalid = 0

for _ in range(moves_number):
    number = int(input())

    if 0 <= number <= 9:
        points += (0.20 * number)
        count_0_to_9 += 1
    elif 10 <= number <= 19:
        points += (0.30 * number)
        count_10_to_19 += 1
    elif 20 <= number <= 29:
        points += (0.40 * number)
        count_20_to_29 += 1
    elif 30 <= number <= 39:
        points += 50
        count_30_to_39 += 1
    elif 40 <= number <= 50:
        points += 100
        count_40_to_50 += 1
    else:
        count_invalid += 1
        points /= 2

percentage_0_to_9 = count_0_to_9 / moves_number
percentage_10_to_19 = count_10_to_19 / moves_number
percentage_20_to_29 = count_20_to_29 / moves_number
percentage_30_to_39 = count_30_to_39 / moves_number
percentage_40_to_50 = count_40_to_50 / moves_number
percentage_invalid = count_invalid / moves_number

print(f"{points:.2f}")
print(f"From 0 to 9: {percentage_0_to_9:.2%}")
print(f"From 10 to 19: {percentage_10_to_19:.2%}")
print(f"From 20 to 29: {percentage_20_to_29:.2%}")
print(f"From 30 to 39: {percentage_30_to_39:.2%}")
print(f"From 40 to 50: {percentage_40_to_50:.2%}")
print(f"Invalid numbers: {percentage_invalid:.2%}")
