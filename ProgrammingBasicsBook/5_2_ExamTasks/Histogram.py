n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
currV1 = 0
currV2= 0
currV3 = 0
currV4 = 0
currV5 = 0

for i in range(0, n):
    v = int(input())
    if v < 200:
        currV1 += 1
        p1 = (currV1 / n) * 100
    elif 200 <= v <= 399:
        currV2 += 1
        p2 = (currV2 / n) * 100
    elif 400 <= v <= 599:
        currV3 += 1
        p3 = (currV3 / n) * 100
    elif 600 <= v <= 799:
        currV4 += 1
        p4 = (currV4 / n) * 100
    else:
        currV5 += 1
        p5 = (currV5 / n) * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")
