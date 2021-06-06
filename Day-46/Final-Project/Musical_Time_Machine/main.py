import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_UNIQUE_CLIENT_ID",
        client_secret="YOUR_UNIQUE_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}{date}")

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.findAll(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
print(song_names)

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
