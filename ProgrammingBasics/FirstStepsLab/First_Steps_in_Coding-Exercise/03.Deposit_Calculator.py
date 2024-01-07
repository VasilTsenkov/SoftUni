deposit = float(input())
months = int(input())
interest_rate = float(input()) / 100

amount = deposit + months * ((deposit * interest_rate) / 12)

print(amount)
