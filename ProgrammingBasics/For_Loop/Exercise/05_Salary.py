open_tabs_number = int(input())
salary = int(input())

for _ in range(open_tabs_number):
    site_name = input()
    if site_name == "Facebook":
        salary -= 150
    elif site_name == "Instagram":
        salary -= 100
    elif site_name == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(int(salary))
