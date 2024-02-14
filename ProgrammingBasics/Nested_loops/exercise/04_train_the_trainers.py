judges = int(input())

sum_average_grades = 0
given_average_grades = 0

while True:
    user_input = input()

    if user_input != "Finish":
        presentation = user_input
    else:
        break

    presentation_grade = 0
    average_grade = 0

    for _ in range(judges):
        grade_per_judge = float(input())

        presentation_grade += grade_per_judge

    average_grade = presentation_grade / judges
    sum_average_grades += average_grade
    given_average_grades += 1

    print(f"{presentation} - {average_grade:.2f}.")

final_assessment = sum_average_grades / given_average_grades

print(f"Student's final assessment is {final_assessment:.2f}.")
