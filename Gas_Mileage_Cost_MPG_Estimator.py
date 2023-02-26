# Cory Cusick
# CIS-135 Python
# Homework Programming Assignment #2 (Part 2)

''' Updated application from HW assignment Part 1. This update makes changes as follows:

1) Data Types declared for required variables
 Floats: cost_per_gallon_gas, MPG, price_to_fill_tank, total_distance_per_tank
 Integer: total_tank_capacity
2) Communicate Section needs re-wording and reformatting: Suggestions include:
print("Hello, and Welcome to the Gas Mileage App")
# Display: "This app calculates MPG and cost to fill fuel tank with gas”
print("This app calculates MPG and cost to fill tank")
3) In the Acquire Data Section:
    A) Re-formatting and streamlined input statements are suggested
    B) In Python is taken in as a string.
   All numeric data is re-cast to the float or int data types
4) Logic Error found in the Compute Data Section
   Original Specification Said:
     from # distance_per_tank = tank_total_gallons / distance_per_gallon
   This should have been a multiplication not a division
     to # distance_per_tank = tank_total_gallons * distance_per_gallon
5) Final section needs re-wording and reformatting: Suggestions include:
     print("Price to fill tank $", price_to_fill_tank)
     print("The distance you can travel on a full tank is, ", distance_per_tank, "miles")
     print("Thank you for using the Gas Mileage App.")
'''



# Variables
# Variable Cost per Gallon:  cost_per_gallon_gas
cost_per_gallon_gas = 0.00
# Variable Total Gallons for Tank:  total_tank_capacity
total_tank_capacity = 0
# Variable Cost per Distance per Gallon:  MPG
MPG = 0.00
# Variable Cost to Fill Tank:  price_to_fill_tank
price_to_fill_tank = 0.00
# Distance per Tank:  total_distance_per_tank
total_distance_per_tank = 0.00

# Display
# Display: "Hello, and Welcome to the Gas Mileage App!"
print("\n\tHello, and Welcome to the Gas Mileage App!")
# Display: "This app calculates MPG and cost to fill tank”
print("\tThis app calculates MPG and cost to fill tank")

# Input
# Display: “Cost of gallon of gas”
# print("Cost of gallon of gas")
cost_per_gallon_gas = float(input("\n\t\tPlease enter the cost of a gallon of gas: "))
# Display: “Gas tank capacity”
# print("Gas tank capacity")
total_tank_capacity = int(input("\t\tHow many gallons of gas does your fuel tank hold?: "))
# Display: “Get vehicle MPG”
# print("What is vehicle MPG")
MPG = float(input("\t\tPlease enter your vehicles Miles Per Gallon (MPG) : "))

# Calculate
# Total_distance_per_tank = total_tank_capacity / miles per gallon (MPG)
# old-incorrect version total_distance_per_tank = total_tank_capacity / MPG
total_distance_per_tank = total_tank_capacity * MPG
# price_to_fill_tank = cost_per_gallon_gas * total_tank_capacity
price_to_fill_tank = cost_per_gallon_gas * total_tank_capacity


# Results

# Display: “Price to fill tank”
print("\n\tThe price of filling your fuel tank is: $ {:.2f}".format(price_to_fill_tank))
# Display: “The distance you can travel on a full tank is, ”
print("\tThe estimated distance you can travel on a full tank is, {}-miles.".format(int(total_distance_per_tank), "-miles"))
# Display: “Thank you for using the Gas Mileage App.”
print("\n\tThank you for using the Gas Mileage App.")
