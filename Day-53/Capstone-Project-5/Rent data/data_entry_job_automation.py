import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

header = {
    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/91.0.4472.77 Safari/537.36 "
}

response = requests.get("https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination"
                        "%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B"
                        "%22west%22%3A-122.5651649375%2C%22east%22%3A-122.29531325292969%2C%22south%22%3A37"
                        ".68601152127223%2C%22north%22%3A37.84521725766066%7D%2C%22regionSelection%22%3A%5B%7B"
                        "%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C"
                        "%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A798064%7D%2C%22mp%22%3A"
                        "%7B%22min%22%3A0%2C%22max%22%3A2600%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B"
                        "%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse"
                        "%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf"
                        "%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B"
                        "%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com/{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-addr")
all_addresses = [address.get_text() for address in all_address_elements]

all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text().split(" ")[0].split("+")[0] for price in all_price_elements]

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/1PhXoWKz1tIhqjycYkM5BA0ZMIH0awNrH3TRtnVHSCr4")

    time.sleep(2)
    address_field = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div["
                                                 "2]/div/div[1]/div/div[1]/input")
    price_field = driver.find_element_by_xpath("//html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div["
                                               "2]/div/div[1]/div/div[1]/input")
    link_field = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div["
                                              "2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div/div/span")

    address_field.send_keys(all_addresses[n])
    price_field.send_keys(all_prices[n])
    link_field.send_keys(all_links[n])
    submit_button.click()
