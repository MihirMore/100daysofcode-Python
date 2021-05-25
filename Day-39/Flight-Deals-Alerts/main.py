from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flightsearch = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flightsearch.get_destination_code(city_name=row["city"])
    print(f"sheet data: \n{sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()
