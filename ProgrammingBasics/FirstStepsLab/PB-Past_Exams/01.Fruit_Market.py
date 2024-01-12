price_strawberry = float(input())
quantity_bananas = float(input())
quantity_orange = float(input())
quantity_malina = float(input())
quantity_strawberry = float(input())

price_malina = 0.5 * price_strawberry
price_orange = 0.6 * price_malina
price_bananas = 0.2 * price_malina

total_bill = price_strawberry * quantity_strawberry \
             + price_bananas * quantity_bananas \
             + price_orange * quantity_orange \
             + price_malina * quantity_malina

print(f"{total_bill:.2f}")
