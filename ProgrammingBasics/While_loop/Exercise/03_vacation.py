vacation_cost = float(input())
budget = float(input())

spending_days = 0
total_days = 0
five_consecutive_days_of_spending = False

while vacation_cost > budget:
    decision = input()
    decision_sum = float(input())
    
    if decision == "spend":
        spending_days += 1
        budget -= decision_sum
        if budget < 0:
            budget = 0

    elif decision == "save":
        spending_days = 0
        budget += decision_sum

    total_days += 1

    if spending_days == 5:
        five_consecutive_days_of_spending = True
        break

if five_consecutive_days_of_spending:
    print("You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
