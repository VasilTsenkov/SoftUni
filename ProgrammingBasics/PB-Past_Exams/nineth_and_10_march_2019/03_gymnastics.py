country = input()
tool = input()

difficulty = 0
performance = 0

if tool == "ribbon":
    if country == "Russia":
        difficulty = 9.1
        performance = 9.4
    elif country == "Bulgaria":
        difficulty = 9.6
        performance = 9.4
    elif country == "Italy":
        difficulty = 9.2
        performance = 9.5
elif tool == "hoop":
    if country == "Russia":
        difficulty = 9.3
        performance = 9.8
    elif country == "Bulgaria":
        difficulty = 9.55
        performance = 9.75
    elif country == "Italy":
        difficulty = 9.45
        performance = 9.35
elif tool == "rope":
    if country == "Russia":
        difficulty = 9.6
        performance = 9.0
    elif country == "Bulgaria":
        difficulty = 9.5
        performance = 9.4
    elif country == "Italy":
        difficulty = 9.7
        performance = 9.15

score = difficulty + performance
percent = (20 - score) / 20

print(f"The team of {country} get {score:.3f} on {tool}.")
print(f"{percent:.2%}")
