number_of_students = int(input())

fail_count = 0
fair_count = 0
good_count = 0
top_student_count = 0
sum_of_grades = 0

for _ in range(number_of_students):
    exam_grade = float(input())

    if 2.00 <= exam_grade <= 2.99:
        fail_count += 1

    elif exam_grade <= 3.99:
        fair_count += 1

    elif exam_grade <= 4.99:
        good_count += 1

    else:
        top_student_count += 1

    sum_of_grades += exam_grade

top_student_percent = (top_student_count / number_of_students) * 100
good_percent = (good_count / number_of_students) * 100
fair_percent = (fair_count / number_of_students) * 100
fail_percent = (fail_count / number_of_students) * 100
average_grade = sum_of_grades / number_of_students

print(f"Top students: {top_student_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {fair_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
