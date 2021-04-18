#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ordered_password = ""

for chars in range(1 , nr_letters + 1):
  random_char = random.choice(letters)
  ordered_password += random_char

for symbol in range(1 , nr_symbols + 1):
  random_symbol = random.choice(symbols)
  ordered_password += random_symbol  

for number in range(1, nr_numbers + 1):
  random_number = random.choice(numbers)
  ordered_password += random_number 

print(f"Ordered Password is {ordered_password} \n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = ""

password_list = list(ordered_password)
random.shuffle(password_list)

password = ""

for char in password_list:
  password += char

print(f"Your strong password is {password}")  
