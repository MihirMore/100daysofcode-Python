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

for tag in anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)
