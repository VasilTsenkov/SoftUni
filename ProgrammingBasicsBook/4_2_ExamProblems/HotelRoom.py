month = str(input()).lower()
nights = int(input())

FullPriceStudio = 0.00
FullPriceAp = 0.00

if month == "may" or month == "october":
    studio_price = 50
    ap_price = 65
    if 7 < nights <= 14:
        studio_price = studio_price * 0.95
    elif nights > 14:
        studio_price *= 0.70
        ap_price *= 0.90
    FullPriceStudio = studio_price * nights
    FullPriceAp = ap_price * nights
elif month == "june" or month == "september":
    studio_price = 75.20
    ap_price = 68.70
    if nights > 14:
        studio_price *= 0.80
        ap_price *= 0.90
    FullPriceStudio = studio_price * nights
    FullPriceAp = ap_price * nights
elif month == "july" or month == "august":
    studio_price = 76
    ap_price = 77
    if nights > 14:
        ap_price *= 0.90
    FullPriceStudio = studio_price * nights
    FullPriceAp = ap_price * nights

print(f"Apartment: {FullPriceAp:.2f} lv.")
print(f"Studio: {FullPriceStudio:.2f} lv.")
