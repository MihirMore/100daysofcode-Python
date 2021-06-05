from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.prettify())
print(soup.a)
anchor_tags = soup.find_all(name="a")
print(anchor_tags)
paragraph_tags = soup.find_all(name="p")
print(paragraph_tags)