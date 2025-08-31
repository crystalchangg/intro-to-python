# check.py
# Crystal Chang 
#
# Checking whether or not a credit card number is valid

# Inputting 8 digit credit card number
s=input("Enter your 8-digit card number:")
# Taking out the space in case user puts space like what is shown on credit cards
s=s.replace(" ","")
# Keeping track of total sum
sum2=0
# Length of card has to be 8 or else invalid statement is printed
if len(s)!=8:
    print("Invalid")
else:
    # If length of card is satisfied, add every other digit starting from right side
    sum1=int(s[-1])+int(s[-3])+int(s[-5])+int(s[-7])
    # If length of card is satisfied, add two times the other digits that were not in the past step
    temp_string=str(int(s[-2])*2)+str(int(s[-4])*2)+str(int(s[-6]*2))+str(int(s[-8])*2)
# Loop running sum to get the total sum
for num in temp_string:
    sum2+=int(num)
    sum=sum1+sum2
# If last digit of sum is 0 then print "valid"
if str(sum)[-1]==str(0):
    print("Valid")
# If last digit of sum is not 0 then print "invalid"
else:
    print("Invalid")
