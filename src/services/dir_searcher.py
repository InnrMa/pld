import os
from pathlib import Path

from result import is_err, Result, Ok, Err

from models.audio_file import AudioFile
from models.track import Track
from utils.advanced_list import AdvancedList
from utils.advanced_error import AdvancedError

class DirSearcher:
    target_dir: Path

    def __init__(self, target_dir: Path):
        self.target_dir = target_dir

    def get_tracklist(self) -> Result[AdvancedList[Track, AdvancedError], AdvancedError]:
        tracklist: AdvancedList[Track, AdvancedError] = AdvancedList()

        for (root, dirs, files) in os.walk(self.target_dir):
            for file in files:
                file_path = f"{root}/{file}"
                audio_file: AudioFile = AudioFile(file_path)
                audio_metadata = audio_file.get_metadata_as_dict()
                if is_err(audio_metadata):
                    if audio_metadata.err_value.is_fatal:
                        return audio_metadata
                    tracklist.failure.append(audio_metadata.err_value)
                    continue
                if Path(".".join((file_path.rsplit(".", 1)[0], "lrc"))).exists():
                    tracklist.failure.append(AdvancedError(f"Skipped '{file_path}' - file already exists.", 22, False))
                    continue
                tracklist.success.append(
                    Track(audio_file))

        return Ok(tracklist)

searcher = DirSearcher(Path("/home/betten/Music"))

res_tracklist = searcher.get_tracklist()