import requests
from requests import Response

BASE_URL: str = "https://lrclib.net"
HEADERS = {'user-agent': 'pld v0.0.1 (innmax001@gmail.com)'}

def get_lyrics():
    r: Response = requests.get(
        BASE_URL + "/api/get?artist_name=Fujii+Kaze&track_name=%E4%BD%95%E3%81%AA%E3%82%93w&album_name=HELP+EVER+HURT+NEVER&duration=319",
        headers=HEADERS)
    return r.json()

print(get_lyrics())