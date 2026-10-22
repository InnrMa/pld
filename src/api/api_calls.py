import requests
from models.track import Track
import urllib.parse

HEADERS = {'user-agent': 'pld v0.0.1 (innmax001@gmail.com)'}
BASE_URL: str = "https://lrclib.net"

def lrc_lib_call(track: Track):
    r = requests.get(
        BASE_URL + "/api/get?" + urllib.parse.urlencode({
            "artist_name": track.artist_name,
            "track_name": track.track_name,
            "album_name": track.album_name,
            "duration": track.duration
        }),
        headers=HEADERS)
    return r.json()