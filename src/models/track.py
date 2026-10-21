class Track:
    album_name: str
    track_name: str
    artist_name: str
    duration: int

    def __init__(self, album_name: str, track_name: str, artist_name: str, duration: int):
        self.album_name = album_name
        self.track_name = track_name
        self.artist_name = artist_name
        self.duration = duration