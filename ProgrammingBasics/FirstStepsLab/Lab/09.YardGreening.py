yardSize = float(input())

GreeningPrice = yardSize * 7.61
discount = GreeningPrice * 0.18
finalPrice = GreeningPrice - discount

print(f"The final price is: {finalPrice} lv.")
print(f"The discount is: {discount} lv.")