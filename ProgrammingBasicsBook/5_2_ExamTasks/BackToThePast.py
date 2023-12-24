cash = float(input())
year = int(input())
years = 18

totalEvenExpense = 0.00
totalOddExpense = 0.00

for i in range(1800, year + 1):
    if i % 2 == 0:
        evenExpense = 12000.00
        totalEvenExpense += evenExpense
    else:
        oddExpense = 12000 + (years * 50)
        totalOddExpense += oddExpense
    years += 1

totalExpense = totalOddExpense + totalEvenExpense

print((f"Yes! He will live a carefree life and will have {cash - totalExpense:.2f} dollars left.")
    if cash >= totalExpense
    else (f"He will need {totalExpense - cash:.2f} dollars to survive."))
