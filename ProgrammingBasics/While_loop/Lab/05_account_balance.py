account_balance = 0

while True:
    text = input()

    if text == "NoMoreMoney":
        break
    else:
        deposit = float(text)

    if deposit >= 0:
        account_balance += deposit
        print(f"Increase: {deposit:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {account_balance:.2f}")
