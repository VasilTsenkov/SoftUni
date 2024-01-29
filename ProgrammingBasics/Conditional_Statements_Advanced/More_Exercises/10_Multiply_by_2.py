number = 1

while number >= 0:
    number = float(input())
    number *= 2
    if number < 0:
        print("Negative number!")
        break

    print(f"Result: {number:.2f}")
