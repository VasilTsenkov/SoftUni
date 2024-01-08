x = float(input())
y = float(input())
h = float(input())

front_wall_area = (x * x) - (1.2 * 2)
back_wall_area = (x * x)
side_walls = ((y * x) - (1.5 * 1.5)) * 2
paint_for_walls = front_wall_area + back_wall_area + side_walls

roof_rectangles = (x * y) * 2
roof_triangles = ((x * h) / 2) * 2
paint_for_roof = roof_rectangles + roof_triangles

green_paint = paint_for_walls / 3.4
red_paint = paint_for_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
