# roth.py
# Crystal Chang
# 
# Figuring out how long it takes to double investment

# Setting up years
running_year=0
# Input deposit
deposit_amount=input("Enter an initial Roth IRA deposit amount:")
deposit_amount=float(deposit_amount)
# Defining investment amount
investment_amount=deposit_amount
# Input percent
percent=input("Enter an annual percent rate of return:")
percent=float(percent)
# While loop to loop investment amount until doubled the investment
while True:
# When the investment is doubled
    if investment_amount>deposit_amount*2:
        break
# When the investment has not doubled
    investment_amount=investment_amount*(1+(percent/100))
    running_year=running_year+1
    print("Value after year {}: ${:.2f}".format(running_year, round(investment_amount, 4)))
# Total year output
print("It will take", running_year,"years to double your investment with a {:.0f}%".format(percent),"APR.")
