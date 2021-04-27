from colorama import Fore, Back, Style
import os
import random
from data import first,last
from art import logo


user_exit = True

while user_exit:
    print(logo)
    first_name = random.choice(first)
    last_name = random.choice(last)
    print(Fore.GREEN + "{} {}".format(first_name,last_name))
    user_choice = input("Do you want to continue? Type 'y' to continue or 'n' to exit. " ).lower()
    _ = os.system('cls')
    if user_choice == 'n':
        user_exit = False


