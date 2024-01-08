price_vegetables = float(input())
price_fruits = float(input())
quantity_vegetables = int(input())
quantity_fruits = int(input())
euro = 1.94

total_vegetables = (price_vegetables * quantity_vegetables) / euro
total_fruits = (price_fruits * quantity_fruits) / euro
total_price = total_fruits + total_vegetables

print(f'{total_price:.2f}')
