flour_price = float(input())
flour_quantity = float(input())
sugar_quantity = float(input())
egg_boxes_quantity = int(input())
yeast_quantity = int(input())

sugar_price = flour_price * (1 - 0.25)
egg_boxes_price = flour_price * (1 + 0.10)
yeast_price = sugar_price * (1 - 0.80)

flour_bill = flour_price * flour_quantity
sugar_bill = sugar_price * sugar_quantity
egg_boxes_bill = egg_boxes_price * egg_boxes_quantity
yeast_bill = yeast_price * yeast_quantity

total_costs = flour_bill + sugar_bill + egg_boxes_bill + yeast_bill

print(f"{total_costs:.2f}")
