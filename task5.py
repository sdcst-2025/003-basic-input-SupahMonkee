#! python3
import math
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.


print("Finding Radius of a Sphere given Volume")

v = float(input("Enter your volume: "))

r = math.pow(3*v/(4*math.pi),1.0/3)

print(f"Radius = {r}")

#done