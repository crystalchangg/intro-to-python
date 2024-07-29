# bmi.py
# Crystal Chang
#
# Using the inputted height and weight values, calculate the BMI using the BMI formula.

# Input the height 
height=input("Enter height in inches:")
height=float(height)
# Input the weight
weight=input("Enter weight in pounds:")
weight=float(weight)
# Output result
BMI=((weight)/((height)**2))*703
print("BMI:",BMI)
