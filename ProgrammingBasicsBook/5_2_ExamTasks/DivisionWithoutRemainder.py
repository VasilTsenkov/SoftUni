n = int(input())

count2 = 0
count3 = 0
count4 = 0

for i in range(0, n):
    v = int(input())
    if v % 2 == 0:
        count2 += 1
    if v % 3 == 0:
        count3 += 1
    if v % 4 == 0:
        count4 += 1

print(f"{(count2 / n) * 100:.2f}%")
print(f"{(count3 / n) * 100:.2f}%")
print(f"{(count4 / n) * 100:.2f}%")
