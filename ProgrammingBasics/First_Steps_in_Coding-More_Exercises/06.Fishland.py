price_skumriq = float(input())
price_caca = float(input())
quantity_palamud = float(input())
quantity_safrid = float(input())
quantity_midi = int(input())

price_palamud = price_skumriq + (price_skumriq * 0.6)
price_safrid = price_caca + (price_caca * 0.80)
price_midi = 7.50
total_pay = (price_palamud * quantity_palamud
             + price_safrid * quantity_safrid
             + price_midi * quantity_midi)

print(f'{total_pay:.2f}')
