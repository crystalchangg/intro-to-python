# digits.py
# Crystal Chang 
#
# Gives a phone number digits string based on inputted phone number

# Inputting in phone number
phone=input("Enter phone number:")
# In case user puts hyphen in phone number input, the hyphen is taken out for consistency
phone=phone.replace('-','')
# In case user puts parentheses in phone number input, the parentheses are taken out for consistency
phone=phone.replace('(','')
phone=phone.replace(')','')
# In case user puts spaces in phone number input, the spaces are taken out for consistency
phone=phone.replace(' ','')
# After accounting for all these possible scenarios, print out digit string
print("Digit string: "+phone)
