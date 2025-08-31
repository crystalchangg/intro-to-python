# pi.py
# Crystal Chang
#
# Estimating pi

# Setting up and importing math module
estimate=0
count=0
denominator=1
sign=1
import math
# Input terms
terms=int(input("Number of terms:"))
# While loop for looping until the inputted number of terms
while True:
    count+=1
    estimate+=4/denominator*sign
    denominator +=2
    sign*=-1
    if count==terms:
        break
# Output of estimate and error 
print("Estimate of pi: {:.9f}".format(estimate))
error=(math.pi-estimate)
print("Error: {:.9f}".format(error))
