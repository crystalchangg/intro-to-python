# password.py
# Crystal Chang
# 
# Checking an inputted password's length and its digits, special characters, upper case letters, as well as lower case letters to determine if a password is strong

# Inputting in password
password=input("Enter password:")
# To keep track of how many upper case letters, lower case letters, numbers, and special characters there are
num_upper=0
num_lower=0
digit=0
special=0
# To specify which special characters to look for
character=['!','@','#','$','%','&']
# Loop running sum so that every time there is one of these password elements within the inputted password, it is added to the tracker
for letter in password:
    if letter.isupper():
        num_upper+=1
    if letter.islower():
        num_lower+=1
    if letter.isdigit():
        digit+=1
    if letter in character:
        special+=1
# Conditions that need to be met before printing (checks for whether the password is of length and has a lower case, upper case, special character, and number)
if len(password)>=8:
    print("Has length")
if num_lower>=1:
    print("Has lower case")
if num_upper>=1:
    print("Has upper case")
if digit>=1:
    print("Has digit")
if special>=1:
    print("Has special")
