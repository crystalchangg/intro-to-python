# tip.py
# Crystal Chang
#
# Calculating and looping tipping options

# Input total 
total=input("Enter total:")
total=float(total)
# Loop for tip options
n=15
tip=0
while n > 0:
    tip=(n/100)*total
# Print tip output 
    print("A {:.0f}%".format(n), "tip is ${:.2f}".format(tip))
# Ending loop when reaching 25%
    if n == 25:
        break
# Increasing tipping options each by 1%
    n=n+1
