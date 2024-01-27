from math import floor, ceil

vineyard_squares = int(input())
grapes_per_square = float(input())
needed_wine = int(input())
workers = int(input())

vineyard_used_for_wine = 0.40 * vineyard_squares
total_grapes_produced = vineyard_used_for_wine * grapes_per_square
wine_produced = total_grapes_produced / 2.5

difference = abs(needed_wine - wine_produced)

if wine_produced < needed_wine:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
else:
    wine_per_worker = difference / workers
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.")
