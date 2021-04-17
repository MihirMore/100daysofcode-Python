# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

who_will_buy = random.choice(names)

print(f"{who_will_buy} is going to buy the meal today!")



