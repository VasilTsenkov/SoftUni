number_of_days = int(input())
hours_per_day = int(input())

price_per_hour = 0
total_bill = 0

for day in range(1, number_of_days + 1):

    price_per_day = 0

    for hour in range(1, hours_per_day + 1):

        if (day % 2 == 0) and (hour % 2 != 0):
            price_per_hour = 2.50
        elif (day % 2 != 0) and (hour % 2 == 0):
            price_per_hour = 1.25
        else:
            price_per_hour = 1

        price_per_day += price_per_hour

    total_bill += price_per_day

    print(f"Day: {day} - {price_per_day:.2f} leva")

else:
    print(f"Total: {total_bill:.2f} leva")
