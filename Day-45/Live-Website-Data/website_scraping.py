from bs4 import BeautifulSoup
import requests
import smtplib

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

article_title = article_texts[index_of_highest]
article_link = article_links[index_of_highest]
print(article_title)

with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
    connection.login("YOUR_EMAIL_ID", "PASSWORD")
    connection.sendmail(from_addr="YOUR_EMAIL_ID", to_addrs="YOUR_EMAIL_ID", msg=f"Subject: Today's News\n\n"
                                                                                                        f"Highest "
                                                                                                        f"upvoted news "
                                                                                                        f"on Hackernews:"
                                                                                                        f" \n{article_title} "
                                                                                                        f"\n{article_link}")
    print("email send")
