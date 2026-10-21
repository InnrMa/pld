from returns.result import Failure

from models.audio_file import AudioFile

class Track:
    album_name: str
    track_name: str
    artist_name: str
    duration: int

    def __init__(self, audio_file: AudioFile):
        metadata = audio_file.get_metadata_as_dict()
        if Failure(metadata):
            raise metadata.failure()
        metadata = metadata.

        self.album_name = metadata["album"][0]
        self.track_name = metadata["title"][0]
        self.artist_name = metadata["artist"][0]
        self.duration = audio_file.file_length