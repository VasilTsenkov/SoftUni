trip_price = float(input())
quantity_puzzles = int(input())
quantity_dolls = int(input())
quantity_bears = int(input())
quantity_minions = int(input())
quantity_trucks = int(input())

price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

total_price = price_puzzle * quantity_puzzles + price_doll * quantity_dolls \
              + price_bear * quantity_bears + price_minion * quantity_minions \
              + price_truck * quantity_trucks

total_quantity = quantity_puzzles + quantity_dolls + quantity_bears \
                 + quantity_minions + quantity_trucks

if total_quantity >= 50:
    total_price *= 0.75

total_price_after_rent = total_price * 0.90

if total_price_after_rent >= trip_price:
    sum_left = total_price_after_rent - trip_price
    print(f'Yes! {sum_left:.2f} lv left.')
else:
    sum_needed = trip_price - total_price_after_rent
    print(f'Not enough money! {sum_needed:.2f} lv needed.')
