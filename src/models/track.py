from result import is_ok

from models.audio_file import AudioFile

class Track:
    audio_file: AudioFile
    album_name: str
    track_name: str
    artist_name: str
    duration: int

    def __init__(self, audio_file: AudioFile):
        self.audio_file = audio_file
        metadata = audio_file.get_metadata_as_dict()

        if is_ok(metadata):
            metadata = metadata.ok_value
            self.album_name = metadata["album"][0]
            self.track_name = metadata["title"][0]
            self.artist_name = metadata["artist"][0]
            self.duration = metadata["duration"][0]

    def __str__(self) -> str:
        return f"{self.artist_name} - {self.album_name} - {self.track_name} - {self.duration}sec"