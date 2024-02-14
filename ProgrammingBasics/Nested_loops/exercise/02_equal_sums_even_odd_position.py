first_number = int(input())
second_number = int(input())

for inbetween_number in range(first_number, second_number + 1):

    even_sum = 0
    odd_sum = 0

    number_to_string = str(inbetween_number)
    length = len(number_to_string)

    for index in range(length):
        if index % 2 == 0:
            even_sum += int(number_to_string[index])
        else:
            odd_sum += int(number_to_string[index])

    if even_sum == odd_sum:
        print(number_to_string, end=" ")
