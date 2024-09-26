# Cory Cusick
# ITEC 312-940
# Rectangle area

# The area of a rectangle is the rectangle’s length times its width. Write a program that
# asks for the length and width of two rectangles. The program should tell the user which
# rectangle has the greater area or if the areas are the same.

# Area = Length * Width

# Get dimensions of rectangle 1
Length1 = int(input("Please enter the length of the rectangle 1: "))

Width1 = int(input("Please enter the width of the rectangle 1: "))

# Get the dimensions of rectangle 2
length2 = int(input("Please enter the length of rectangle 2: "))

width2 = int(input("Please enter the width of rectangle 2: "))

# Get areas of the rectangles
area1 = Length1 * Width1
area2 = length2 * width2

# Which has the greater area?

if area1 > area2:
    print("Rectangle 1 has the greatest area.")
elif area2 > area1:
    print("Rectangle 2 has the greatest area.")
else:
    print("Both have the same area.")