#Geometric formulas

import math

#Square
square_peri = lambda side: 4 * side

print(square_peri(10))

square_area = lambda side: side ** 2

print(square_area(10))


#Rectangle
rect_peri = lambda length,width: 2*length + 2*width

print(rect_peri(100,50))

rect_area = lambda length,width: length * width

print(rect_area(100,50))


#Parallelogram
para_area = lambda base, height: base * height

print(para_area(75, 50))


#Trapezoid
trap_area = lambda base_1, base_2, height: (1/2) * height *(base_1 + base_2)

print(trap_area(50, 100, 80))


#Triangle
tri_area = lambda base, height: (1/2) * base * height

print(tri_area(50, 80))


#Circle
circle_circum = lambda rad: round((math.pi * rad * 2),2)

print(circle_circum(12))

circle_area = lambda rad: round(math.pi * (rad ** 2),2)

print(circle_area(12))


#Cube
cube_area = lambda side: 6 * (side**2)

print(cube_area(20))

cube_vol = lambda side: side ** 3

print(cube_vol(20))


#Right rectangular prism
rec_prism_area = lambda length, width, height: (2 * length * width) + (2 * length * height) + (2 * width * height)

print(rec_prism_area(20, 10, 8))

rec_prism_vol = lambda length, width, height: length * width * height

print(rec_prism_vol(20,10,8))



#Right triangular prism
tri_prism_area = lambda length, width, side, height: (length * width) + (2 * length * side) + (width * height)

print(tri_prism_area(20, 10, 10, 8))

tri_prism_vol = lambda length, width, height: ((1/2) * length * width * height)

print(tri_prism_vol(20, 10, 8))


#Right circular cylinder
cyl_lateral_area = lambda rad, height: round((2 * math.pi * rad * height),2)

print(cyl_lateral_area(5,20))

cyl_area = lambda rad, height: round((2 * math.pi * rad ** 2) + (2 * math.pi * rad * height),2)

print(cyl_area(5,20))

cyl_vol = lambda rad, height: round((math.pi * (rad ** 2) * height),2)

print(cyl_vol(5,20))



#Sphere
sphere_area = lambda rad: 4 * math.pi * (rad ** 2)

print(sphere_area(8))

sphere_vol = lambda rad: round((4/3) * math.pi * (rad **3),2)

print(sphere_vol(8))








