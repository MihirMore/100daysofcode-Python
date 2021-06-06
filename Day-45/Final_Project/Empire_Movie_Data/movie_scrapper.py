import requests
from bs4 import BeautifulSoup

URL = "https://www.esquire.com/entertainment/movies/g226/best-movies-ever-0609/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.findAll(name="span", class_="listicle-slide-hed-text")

movies_list = []
for movie in range(len(all_movies)):
    movies_list.append(all_movies[movie].text)


count = 1
with open("movies.txt", mode="w") as file:
    for movie in movies_list:
        file.write(f"{count}: {movie}\n")
        count += 1
