
# mileage.py
# Crystal Chang
#
# Calculating the average mileage

# Setting up  
sum_mileage=0
sum_gallons=0
print("Your Personal Fuel Economy")
# While loop to loop number of miles and gallons input and sums
while True:
    miles=input("Number of miles traveled (or enter to exit):")
# When user enters to exit
    if miles=="":
        break
# When user inputs number of miles
    miles=float(miles)
    gallons=input("Number of gallons needed:")
    gallons=float(gallons)
    mileage=miles/gallons
    print("Mileage this tank = {:.1f}".format(mileage))
    sum_mileage+=miles
    sum_gallons+=gallons
# Calculating average mileage
average_mileage=sum_mileage/sum_gallons
# Output of average mileage
mileage=print("Average mileage = {:.1f}".format(average_mileage))
