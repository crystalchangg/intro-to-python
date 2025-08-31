# phone.py
# Crystal Chang
#
# Checks if the phone number inputted is valid or invalid

# Inputting in phone number based on the given format "### ###-####"
phone=input("Enter number as ### ###-####:")
# Defining "valid" conditions with length of phone number being 12
valid=len(phone)==12
# To keep track of position in inputted phone number, first number of inputted phone number is position=0
pos=0
# Loop running sum of position to ensure inputted phone number is valid based on its length
while valid and pos<12:
    # Checks to make sure user inputs the space between the third and fourth number
    if pos==3:
        valid = phone[pos]==" "
    # Checks to make sure user inputs the hyphen between the sixth and seventh number
    elif pos==7:
        valid=phone[pos]=="-"
    # Checks to make sure user only inputs numbers
    else:
        valid=phone[pos].isdigit()
    # Keeps track of position number of phone number within loop
    pos=pos+1
# When conditions are satisfied print function is "valid"
if valid:
    print("Valid")
# When conditions aren't satisfied print function is "invalid"
else:
    print("Invalid")
