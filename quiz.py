# quiz.py
# Crystal Chang
#
# Create a quiz with feedback and score on your answers

# Starting score 
score=0
score=int(score)
# Quiz art question and answer 
print("ART: Who painted 'The Persistance of Memory'?")
print("a. Dali")
print("b. Munch")
print("c. Picasso")
solution = "a"
ans = input("Enter your choice:")
# Invalid input for answers
if ans != "a" and ans != "b" and ans != "c":
    print("Invalid input! Enter a, b, or c next time.")
# Result of inputted answer and score calculator
if ans==solution:
    print("Correct!")
    score=score+1
else:
    print("The correct answer was a")
# Quiz entertainment question and answer
print("ENTERTAINMENT: How many oscars did Hitchcock win?")
print("a. None")
print("b. One")
print("c. Two")
solution = "a"
ans = input("Enter your choice:")
# Invalid input for answers
if ans != "a" and ans != "b" and ans != "c":
    print("Invalid input! Enter a, b, or c next time.")
# Result of inputted answer and score calculator
if ans==solution:
    print("Correct!")
    score=score+1
else:
    print("The correct answer was a")
# Quiz science question and answer
print("SCIENCE: Which dinosaur is most closely related to the pelican?")
print("a. Velociraptor")
print("b. Stegosaurus")
print("c. Pterodactyl")
solution = "a"
ans = input("Enter your choice:")
# Invalid input for answers
if ans != "a" and ans != "b" and ans != "c":
    print("Invalid input! Enter a, b, or c next time.")
# Result of inputted answer and score calculator
if ans==solution:
    print("Correct!")
    score=score+1
else:
    print("The correct answer was a")
# Quiz history question and answer
print("HISTORY: Which of the following was not invented in Baja California?")
print("a. Margaritas")
print("b. Chocolate")
print("c. Caesar Salad")
solution = "b"
ans = input("Enter your choice:")
# Invalid input for answers
if ans != "a" and ans != "b" and ans != "c":
    print("Invalid input! Enter a, b, or c next time.")
# Result of inputted answer and score calculator
if ans == solution:
    print("Correct!")
    score=score+1
else:
    print("The correct answer was b")
# Quiz science and nature question and answer
print("SCIENCE AND NATURE: Can pigs swim?")
print("a. Yes")
print("b. No")
print("c. Only in salt water")
solution = "a"
ans = input("Enter your choice:")
# Invalid input for answers
if ans != "a" and ans != "b" and ans != "c":
    print("Invalid input! Enter a, b, or c next time.")
# Result of inputted answer and score calculator
if ans==solution:
    print("Correct!")
    score=score+1
else:
    print("The correct answer was a")
# Quiz sport and leisure question and answer
print("SPORT AND LEISURE: What color is the middle Olympic ring?")
print("a. Red")
print("b. Blue")
print("c. Black")
solution = "c"
ans = input("Enter your choice:")
# Invalid input for answers
if ans != "a" and ans != "b" and ans != "c":
    print("Invalid input! Enter a, b, or c next time.")
# Result of inputted answer and score calculator
if ans==solution:
    print("Correct!")
    score=score+1
else:
    print("The correct answer was c")
# Quiz genius question and answer
print("GENIUS: In ancient Rome, what is L divided by X?")
ans = input("Enter your answer:")
# Result of inputted answer and score calculator
if ans == 'V' or ans == '5':
    done = True
    print("Correct!")
    score=score+1
else:
    done=False
    print("Correct answers were 5 or V")
# Results of quiz
print("Your final score is "+ str(score))
if 0<=score<=2:
    print("You were unlucky!")
elif(3<=score<=4):
    print("At least you did better than chance!")
elif(5<=score<=6):
    print("Excellent!")
else:
    print("Genius!")
