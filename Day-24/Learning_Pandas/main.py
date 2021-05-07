Using file function to read file
with open("weather_data.csv", "r") as fhand:
    initial_data = fhand.readlines()

final_data = []
for items in initial_data:
    final_data.append(items.strip()) 

print(final_data)      

