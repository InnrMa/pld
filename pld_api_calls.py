import requests
BASE_URL: str = "https://lrclib.net"
HEADERS = {'user-agent': 'pld-python lyrics downloader v0.0.1 (innmax001@gmail.com)'}

class LrcLibApiCall:
    def get_lyrics(self, artist_data):
        r = requests.get(
            BASE_URL + "/api/get?artist_name=" + artist_data[0] + "&track_name=I+Want+to+Live&album_name=Baldur%27s+Gate+3+(Original+Game+Soundtrack)&duration=233",
            headers=HEADERS)
        return r.json()
