from bs4 import BeautifulSoup
import requests

top100_movie_endpoint = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(top100_movie_endpoint)
top100_movie_html = response.text

# get top 100 movies to watch
soup = BeautifulSoup(top100_movie_html, "html.parser")
top100_movies = [movie.get_text() for movie in soup.find_all(name="h3", class_="title")]
top100_movies.reverse()

# writing the list of movies into a .txt file
with open("Top100_Movies.txt", "w", encoding="utf-8") as file:
    for movie in top100_movies:
        file.write(f"{movie}\n")

