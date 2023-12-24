age = int(input())
priceDishwasher = float(input())
priceToy = int(input())

toys = 0
totalCash = 0
cash = 10.00

for i in range(1, age + 1):
    if i % 2 != 0:
        toys += 1
    else:
        totalCash += (cash - 1)
        cash += 10.00

savings = (toys * priceToy) + totalCash

if savings >= priceDishwasher:
    print(f"Yes! {savings - priceDishwasher:.2f}")
else:
    print(f"No! {priceDishwasher - savings:.2f}")
