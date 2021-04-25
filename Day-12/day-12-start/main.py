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

# Global Scope

player_health = 10

def power_up(health):
    portion_strength = 4
    health += portion_strength
    print(health)
    print(player_health)

power_up(player_health)    

# There is no block scope in Python
player_level = 3
enemies = ['skeletons','zombies','demons']

if player_level < 5:
    new_enemy = enemies[0]
    
print(new_enemy)


