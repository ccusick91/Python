# Cory Cusick
# ITEC 312-940
# Bug Collector

# A bug collector collects bugs every day for five days. Write a program that keeps a
# running total of the number of bugs collected during the five days. The loop should ask
# for the number of bugs collected for each day, and when the loop is finished, the
# program should display the total number of bugs collected.

total_bugs = 0

for day in range(1, 6):
    bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
    
    total_bugs += bugs
    
    print(f"Running total after day {day}: {total_bugs}")

print(f"The total number of bugs collected over 5 days: {total_bugs}")