import os
from pathlib import Path

from result import is_err

from models.audio_file import AudioFile
from models.track import Track


class DirSearcher:
    target_dir: Path

    def __init__(self, target_dir: Path):
        self.target_dir = target_dir

    def get_tracklist(self) -> list[Track]:
        tracklist: list[Track] = []
        for (root, dirs, files) in os.walk(self.target_dir):
            if len(files) == 0:
                continue

            for file in files:
                file_path = root + "/" + file
                audio_file: AudioFile = AudioFile(file_path)
                audio_metadata = audio_file.get_metadata_as_dict()
                if is_err(audio_metadata):
                    print(audio_metadata.err_value)
                    continue
                tracklist.append(
                    Track(audio_file))
        return tracklist