n = int(input())

combination_counter = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            x_sum = x1 + x2 + x3

            if x_sum == n:
                combination_counter += 1

print(combination_counter)
