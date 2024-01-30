months_number = int(input())

total_electricity_bill = 0
water_bill = 20
internet_bill = 15
total_misc_bill = 0
total_water_bill = water_bill * months_number
total_internet_bill = internet_bill * months_number

for _ in range(months_number):
    electricity_bill = float(input())

    total_electricity_bill += electricity_bill
    misc_bill = (electricity_bill + water_bill + internet_bill) * 1.20
    total_misc_bill += misc_bill

average_bill = (total_internet_bill + total_water_bill + total_electricity_bill + total_misc_bill) / months_number

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_misc_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
