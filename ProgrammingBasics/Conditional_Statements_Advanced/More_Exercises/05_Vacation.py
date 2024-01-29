budget = float(input())
season = input()

location = ""
stay_type = ""
price = 0

if budget <= 1000:
    stay_type = "Camp"
    if season == "Summer":
        price = 0.65 * budget
        location = "Alaska"
    elif season == "Winter":
        price = 0.45 * budget
        location = "Morocco"
elif budget <= 3000:
    stay_type = "Hut"
    if season == "Summer":
        price = 0.80 * budget
        location = "Alaska"
    elif season == "Winter":
        price = 0.60 * budget
        location = "Morocco"
else:
    stay_type = "Hotel"
    price = 0.90 * budget
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {stay_type} - {price:.2f}")
