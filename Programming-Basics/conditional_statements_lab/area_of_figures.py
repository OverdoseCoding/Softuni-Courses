from math import pi

figure = input()

if figure == "square":
    side = float(input())
    square_total = side * side
    print(f"{square_total:.3f}")
elif figure == "rectangle":
    side = float(input())
    side1 = float(input())
    rectangle_total = side * side1
    print(f"{rectangle_total:.3f}")
elif figure == "circle":
    side = float(input())
    circle_total = side * side * pi
    print(f"{circle_total:.3f}")
elif figure == "triangle":
    side = float(input())
    side1 = float(input())
    triangle_total = (side * side1) / 2
    print(f"{triangle_total:.3f}")