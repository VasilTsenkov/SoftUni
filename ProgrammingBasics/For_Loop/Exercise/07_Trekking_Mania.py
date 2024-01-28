climber_groups_count = int(input())

musala_count = 0
monblanc_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0
all_climbers = 0

for _ in range(climber_groups_count):
    climbers = int(input())

    if climbers <= 5:
        musala_count += climbers
    elif climbers <= 12:
        monblanc_count += climbers
    elif climbers <= 25:
        kilimandjaro_count += climbers
    elif climbers <= 40:
        k2_count += climbers
    else:
        everest_count += climbers

    all_climbers += climbers

musala_percentage = (musala_count / all_climbers) * 100
monblanc_percentage = (monblanc_count / all_climbers) * 100
kilimandjaro_percentage = (kilimandjaro_count / all_climbers) * 100
k2_percentage = (k2_count / all_climbers) * 100
everest_percentage = (everest_count / all_climbers) * 100

print(f"{musala_percentage:.2f}%")
print(f"{monblanc_percentage:.2f}%")
print(f"{kilimandjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
