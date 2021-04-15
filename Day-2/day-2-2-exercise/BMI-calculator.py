# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) // float(height) ** 2

if (bmi <= 18.5):
    print(f"BMI is {bmi} - Underweight")
elif (18.5 < bmi <= 25):
    print(f"BMI is {bmi} - Normal")
elif (25 < bmi <= 30):
    print(f"BMI is {bmi} - Overweight")
else: 
    print(f"BMI is {bmi} - Obese")            












