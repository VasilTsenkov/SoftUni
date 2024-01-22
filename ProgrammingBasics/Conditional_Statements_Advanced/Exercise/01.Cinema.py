cinema_type = input()
rows_in_cinema = int(input())
columns_in_cinema = int(input())

ticket_price = 0

if cinema_type == 'Premiere':
    ticket_price = 12.00
elif cinema_type == 'Normal':
    ticket_price = 7.50
elif cinema_type == 'Discount':
    ticket_price = 5.00

revenue = rows_in_cinema * columns_in_cinema * ticket_price
print(f'{revenue:.2f} leva')
