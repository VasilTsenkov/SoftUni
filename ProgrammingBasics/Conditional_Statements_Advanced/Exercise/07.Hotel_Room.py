month = input()
number_of_nights = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0.10

if (month == 'May') or (month == 'October'):
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights <= 14:
        discount = 0.05
        studio_price *= (1 - discount)
    elif number_of_nights > 14:
        discount = 0.30
        studio_price *= (1 - discount)
        apartment_price *= (1 - apartment_discount)
elif (month == 'June') or (month == 'September'):
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_discount = 0.20
        studio_price *= (1 - studio_discount)
        apartment_price *= (1 - apartment_discount)
elif (month == 'July') or (month == 'August'):
    studio_price = 76
    apartment_price = 77
    if number_of_nights > 14:
        apartment_price *= (1 - apartment_discount)

apartment_bill = apartment_price * number_of_nights
studio_bill = studio_price * number_of_nights

print(f'Apartment: {apartment_bill:.2f} lv.')
print(f'Studio: {studio_bill:.2f} lv.')
