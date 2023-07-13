# mathematical problems
# 1. a function to find area of a triangle using Heron’s formula
def area_of_triangle():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))

    s=(a+b+c)/2
    return((s*(s-a)*(s-b)*(s-c))**0.5)

area=area_of_triangle()
print(area)

# 2.function to find area of square

def area_of_square():
    a=int(input("a="))

    a=a**2
    return a
area=area_of_square()
print(area)

# 3.function to find area of rectangle

def area_of_rectangle():
    l=int(input("l="))
    w=int(input("w="))

    a=l*w
    return a
area=area_of_rectangle()
print(area)

# 4. Function to find area of a Circle

def area_of_circle():
    r=int(input("r="))

    a=3.14*(r**2)
    return a
area=area_of_circle()
print(area)

# 5. Function to find the area of a trapezium

def area_of_trapezium():

    h=int(input("h="))
    a=int(input("a="))
    b=int(input("b="))

    Area = (a+b)/2*h
    return Area
area=area_of_trapezium()
print(area)