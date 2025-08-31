# translate.py
# Crystal Chang 
#
# Translating from English into Pig Latin

# Inputting English word
word=input("Enter a word:")
# Converts inputted English word into lower case letters for consistency
word=word.lower()
# Defines what a vowel is 
vowel=['a','e','i','o','u']
# Changes in inputted English word if first letter/position of the inputted English word is vowel 
if word[0] in vowel:
    latin=word+"way"
    print(word,"in Pig latin is",latin)
# Changes in inputted English word if first letter/position of the inputted English word is a consonant
else:
    latin=word[1:]+word[0]+"ay"
    print(word,"in Pig latin is",latin)
