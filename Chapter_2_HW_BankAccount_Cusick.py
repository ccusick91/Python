# Cory Cusick
# ITEC 312-940
# Chapter 2 HW Bank Account

# When a bank account pays compound interest, it pays interest not only on the principal amount
# that was deposited into the account, but also on the interest that has accumulated over time.
# Suppose you want to deposit some money into a savings account, and let the account earn
# compound interest for a certain number of years.

import math

def calculate_compund_interest(P, r, n, t):
    return P * (1 + r / n) ** (n * t)


print ("Welcome to the Account Balance App")

#float makes values into numbers

P = float(input("Please enter the amount of principal: "))

r = float(input("Please enter the interest rate: "))
#int is for integer

n = int(input("Please enter the amount of times interest is compounded annually: "))

t = int(input("Please enter number of years: "))

A = calculate_compund_interest(P, r, n, t)

print(f"Amount after {t} years: ${A:,.2f}")

