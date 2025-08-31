# car.py
# Crystal Chang
#
# Determine the price of a car through guesses 

# Setting price
number = 44500

# Counting the number of guesses
count_guess = 0

# Starting the game
print("Guess the price and win the prize!")
# While loop for guessing
while True:
    guess = input("Enter your guess:")
    guess = int(guess)
    count_guess = count_guess + 1
# Output for guessing 
    if guess == number:
        if count_guess > 5:
            print("It took", count_guess, "guesses.")
            print("Too many guesses!")
            break
        elif count_guess <= 5:
            print("It took", count_guess, "guesses.")
            print("You won the car!")
            break
# Hints for guessing 
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
