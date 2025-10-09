# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output:
# r = 1.1
# Area = 3.8013271108436504
#######################################################################################################################

import math

r = float(input("Enter the radius of circle to calculate its area: "))

area = round((math.pi * (r**2)),2)
print(f"\n\nThe area of circle with radiun {r} is : {area}")