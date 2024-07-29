# hybrid.py
# Crystal Chang
#
# Hybrid cars total costs can vary for five years depending on different variables.

# Input cost of car
cost_of_car=input("Cost of car:")
cost_of_car=float(cost_of_car)
# Input miles driven per year
miles_driven_per_yr=input("Miles driven per year:")
miles_driven_per_yr=float(miles_driven_per_yr)
# Input cost of gas
cost_of_gas=input("Cost of gas:")
cost_of_gas=float(cost_of_gas)
# Input fuel efficiency (mpg)
fuel_efficiency=input("Fuel efficiency (mpg):")
fuel_efficiency=float(fuel_efficiency)
# Input estimated resale value after 5 years
estimated_resale_value_after_5_years=input("Estimated resale value after 5 years:")
estimated_resale_value_after_5_years=float(estimated_resale_value_after_5_years)
# Output result for five year gas cost
five_yr_gas_cost=(miles_driven_per_yr/fuel_efficiency)*cost_of_gas*5
print("Five year gas cost:", five_yr_gas_cost)
# Output result five year car cost
five_yr_car_cost=cost_of_car-estimated_resale_value_after_5_years
print("Five year car cost:", five_yr_car_cost)
# Output result five year total cost
total_cost=five_yr_gas_cost+five_yr_car_cost
print("Five year total cost:",total_cost)
