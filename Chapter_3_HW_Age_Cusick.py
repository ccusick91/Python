# Cory Cusick
# ITEC 312-940
# Day of The Week

# Write a program that asks the user to enter a person’s age. The program should display
# a message indicating whether the person is an infant, a child, a teenager, or an adult.


age = int(input("Please enter your age: "))

if age <= 1:
    print("User age is infant")

elif age >= 1 and age <= 12: 
    print("User is a child")

elif age >= 13 and age <= 19:
    print("User is a teenager")
elif age >= 20:
    print("User is an adult")

