size_of_egg = input()
color_of_egg = input()
number_of_egg_boxes = int(input())

sale_price_of_egg_box = 0

if color_of_egg == "Red":
    if size_of_egg == "Large":
        sale_price_of_egg_box = 16
    elif size_of_egg == "Medium":
        sale_price_of_egg_box = 13
    elif size_of_egg == "Small":
        sale_price_of_egg_box = 9

elif color_of_egg == "Green":
    if size_of_egg == "Large":
        sale_price_of_egg_box = 12
    elif size_of_egg == "Medium":
        sale_price_of_egg_box = 9
    elif size_of_egg == "Small":
        sale_price_of_egg_box = 8

elif color_of_egg == "Yellow":
    if size_of_egg == "Large":
        sale_price_of_egg_box = 9
    elif size_of_egg == "Medium":
        sale_price_of_egg_box = 7
    elif size_of_egg == "Small":
        sale_price_of_egg_box = 5

revenue = sale_price_of_egg_box * number_of_egg_boxes
costs = revenue * 0.35
net_income = revenue - costs

print(f"{net_income:.2f} leva.")
