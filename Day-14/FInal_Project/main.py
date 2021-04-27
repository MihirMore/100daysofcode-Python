# Importing all the required libraries and classes.

from art import logo
from art import vs
from game_data import data
import os
import random

# Using random function to generate a random selection from game_data data dictionary
# This is done for 2 selections 

first_select = random.choice(data)
# a flag for while loop is set to loop over a logic

should_continue = True
# Score variable to maintain score 

score = 0
while should_continue:
  second_select = random.choice(data)  
  # If both the entries are same we select again.
  if (first_select == second_select):
      second_select = random.choice(data)

  # Creating a new dictionary with a and b as keys and follower_count as value to compare data.    
  follower_value = {
  'a' : first_select["follower_count"],
  'b' : second_select["follower_count"]
  }
  print(logo)
  # This will be printed after score = 1.

  if score > 0:
    print(f"You're right! Current Score: {score}")    
  # Printing data for higher lower game for user to view and take a decision.

  print(f"Compare A: {first_select['name']}, a {first_select['description']}, from {first_select['country']}")
  print(vs , end="\n")
  print(f"Against B: {second_select['name']}, a {second_select['description']}, from {second_select['country']}")
  # Accepting  user input and converting it to lower to avoid and traceback error.

  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  # user_value is the value of choice user selected.

  user_value = follower_value[user_guess]

  # Comparing the value entered by user is higher or lower. If value is higher then user scores 1 point or else 
  # user loses the game and final score is showed.
  # Also the second entry is swaped with first entry after completing the comparison since we need it for further 
  # gameplay if user wins.

  if user_guess == 'a':
    if user_value > follower_value["b"]:
      score += 1
      print(f"You're right! Current Score: {score}")
      first_select = second_select
      _ = os.system('cls')
    else:      
      should_continue = False
  elif user_guess == 'b':
    if user_value > follower_value["a"]:
      score += 1
      print(f"You're right! Current Score: {score}")
      first_select = second_select
      _ = os.system('cls')
    else:      
      should_continue = False

# Screen is cleared and final score is showed.

_ = os.system('cls')
print(f"Sorry, That's wrong. Final Score: {score}")
