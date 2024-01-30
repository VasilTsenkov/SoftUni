stadium_capacity = int(input())
fans_number = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for _ in range(fans_number):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

percentage_sector_a = sector_a / fans_number
percentage_sector_b = sector_b / fans_number
percentage_sector_v = sector_v / fans_number
percentage_sector_g = sector_g / fans_number
percentage_fans = fans_number / stadium_capacity

print(f"{percentage_sector_a:.2%}")
print(f"{percentage_sector_b:.2%}")
print(f"{percentage_sector_v:.2%}")
print(f"{percentage_sector_g:.2%}")
print(f"{percentage_fans:.2%}")
