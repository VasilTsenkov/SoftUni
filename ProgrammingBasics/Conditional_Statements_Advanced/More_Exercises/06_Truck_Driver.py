season = input()
kilometers_per_month = float(input())

tariff_per_kilometer = 0
tax = 0.10

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        tariff_per_kilometer = 0.75
    elif season == "Summer":
        tariff_per_kilometer = 0.90
    elif season == "Winter":
        tariff_per_kilometer = 1.05
elif kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        tariff_per_kilometer = 0.95
    elif season == "Summer":
        tariff_per_kilometer = 1.10
    elif season == "Winter":
        tariff_per_kilometer = 1.25
else:
    tariff_per_kilometer = 1.45

salary = (tariff_per_kilometer * kilometers_per_month * 4) * (1 - tax)

print(f"{salary:.2f}")
