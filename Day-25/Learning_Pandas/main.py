# Using file function to read file
with open("weather_data.csv", "r") as fhand:
    initial_data = fhand.readlines()

final_data = []
for items in initial_data:
    final_data.append(items.strip()) 

print(final_data)      

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)
    temperatures = []
    for row_data in data:
        if row_data[1] != "temp":
            temperatures.append(int(row_data[1]))
    print(temperatures)    

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)