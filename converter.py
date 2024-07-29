# converter.py
# Crystal Chang
#
# Convert a character to the binary representations of the letter.

# Input character
character=input("Enter a character:")
num=ord(character)
binary=bin(num)
# Output result
print(character, "corresponds to the integer", num, "which is", binary, "in binary.")
