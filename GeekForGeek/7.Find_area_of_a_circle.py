import math

def area_of_circle(radius):
     area = math.pi * math.pow(radius, 2)
     return area

r = int(input("Enter the radius of circle to calculate its area : "))

print(f"The area of circle is : {area_of_circle(r):.2f}")