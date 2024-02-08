kid_counter = 0
student_counter = 0
standard_counter = 0
all_tickets = 0

while True:
    film_name = input()
    if film_name == "Finish":
        break

    free_space = int(input())
    ticket_type = input()
    film_tickets = 0
    while ticket_type != "End":
        if ticket_type == "kid":
            kid_counter += 1
        elif ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1

        film_tickets += 1

        if free_space == film_tickets:
            break

        ticket_type = input()

    capacity = film_tickets / free_space
    all_tickets += film_tickets
    print(f"{film_name} - {capacity:.2%} full.")

student_percentage = student_counter / all_tickets
standard_percentage = standard_counter / all_tickets
kid_percentage = kid_counter / all_tickets

print(f"Total tickets: {all_tickets}")
print(f"{student_percentage:.2%} student tickets.")
print(f"{standard_percentage:.2%} standard tickets.")
print(f"{kid_percentage:.2%} kids tickets.")
