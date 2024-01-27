kilometers = int(input())
time_of_day = input()

price = 0
tariff = 0

if kilometers < 20:
    price = 0.70
    if time_of_day == "day":
        tariff = 0.79
    elif time_of_day == "night":
        tariff = 0.90
elif kilometers < 100:
    tariff = 0.09
else:
    tariff = 0.06

total_bill = price + (tariff * kilometers)

print(f"{total_bill:.2f}")
