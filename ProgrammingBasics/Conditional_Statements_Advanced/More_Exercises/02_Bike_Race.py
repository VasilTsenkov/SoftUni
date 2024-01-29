junior_participants = int(input())
senior_participants = int(input())
trace_type = input()

junior_tax = 0
senior_tax = 0
extra_discount = 0
cost_percentage = 0.05

if trace_type == "trail":
    junior_tax = 5.50
    senior_tax = 7
elif trace_type == "cross-country":
    junior_tax = 8
    senior_tax = 9.50
elif trace_type == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
elif trace_type == "road":
    junior_tax = 20
    senior_tax = 21.50

total_sum = (junior_participants * junior_tax) + (senior_participants * senior_tax)

if (junior_participants + senior_participants) >= 50 and trace_type == "cross-country":
    extra_discount = 0.25
    total_sum *= (1 - extra_discount)

donation = total_sum * (1 - cost_percentage)

print(f"{donation:.2f}")
