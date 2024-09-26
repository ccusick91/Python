# Cory Cusick
# ITEC 312-940
# Budget Analysis

# Write a program that asks the user to enter the amount that he or she has budgeted for
# a month. A loop should then prompt the user to enter each of his or her expenses for
# the month and keep a running total. When the loop finishes, the program should display
# the amount that the user is over or under budget.

budget = float(input("Enter your budget for the month: $"))
total_expenses = 0
num_expenses = int(input("How many expenses do you have this month? "))

for expense_num in range(1, num_expenses + 1):
    expense = float(input(f"Enter expense {expense_num}: $"))
    total_expenses += expense
difference = budget - total_expenses

if difference > 0:
    print(f"You are under budget by: ${difference:.2f}")
elif difference < 0:
    print(f"You are over budget by: ${-difference:.2f}")
else:
    print(f"You have met your budget.")