shirt_price = float(input())
target_sum = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
boots_price = (shirt_price + shorts_price) * 2
discount = 0.15

total_bill = (shirt_price + shorts_price + socks_price + boots_price) * (1 - discount)

if total_bill >= target_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_bill:.2f} lv.")
else:
    difference = target_sum - total_bill
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
