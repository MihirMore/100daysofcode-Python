# Include an ASCII art logo.
from art import logo
import random
import sys
print(logo)
print("Welcome to the Guessing Game!")
print("I'm guessing a number between 1 and 100.")

value = random.randint(1,100)
print(value)

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
   


