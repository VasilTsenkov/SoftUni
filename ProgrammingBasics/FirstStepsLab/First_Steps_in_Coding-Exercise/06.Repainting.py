nailon = int(input())
boq = int(input())
razdelitel = int(input())
work_hours = int(input())
torbichki = 0.40

price_nailon = (nailon + 2) * 1.50
price_boq = (boq * 1.10) * 14.50
price_razdelitel = razdelitel * 5.00
material_expense = price_boq + price_razdelitel + price_nailon + torbichki
worker_pay = work_hours * (material_expense * 0.30)
total_expenses = material_expense + worker_pay

print(total_expenses)