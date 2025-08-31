# change.py
# Crystal Chang
#
# Convert amount of cents to number of coins

# Input amount of cents
cents=input("Enter cents:")
cents=int(cents)
print("The minimum coins for",cents,"cents are:")
# Number of quarters 
quarters=cents//25
print(quarters,"Quarters")
# Number of dimes 
quarters_value=quarters*25
remaining_cents_after_quarters=cents-quarters_value
dimes=remaining_cents_after_quarters//10
print(dimes,"Dimes")
# Number of nickels
dimes_value=dimes*10
remaining_cents_after_dimes=remaining_cents_after_quarters-dimes_value
nickels=remaining_cents_after_dimes//5
print(nickels,"Nickels")
# Number of pennies
nickels_value=nickels*5
remaining_cents_after_nickels=remaining_cents_after_dimes-nickels_value
pennies=remaining_cents_after_nickels//1
print(pennies,"Pennies")
