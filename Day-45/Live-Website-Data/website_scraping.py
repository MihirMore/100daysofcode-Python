from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_news_page = response.text

soup = BeautifulSoup(yc_news_page, "html.parser")
articles = soup.findAll(name="a", class_="storylink")
article_texts = []
article_links = []


for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvotes = [score.getText() for score in soup.findAll(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)
