pens_needed = int(input())
markers_needed = int(input())
belina_needed = int(input())
discount = int(input()) / 100

price_pens = pens_needed * 5.80
price_markers = markers_needed * 7.20
price_belina = belina_needed * 1.20
full_price = price_pens + price_markers + price_belina
discount_price = full_price * (1 - discount)

print(discount_price)
