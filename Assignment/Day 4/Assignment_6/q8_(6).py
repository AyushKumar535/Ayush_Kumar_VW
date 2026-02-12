import math

def circle_area(radius):
    return math.pi * radius * radius

def square_area(side):
    return side * side

def rectangle_area(length, breadth):
    return length * breadth

def circle_perimeter(radius):
    return 2 * math.pi * radius

def square_perimeter(side):
    return 4 * side

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

def menu():
    print("Select the shape: ")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        radius = float(input("Enter radius: "))
        print("Area of Circle:", circle_area(radius))
        print("Perimeter of Circle:", circle_perimeter(radius))
    elif choice == 2:
        side = float(input("Enter side length: "))
        print("Area of Square:", square_area(side))
        print("Perimeter of Square:", square_perimeter(side))
    elif choice == 3:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        print("Area of Rectangle:", rectangle_area(length, breadth))
        print("Perimeter of Rectangle:", rectangle_perimeter(length, breadth))
    else:
        print("Invalid choice!")

menu()
