# Cory Cusick
# ITEC 312-940
# Chapter 2 HW Radius and Circumference

# Write a program that asks the user to enter the radius of a circle
# the program should calculate and display the area and the circumference
# of the circle using Pi R squared for the area and 2 pi R for the circumference

from cmath import pi
import math

radius = float(input ("Greetings, please enter the radius of a circle: "))
circumference = 2 * pi * radius

area = pi * radius ** 2

print("The area of the circle is " + str(area))
print("The circumference of the circle is " + str(circumference))

