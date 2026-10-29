from plistlib import InvalidFileException

from mutagen import File, MutagenError, FileType
from result import Result, Ok, Err
from utils.advanced_error import AdvancedError


def _get_first(tags: dict, key):
    val = tags.get(key)
    if val is not None:
        val = val[0]
    return val


def _simplify_metadata(audio: FileType) -> dict:
    tags = dict(audio)
    duration = int(audio.info.length)

    return {
        "album": _get_first(tags, "album"),
        "title": _get_first(tags, "title"),
        "artist": _get_first(tags, "artist"),
        "duration": duration,
    }


class AudioFile:
    file_path: str

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_metadata_as_dict(self) -> Result[dict[str, str | int | None], AdvancedError]:
        try:
            audio: FileType = File(self.file_path, easy=True)
            if audio is not None and audio.info is not None:
                return Ok(_simplify_metadata(audio))

            return Err(AdvancedError(f"'{self.file_path}' is not valid or unsupported.", 74, False))

        except MutagenError as e:
            return Err(AdvancedError(f"Corrupt audio file: {e}", 74, False))

        except (FileNotFoundError, PermissionError) as e:
            error_code = e.errno if e.errno is not None else -1
            return Err(AdvancedError(f"OS error: {e}", error_code, True))

    def __str__(self) -> str:
        return f"{self.file_path} - {self.get_metadata_as_dict().is_ok()}"