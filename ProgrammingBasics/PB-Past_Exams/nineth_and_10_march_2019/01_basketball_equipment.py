annual_fee = int(input())

sneakers = 0.60 * annual_fee
jersey = 0.80 * sneakers
ball = 0.25 * jersey
miscellaneous = 0.20 * ball

total_costs = annual_fee + sneakers + jersey + ball + miscellaneous

print(f"{total_costs:.2f}")
