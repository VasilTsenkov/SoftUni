prime_numbers_sum = 0
non_prime_numbers_sum = 0

while True:
    is_prime = True

    user_input = input()

    if user_input != "stop":
        number = int(user_input)
    else:
        break

    if number < 0:
        print("Number is negative.")
        continue

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += number
    else:
        non_prime_numbers_sum += number

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
