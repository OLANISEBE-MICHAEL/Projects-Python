markdown
# Billboard 100 Playlist Creator

A Python program that scrapes the Billboard Top 100 songs for a given date and creates a private Spotify playlist with those songs using the Spotify Web API.

## Features

- Scrapes historical Billboard Hot 100 chart using BeautifulSoup
- Authenticates with Spotify and creates a private playlist
- Searches for songs on Spotify and adds them to the playlist

## Technologies

- Python
- BeautifulSoup
- Requests
- Spotipy (Spotify API client)

## Setup Instructions

1. Create a Spotify Developer App to get your `CLIENT_ID` and `CLIENT_SECRET`.
2. Set environment variables or load from `token.txt`.
3. Run the script:

bash
python billboard_playlist.py
