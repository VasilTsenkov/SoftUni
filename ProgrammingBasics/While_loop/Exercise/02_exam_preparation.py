number_of_fails_allowed = int(input())

failed_tasks = 0
sum_of_grades = 0
number_of_problems = 0
last_problem_name = ""

while failed_tasks < number_of_fails_allowed:

    task_name = input()
    if task_name == "Enough":
        break

    task_grade = int(input())

    if task_grade <= 4:
        failed_tasks += 1

    sum_of_grades += task_grade
    number_of_problems += 1
    last_problem_name = task_name

if failed_tasks < number_of_fails_allowed:
    average_score = sum_of_grades / number_of_problems
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {failed_tasks} poor grades.")
