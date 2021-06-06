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


article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

highest_number = max(article_upvotes)
print(highest_number)
index_of_highest = article_upvotes.index(highest_number)


print(article_texts[index_of_highest])
print(article_links[index_of_highest])
print(article_upvotes)

