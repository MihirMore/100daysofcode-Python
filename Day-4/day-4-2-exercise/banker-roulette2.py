# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

random_choice = random.randint(0, len(names)-1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy the meal today!")


