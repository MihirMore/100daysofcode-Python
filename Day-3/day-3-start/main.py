print("Welcome to the rollercoaster! \n")
height = int(input("What is your height in cm? "))

if (height > 120):
  print("Yaay! You can ride the rollercoaster. \n")
  age = int(input("What's your age? "))
  if (age < 12):
      bill = 5
  elif (12 <= age <= 18):
      bill = 7          
  else:
      bill = 12    
  photo = input("Would you like to have your photo? Y or N :").lower()
  if (photo == 'y'):
      total_bill = bill + 3 
  else:
      total_bill = bill
  print(f"Please pay {total_bill}.")                         
else:
  print("Sorry, you have to grow taller to ride the rollercoaster.")


