contract_duration = input()
contract_type = input()
add_mobile_internet = input()
number_of_payment_months = int(input())

contract_price = 0
mobile_internet_price = 0

if contract_duration == "one":
    if contract_type == "Small":
        contract_price = 9.98
    elif contract_type == "Middle":
        contract_price = 18.99
    elif contract_type == "Large":
        contract_price = 25.98
    elif contract_type == "ExtraLarge":
        contract_price = 35.99

elif contract_duration == "two":
    if contract_type == "Small":
        contract_price = 8.58
    elif contract_type == "Middle":
        contract_price = 17.09
    elif contract_type == "Large":
        contract_price = 23.59
    elif contract_type == "ExtraLarge":
        contract_price = 31.79

if add_mobile_internet == "yes":
    if contract_price <= 10.00:
        mobile_internet_price = 5.50
    elif contract_price <= 30:
        mobile_internet_price = 4.35
    else:
        mobile_internet_price = 3.85

    contract_price += mobile_internet_price

if contract_duration == "two":
    additional_discount = 0.0375
    contract_price *= (1 - additional_discount)

total_contract_price = contract_price * number_of_payment_months

print(f"{total_contract_price:.2f} lv.")
