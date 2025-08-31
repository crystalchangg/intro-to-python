# pocket.py
# Crystal Chang
#
# Calculate pocket change

# Pocket change statement
print("Compute your pocket change!")
# Calculation of change in terms of quarters
quarters=input("Quarters?")
quarters=float(quarters)
quarter_amount=quarters*0.25
# Calculation of change in terms of dimes
dimes=input("Dimes?")
dimes=float(dimes)
dime_amount=dimes*0.10
# Calculation of change in terms of nickels
nickels=input("Nickels?")
nickels=float(nickels)
nickel_amount=nickels*0.05
# Calculation of change in terms of pennies
pennies=input("Pennies?")
pennies=float(pennies)
penny_amount=pennies*0.01
# Calculation of total pocket change
total=float(quarter_amount+dime_amount+nickel_amount+penny_amount)
print("The total is ${:.2f}".format(total))
