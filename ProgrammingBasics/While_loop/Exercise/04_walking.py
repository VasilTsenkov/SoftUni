steps_goal = 10_000

steps_total = 0

while steps_goal > steps_total:
    user_input = input()

    if user_input != "Going home":
        steps = int(user_input)
        steps_total += steps
    else:
        extra_steps = int(input())
        steps_total += extra_steps
        break

step_difference = abs(steps_total - steps_goal)

if steps_total >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{step_difference} steps over the goal!")
else:
    print(f"{step_difference} more steps to reach goal.")
