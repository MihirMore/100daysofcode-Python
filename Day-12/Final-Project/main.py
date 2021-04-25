# Include an ASCII art logo.

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
import sys
print(logo)
print("Welcome to the Guessing Game!")
print("I'm guessing a number between 1 and 100.")

value = random.randint(1,100)


user_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
user_attempts = 0
if user_level == 'easy':
  user_attempts = 10  
elif user_level == 'hard':
  user_attempts = 5 
else:
    print("You have entered an invalid input. Bye!")
    sys.exit()
while user_attempts > 0:  
  print(f"You have {user_attempts} attempts remaining to guess the number.")
  user_guessed = int(input("Make a guess: "))
  if user_guessed == value:
    print(f"You got it! The answer was {value}.")
    user_attempts = -1    
  elif user_guessed > value:
    print("Too high.\nGuess again.")
    user_attempts -= 1
  elif user_guessed < value:
    print("Too low.\nGuess again.")
    user_attempts -= 1

if user_attempts == 0:
  print("You've run out of guesses, you lose.")
  print(f"The secret number is {value}.")


