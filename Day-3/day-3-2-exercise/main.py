# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2 , 1)
if (bmi < 18.5):
  print(f"Your BMI is {bmi}, you are underweight")
elif (18.5 <= bmi < 25):
  print(f"Your bmi is {bmi}, you have normal weight")
elif (25 <= bmi < 30):
  print(f"Your bmi is {bmi}, you are overweight") 
elif (30 <= bmi <35):
  print(f"Your bmi is {bmi}, you are obese")
else:
  print(f"Your bmi is {bmi}, you are clinically obese")     



