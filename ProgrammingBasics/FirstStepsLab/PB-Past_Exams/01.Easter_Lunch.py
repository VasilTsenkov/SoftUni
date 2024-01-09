quantity_cake = int(input())
quantity_egg_boxes = int(input())
quantity_cookies = int(input())

price_cake = 3.20
price_egg_box = 4.35
price_cookie = 5.40
price_egg_paint = 0.15

bill_cake = quantity_cake * price_cake
bill_egg_boxes = price_egg_box * quantity_egg_boxes
bill_cookies = price_cookie * quantity_cookies
bill_egg_paint = quantity_egg_boxes * 12 * price_egg_paint
total_bill = bill_cake + bill_egg_boxes \
             + bill_cookies + bill_egg_paint

print(f'{total_bill:.2f}')
