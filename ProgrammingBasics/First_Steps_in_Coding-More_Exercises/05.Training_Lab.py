height = float(input()) * 100
width = float(input()) * 100

width_available = width - 100
desks_per_width = width_available // 70
desks_per_height = height // 120
desks_possible = (desks_per_width * desks_per_height) - 3

print(int(desks_possible))
