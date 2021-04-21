# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello!")
  print("How are you?")
  print("Isn't the weather nice today?")

greet()  


def greet_with_name(name):
  print(f"Hello {name}!")
  print(f"How are you {name}?")
  print("Isn't the weather nice today?")

greet_with_name("Mihir")

def greet_with(name, location):
  print(f"Hello! {name}")
  print(f"What's it like in {location}?")


greet_with("Mihir","Mumbai")
print()
greet_with(name = "Tom", location = "California")