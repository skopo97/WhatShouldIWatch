import requests
from config import Config

BASE_URL = "https://api.themoviedb.org/3"

def fetch_popular_movies(page=1):
    url = f"{BASE_URL}/discover/movie"
    params = {
        'api_key': Config.TMDB_API,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'page': page
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return []