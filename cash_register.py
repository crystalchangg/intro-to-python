# cash_register.py
# Crystal Chang
#
# Totaling up total cost of items

# Setting up item number and cost
items=0
running_sum=0
print("Cash register (press enter to exit)")
# While loop to loop item cost and sum of the costs
while True:
    item_cost=input("Enter item cost:")
# When there are no more items 
    if item_cost == "":
        break
        print("You entered",items)
# When there are items still being checked out
    elif item_cost!=0:
        item_cost=float(item_cost)
        running_sum+=item_cost
        items=items+1
# Total items and cost output
print("You entered", items, "items totaling ${:.2f}".format(running_sum))
