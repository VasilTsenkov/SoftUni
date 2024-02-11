visitors = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
shake_count = 0
bar_count = 0

for _ in range(visitors):
    activity = input()

    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        shake_count += 1
    elif activity == "Protein bar":
        bar_count += 1

work_out = back_count + chest_count + legs_count + abs_count
work_out_percentage = work_out / visitors
protein_percentage = (shake_count + bar_count) / visitors

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{shake_count} - protein shake")
print(f"{bar_count} - protein bar")
print(f"{work_out_percentage:.2%} - work out")
print(f"{protein_percentage:.2%} - protein")
