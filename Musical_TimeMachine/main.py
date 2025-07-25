from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# spotify authentication keys
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
TOKEN = ""
with open("token.txt") as data:
    TOKEN = json.load(data)


# obtaining and scraping billboard 100 data
date = input("Which year do you want to travel to? Enter the data in this format (YYYY-MM-DD) ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 "
                  "Safari/537.36 Edg/138.0.0.0",
}

response = requests.get(URL, headers=header)
response.raise_for_status()

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
top_songs = soup.select("li ul li")
songs_and_artists = []

for song in top_songs:
    song_name = song.select_one("h3")
    song_artist = song.select_one("span")
    if song_name and song_artist:
        title = song_name.get_text(strip=True)
        artist = song_artist.get_text(strip=True)
        songs_and_artists.append((title, artist))


songs_to_search = [f"track: {item[0]} artist: {item[1]} year: {date.split('-')[0]}" for item in songs_and_artists]
song_uris = []

# getting authentication token form spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:9090",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
    username="Michael"
))


# creating and adding songs to the playlist
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Top 100", public=False)
playlist_id = playlist["id"]

for song in songs_to_search:
    result = sp.search(q=song, type="track", limit=1)
    track = result["tracks"]["items"]
    if track:
        uri = track[0]["uri"]
        song_uris.append(uri)
        print(f"Found {song}, URI -> {uri}")
    else:
        print(f"{song} Not found")

# add tracks
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)



