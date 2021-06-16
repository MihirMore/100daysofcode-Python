import requests
from bs4 import BeautifulSoup

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

print(all_links)

