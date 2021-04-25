################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  portion_strength = 2
  print(portion_strength)

drink_potion()  

# print(portion_strength) This will throw an error 'portion_strength not defined' since it's outside the scope of function.

