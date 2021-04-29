from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu" , "Squirtle" , "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.header = True
table.border = True
print(table)