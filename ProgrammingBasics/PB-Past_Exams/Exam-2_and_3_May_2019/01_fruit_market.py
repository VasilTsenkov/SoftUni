strawberry_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price * 0.50
oranges_price = raspberry_price * (1 - 0.40)
bananas_price = raspberry_price * (1 - 0.80)

strawberry_bill = strawberry_quantity * strawberry_price
bananas_bill = bananas_quantity * bananas_price
oranges_bill = oranges_quantity * oranges_price
raspberry_bill = raspberry_quantity * raspberry_price

total_bill = strawberry_bill + bananas_bill + oranges_bill + raspberry_bill

print(f"{total_bill:.2f}")
