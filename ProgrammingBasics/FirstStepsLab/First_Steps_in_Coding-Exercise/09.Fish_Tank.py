length = int(input())
width = int(input())
height = int(input())
percent_full = float(input()) / 100

area_in_liters = (length * width * height) / 1000
liters_capacity = area_in_liters * (1 - percent_full)

print(liters_capacity)
