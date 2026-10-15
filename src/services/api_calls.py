import requests
from requests import Response

BASE_URL: str = "https://lrclib.net"
HEADERS = {'user-agent': 'pld v0.0.1 (innmax001@gmail.com)'}

def get_lyrics(artist_data):
    r: Response = requests.get(
        BASE_URL + "/api/get?artist_name=" + artist_data[0] + "&track_name=I+Want+to+Live&album_name=Baldur%27s+Gate+3+(Original+Game+Soundtrack)&duration=233",
        headers=HEADERS)
    return r.json()

