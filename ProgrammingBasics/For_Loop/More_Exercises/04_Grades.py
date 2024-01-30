student_count = int(input())

sum_grade = 0
fail_grade = 0
fair_grade = 0
good_grade = 0
top_grade = 0

for _ in range(student_count):
    grade = float(input())
    sum_grade += grade

    if 2 <= grade <= 2.99:
        fail_grade += 1
    elif grade <= 3.99:
        fair_grade += 1
    elif grade <= 4.99:
        good_grade += 1
    elif grade <= 6.00:
        top_grade += 1

average_grade = sum_grade / student_count
fail_percentage = fail_grade / student_count
fair_percentage = fair_grade / student_count
good_percentage = good_grade / student_count
top_percentage = top_grade / student_count

print(f"Top students: {top_percentage:.2%}")
print(f"Between 4.00 and 4.99: {good_percentage:.2%}")
print(f"Between 3.00 and 3.99: {fair_percentage:.2%}")
print(f"Fail: {fail_percentage:.2%}")
print(f"Average: {average_grade:.2f}")
