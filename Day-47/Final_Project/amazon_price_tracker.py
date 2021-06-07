import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.in/JBL-Waterproof-Bluetooth-Speaker-PartyBoost/dp/B07SVH63PX/ref=sr_1_2_sspa?crid=2618PXEWSQLPE&dchild=1&keywords=speakers+jbl+loud+speakers&qid=1623057879&sprefix=speakers+j%2Caps%2C323&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUUtaT1hLNEgxMkJJJmVuY3J5cHRlZElkPUEwMTIxNzE0MzdGQ0c1S05GWExOVCZlbmNyeXB0ZWRBZElkPUEwMTQ2ODMxMjlNSEwxOUVNR0xSUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

header = {
    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8",
     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("₹")[1]
actual_price = price_without_currency.replace(",", "")

price_as_float = float(actual_price)
print(price_as_float)

print(f"Current price is ₹ {price_as_float}")
desired_price = float(input("At what price do you want to get notified? "))

if desired_price > price_as_float:
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login("testpythonsmtp123@gmail.com", "Python@123")
        connection.sendmail(from_addr="testpythonsmtp123@gmail.com", to_addrs="moremihir.18@gmail.com", msg=f"Hurry Up!!!! The price for your product has dropped to Rs {price_as_float}.")
print("Email sent.")
