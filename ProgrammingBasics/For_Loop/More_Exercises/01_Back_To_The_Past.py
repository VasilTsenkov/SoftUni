heritage = float(input())
year_final = int(input())

age = 18
life_cost = 0

for year in range(1800, year_final + 1):
    if year % 2 == 0:
        life_cost += 12000
        age += 1
    else:
        life_cost += (12000 + 50 * age)
        age += 1

difference = abs(heritage - life_cost)

if heritage >= life_cost:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")
