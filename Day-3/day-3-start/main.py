print("Welcome to the rollercoaster! \n")
height = int(input("What is your height in cm? "))

if (height > 120):
  print("Yaay! You can ride the rollercoaster.")
  age = int(input("What's your age? "))
  if (age < 12):
      print("Please pay $5")
  elif (12 <= age <= 18):
      print("Please pay $7")          
  else:
      print("Please pay $12")      
else:
  print("Sorry, you have to grow taller to ride the rollercoaster.")
