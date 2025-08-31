# parrot.py
# Crystal Chang
#
# Repeater that repeats in caps whatever user types

# Loop input so that user can keep inputting phrases and printing out these phrases 
while True:
    # Inputting in phrase  
    s=input(">")
    # Converting inputted phrase to lower case: no matter what lower case or capitalization versions of "quiet" that user types, the word "quiet" will follow the break command
    s=s.lower()
    if s=="quiet":
        # Quits the program when user inputs the word "quiet"
        break
    # Alternatively, if "quiet" is not implemented, the inputted value is printed in caps
    else:
        s=s.upper()
    print(s)
