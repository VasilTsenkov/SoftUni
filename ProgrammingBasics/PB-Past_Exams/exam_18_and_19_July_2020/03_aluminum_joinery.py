number_of_joinery = int(input())
type_of_joinery = input()
shipment_method = input()

if number_of_joinery >= 10:

    joinery_price = 0
    discount = 0.00
    payment = 0

    if type_of_joinery == "90X130":
        joinery_price = 110

        if number_of_joinery > 60:
            discount = 0.08
        elif number_of_joinery > 30:
            discount = 0.05

    elif type_of_joinery == "100X150":
        joinery_price = 140

        if number_of_joinery > 80:
            discount = 0.10
        elif number_of_joinery > 40:
            discount = 0.06

    elif type_of_joinery == "130X180":
        joinery_price = 190

        if number_of_joinery > 50:
            discount = 0.12
        elif number_of_joinery > 20:
            discount = 0.07

    elif type_of_joinery == "200X300":
        joinery_price = 250

        if number_of_joinery > 50:
            discount = 0.14
        elif number_of_joinery > 25:
            discount = 0.09

    payment = (joinery_price * number_of_joinery) * (1 - discount)

    if shipment_method == "With delivery":
        delivery = 60
        payment += delivery

    if number_of_joinery > 99:
        additional_discount = 0.04
        payment *= (1 - additional_discount)

    print(f"{payment:.2f} BGN")

else:
    print("Invalid order")
