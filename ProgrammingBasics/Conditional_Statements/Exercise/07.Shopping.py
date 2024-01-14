budget = float(input())
quantity_video_cards = int(input())
quantity_CPU = int(input())
quantity_RAM = int(input())

price_video_card = 250
total_sum_VC = price_video_card * quantity_video_cards
price_CPU = 0.35 * total_sum_VC
total_sum_CPU = price_CPU * quantity_CPU
price_RAM = 0.10 * total_sum_VC
total_sum_RAM = price_RAM * quantity_RAM

total_price = total_sum_VC + total_sum_CPU + total_sum_RAM

if quantity_video_cards > quantity_CPU:
    total_price *= 0.85

if budget >= total_price:
    budget_left = budget - total_price
    print(f'You have {budget_left:.2f} leva left!')
else:
    budget_exceeded = total_price - budget
    print(f'Not enough money! You need {budget_exceeded:.2f} leva more!')
