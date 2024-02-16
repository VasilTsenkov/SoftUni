pastry_quantity = int(input())
egg_boxes_quantity = int(input())
cookies_quantity = int(input())

pastry_price = 3.20
egg_box_price = 4.35
cookies_price_per_kilo = 5.40
paint_per_egg = 0.15

pastry_bill = pastry_quantity * pastry_price
egg_box_bill = egg_boxes_quantity * egg_box_price
cookies_bill = cookies_quantity * cookies_price_per_kilo
paint_bill = 12 * egg_boxes_quantity * 0.15

total_cost = pastry_bill + egg_box_bill + cookies_bill + paint_bill

print(f"{total_cost:.2f}")
