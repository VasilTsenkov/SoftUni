budget = float(input())
season = str(input()).lower()

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        price = budget * 0.30
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price = budget * 0.70
        print(f"Hotel - {price:.2f}")
elif 100 < budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        price = budget * 0.40
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price = budget * 0.80
        print(f"Hotel - {price:.2f}")
elif budget > 1000:
    price = budget * 0.90
    print(f"Somewhere in Europe \nHotel - {price:.2f}")
