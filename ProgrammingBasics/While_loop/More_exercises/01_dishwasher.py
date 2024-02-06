detergent_bottles = int(input())

detergent_per_bottle = 750
detergent_per_dish = 5
detergent_per_pan = 15
counter_for_pans = 1
total_dishes = 0
total_pans = 0

detergent_quantity = detergent_bottles * detergent_per_bottle
detergent_needed = 0
user_is_done = False

while detergent_quantity >= detergent_needed:
    user_input = input()

    if user_input != "End":
        if counter_for_pans % 3 != 0:
            dishes = int(user_input)
            total_dishes += dishes
            detergent_needed += dishes * detergent_per_dish
        else:
            pans = int(user_input)
            total_pans += pans
            detergent_needed += pans * detergent_per_pan
    else:
        user_is_done = True
        break

    counter_for_pans += 1

difference_detergent = abs(detergent_quantity - detergent_needed)

if user_is_done or (detergent_quantity >= detergent_needed):
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pans} pots were washed.")
    print(f"Leftover detergent {difference_detergent} ml.")
else:
    print(f"Not enough detergent, {difference_detergent} ml. more necessary!")
