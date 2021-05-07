import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict["temp"])

data_list = data["temp"].to_list()
print(data_list)
print(sum(data_list) / len(data_list))

print(data["temp"].max())

# Get data in Columns
print(data["condition"])
print(data.condition)

print(data[data.day == "Thursday"])

maximum = data.temp.max()
print(data[data.temp == maximum])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_day = data[data.day == "Monday"]
monday_temp = monday_day.temp
monday_f = (9 / 5 * monday_temp) + 32
print(monday_f)


# Create a dataframe from scratch

data_dictionary = {
    "students": ["Amy", "James", "Jon"],
    "scores": [76, 56, 65]
}

data1 = pandas.DataFrame(data_dictionary)
data1.to_csv("new_data.csv")
