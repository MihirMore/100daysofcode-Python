import requests
from twilio.rest import Client

STOCK_NAME = "GOOGL"
COMPANY_NAME = "Alphabet Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "Your Alphavantage API KEY"
NEWS_API_KEY = "Your newsapi API KEY"
TWILIO_ACCOUNT_SID = "Your Twilio S_ID"
TWILIO_AUTH_TOKEN = "Twilio AUTH TOKEN"

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact",
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "sortBy": "popularity"
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = data_list[0]["4. close"]

# Get day before yesterday's data
day_before_yesterday_data = data_list[1]["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
positive_difference = float(day_before_yesterday_data) - float(yesterday_closing_price)
up_down = None
if positive_difference < 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.
percentage_difference = round((positive_difference / float(yesterday_closing_price)) * 100)
print(percentage_difference)

# If percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percentage_difference) > 10:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    top_three_articles = articles[:3]

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME} {up_down}{percentage_difference}% \nHeadline: {article['title']}. \nBrief: {article['description']} "
        for article in
        top_three_articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_="+16503977270",
            to="my_number"
        )

        print(message.status)
