import os

from shape_all.shape import *


os.system("cls")

# Create a shape from user input
str = " SHAPE CREATOR "
print(str.center(70, "-"))
figure = input("\nEnter the shape type (rectangle, square, triangle): ")

if figure == "rectangle":
    width = float(input("\nEnter the width of the rectangle: "))
    height = float(input("\nEnter the height of the rectangle: "))
    center = point(float(input("\nEnter the x coordinate of the center: ")), float(input("\nEnter the y coordinate of the center: ")))
    shape_obj = rectangle(width, height, center)

elif figure == "square":
    side = float(input("\nEnter the side length of the square: "))
    center = point(float(input("\nEnter the x coordinate of the center: ")), float(input("\nEnter the y coordinate of the center: ")))
    shape_obj = square(side, center)

elif figure == "triangle":
    triangle_type = input("\nEnter the triangle type (isoceles, equilateral, scalene, rectangular): ")

    if triangle_type == "isoceles":
        side1 = float(input("\nEnter the length of side 1: "))
        side2 = float(input("\nEnter the length of side 2: "))
        center = point(float(input("\nEnter the x coordinate of the center: ")), float(input("\nEnter the y coordinate of the center: ")))
        shape_obj = isoceles(side1, side2, center)

    elif triangle_type == "equilateral":
        side = float(input("\nEnter the side length: "))
        center = point(float(input("\nEnter the x coordinate of the center: ")), float(input("\nEnter the y coordinate of the center: ")))
        shape_obj = equilateral(side, center)

    elif triangle_type == "scalene":
        side1 = float(input("\nEnter the length of side 1: "))
        side2 = float(input("\nEnter the length of side 2: "))
        side3 = float(input("\nEnter the length of side 3: "))
        center = point(float(input("\nEnter the x coordinate of the center: ")), float(input("\nEnter the y coordinate of the center: ")))
        shape_obj = scalene(side1, side2, side3, center)

    elif triangle_type == "rectangular":
        opposite = float(input("\nEnter the length of the opposite side: "))
        adjacent = float(input("\nEnter the length of the adjacent side: "))
        hypotenuse = float(input("\nEnter the length of the hypotenuse: "))
        center = point(float(input("\nEnter the x coordinate of the center: ")), float(input("\nEnter the y coordinate of the center: ")))
        shape_obj = TriRectangle(opposite, adjacent, hypotenuse, center)

    else:
        print("\nInvalid triangle type")

else:
    print("\nInvalid shape type")

print("\nShape created:", figure)
print("Area:", round(shape_obj.compute_area(), 2))
print("Perimeter:", round(shape_obj.compute_perimeter(), 2))
print("Inner Angles:", tuple(round(angle, 2) for angle in shape_obj.compute_inner_angle()))
shape_obj.vertices()
shape_obj.edges()
print()