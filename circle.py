# circle.py
# Crystal Chang
#
# Calculate the diameter, circumference, and area of a circle using inputted radius.

# Input radius
radius=input("Enter radius:")
radius=float(radius)
# Formula for diameter 
diameter=2*radius
diameter=print("Diameter", diameter)
# Formula for circumference
circumference=2*3.14159*radius
circumference=print("Circumference",circumference)
# Formula for area
area=3.14159*radius**2
area=print("Area",area)
