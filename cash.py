# cash.py
# Crystal Chang
#
# A cash register that totals how much items and prices are spent 
# Name of the program
print("Automated cash register")
# Inputting file name to open
file_name=input("Enter file of prices:")
infile=open(file_name)
# Keeping track of items and total cost
items=0
total=0
# Loop that reads and prints line by line of opened file when file is opened and accounts for running sum of items and prices
for line in infile:
    lines=line.strip()
    items=items+1
    total=total+float(line)
# When all lines have been read, total cost and number of items are printed
print("File contained",items,"items totaling ${:.2f}".format(total))


# cash2.py
# Crystal Chang 
# A cash register that totals how much items and prices are spent regardless of whether or not there are words within the txt file 
# Name of the program
print("Automated cash register")
# Inputting file name to open
file_name=input("Enter file of prices:")
infile=open(file_name)
# Keeping track of items and total cost
items=0
total=0
# Loop that reads and prints line by line of opened file when file is opened and accounts for running sum of items and prices
for line in infile:
    lines=line.strip()
    # If "$" is in first position, the prices can be added together as decimals  
    if lines[0]=='$':
        lines=lines.strip('$')
        items+=1
        # Converts total cost as float
        total=total+float(lines)
# When all lines have been read, total cost and number of items are printed
print("File contained",items,"items totaling ${:.2f}".format(total))
