from result import is_ok
from models.audio_file import AudioFile

class Track:
    audio_file: AudioFile
    album_name: str | None
    track_name: str | None
    artist_name: str | None
    duration: int | None

    def __init__(self, audio_file: AudioFile):
        self.audio_file = audio_file
        metadata = audio_file.get_metadata_as_dict()

        if is_ok(metadata):
            metadata = metadata.ok_value
            self.album_name = val if isinstance(val := metadata.get("album"), str) else None
            self.track_name = val if isinstance(val := metadata.get("title"), str) else None
            self.artist_name = val if isinstance(val := metadata.get("artist"), str) else None
            self.duration = val if isinstance(val := metadata.get("duration"), int) else None

    def __str__(self) -> str:
        return f"{self.artist_name} - {self.album_name} - {self.track_name} - {self.duration}sec"