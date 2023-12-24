loads = int(input())

tonsMicro = 0
tonsTruck = 0
tonsTrain = 0

for i in range(0, loads):
    tons = int(input())
    if tons <= 3:
        tonsMicro += tons
    elif 3 < tons <= 11:
        tonsTruck += tons
    elif tons > 11:
        tonsTrain += tons

totalTons = tonsMicro + tonsTruck + tonsTrain

print(f"{(tonsMicro * 200 + tonsTruck * 175 + tonsTrain * 120) / totalTons:.2f}")
print(f"{(tonsMicro / totalTons) * 100:.2f}%")
print(f"{(tonsTruck / totalTons) * 100:.2f}%")
print(f"{(tonsTrain / totalTons) * 100:.2f}%")