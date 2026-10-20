import requests
from requests import Response
from models.track import Track
import urllib.parse

BASE_URL: str = "https://lrclib.net"
HEADERS = {'user-agent': 'pld v0.0.1 (innmax001@gmail.com)'}

def get_lyrics(track: Track):
    r: Response = requests.get(
        BASE_URL + urllib.parse.urlencode({
            "artist_name": track.artist_name,
            "track_name": track.track_name,
            "album_name": track.album_name,
            "duration": track.duration
        }),
        headers=HEADERS)
    return r.json()
