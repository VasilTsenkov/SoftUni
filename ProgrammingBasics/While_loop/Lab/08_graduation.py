student_name = input()

school_year = 0
total_grades = 0
failed_years = 0

while school_year < 12:
    year_grade = float(input())

    if year_grade >= 4.00:
        school_year += 1
        total_grades += year_grade
    else:
        failed_years += 1

    if failed_years > 1:
        print(f"{student_name} has been excluded at {school_year + 1} grade")
        break
else:
    average_grade = total_grades / school_year
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
