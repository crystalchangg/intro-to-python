# approx.py
# Crystal Chang
#
# Determine if numbers are identical 

# Weight on moon calculations
print("Weight on moon:", 100/6)
print("Weight on moon:", 100*(1/6))
# Identical numbers determinator
number_1=input("Enter a number:")
number_2=input("Enter a number:")
if number_1==number_2:print("Those numbers are identical")
# Identical numbers determinator to a certain number of decimal places
count_1=0
number_1=float(input("Enter a number:"))
while(number_1>0):
    count_1=count_1+1
    number_1=number_1//10
count_2=0
number_2=float(input("Enter a number:"))
while(number_2>0):
    count_2=count_2+1
    number_2=number_2//10
if count_1==count_2:print("Those numbers are the same to",count_1,"decimal places")
