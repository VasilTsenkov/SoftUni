season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

price_per_student = 0
discount = 0.00
sport = ""

if group_type == "girls":
    if season == "Winter":
        price_per_student = 9.60
        sport = "Gymnastics"
    elif season == "Spring":
        price_per_student = 7.20
        sport = "Athletics"
    elif season == "Summer":
        price_per_student = 15
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        price_per_student = 9.60
        sport = "Judo"
    elif season == "Spring":
        price_per_student = 7.20
        sport = "Tennis"
    elif season == "Summer":
        price_per_student = 15
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        price_per_student = 10.00
        sport = "Ski"
    elif season == "Spring":
        price_per_student = 9.50
        sport = "Cycling"
    elif season == "Summer":
        price_per_student = 20
        sport = "Swimming"

if 10 <= students_count < 20:
    discount = 0.05
elif 20 <= students_count < 50:
    discount = 0.15
elif students_count >= 50:
    discount = 0.50

price = (price_per_student * students_count * nights_count) * (1 - discount)

print(f"{sport} {price:.2f} lv.")
