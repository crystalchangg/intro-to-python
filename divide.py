# divide.py
# Crystal Chang
#
# Divide numbers.

# Input a number
number_1=input("Enter a number:")
number_1=int(number_1)
# Input a second number to divide the first number by
number_2=input("Enter a number to divide that by:")
number_2=int(number_2)
# Division and remainder
number_3=number_1//number_2
number_4=number_1%number_2
# Output result
print(number_1,"divided by", number_2, "is", number_3, "with", number_4, "remaining")
