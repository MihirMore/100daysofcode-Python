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
