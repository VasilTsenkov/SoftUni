student_count = 0
standard_count = 0
kid_count = 0
total_tickets = 0

while True:
    user_input = input()

    if user_input != "Finish":
        film_name = user_input
    else:
        break

    available_seats = int(input())
    tickets = 0

    for _ in range(available_seats):
        second_input = input()

        if second_input == "End":
            break
        else:
            ticket_type = second_input

        if ticket_type == "student":
            student_count += 1
        elif ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "kid":
            kid_count += 1

        tickets += 1

    film_interest = tickets / available_seats
    total_tickets += tickets

    print(f"{film_name} - {film_interest:.2%} full.")

student_percent = student_count / total_tickets
standard_percent = standard_count / total_tickets
kid_percent = kid_count / total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2%} student tickets.")
print(f"{standard_percent:.2%} standard tickets.")
print(f"{kid_percent:.2%} kids tickets.")
