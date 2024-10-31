#! python3
import math
# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("ax + b = c")

a = int(input("Enter variable A: "))
b = int(input("Enter variable B: "))
c = int(input("Enter variable C: "))

x = (c-b)/a

print(f"x = {x}")

#done