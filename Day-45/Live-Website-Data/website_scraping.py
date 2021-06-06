from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_news_page = response.text

soup = BeautifulSoup(yc_news_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.get_text()
article_link = article_tag.get("href")
print(article_link)
article_upvote = soup.find(name="span", class_="score").get_text()
print(article_upvote)
