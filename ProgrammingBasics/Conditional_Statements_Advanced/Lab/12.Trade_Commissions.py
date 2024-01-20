city = input()
sales = float(input())

commission = 0.00

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission = 0.05
    elif sales <= 1000:
        commission = 0.07
    elif sales <= 10000:
        commission = 0.08
    else:
        commission = 0.12

elif city == 'Varna':
    if 0 <= sales <= 500:
        commission = 0.045
    elif sales <= 1000:
        commission = 0.075
    elif sales <= 10000:
        commission = 0.10
    else:
        commission = 0.13

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = 0.055
    elif sales <= 1000:
        commission = 0.08
    elif sales <= 10000:
        commission = 0.12
    else:
        commission = 0.145

if commission == 0.00 or sales < 0:
    print('error')
else:
    trade_commission = sales * commission
    print(f'{trade_commission:.2f}')
