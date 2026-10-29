from pathlib import Path
from result import Result, Ok, Err
from models.lyric_container import LyricContainer
from utils.advanced_error import AdvancedError


def _write_to_file(file_path: str, lrc: str, is_overwritable: bool) -> str:
    if Path(file_path).exists() and not is_overwritable:
        return f"Skipping '{file_path}' - file already exists."
    else:
        file = open(file_path, "w")
        file.write(lrc)
        file.close()
        return f"'{file_path}' has been written to disk."

def _write_to_tags(file_path: str, lrc: str, overwrite: bool) -> str:
    return ""

class LyricsWriter:
    _is_writing_metadata: bool
    _is_overwritable: bool

    def __init__(self, is_writing_metadata, is_overwritable):
        self._is_writing_metadata = is_writing_metadata
        self._is_overwritable = is_overwritable

    def write_lyrics(self, lyric_container: LyricContainer) -> Result[str, AdvancedError]:
        if lyric_container.file_path is None:
            return Err(AdvancedError(f"Failed to write lyrics for '{lyric_container.file_path}'. Attribute `file_path` [None].", 22, False))

        lrc: str
        new_file_path: str = lyric_container.file_path.rsplit(".", 1)[0]
        if lyric_container.synced_lrc is not None:
            new_file_path = ".".join((new_file_path, "lrc"))
            lrc = lyric_container.synced_lrc
        elif lyric_container.plain_lrc is not None:
            new_file_path = ".".join((new_file_path, "txt"))
            lrc = lyric_container.plain_lrc
        else:
            return Err(AdvancedError(f"Failed to write lyrics for '{lyric_container.file_path}'. Attributes `synced_lrc` and `plain_lrc` are [None].", 22, False))

        return Ok(
            _write_to_tags(lyric_container.file_path, lrc, self._is_overwritable)
            if self._is_writing_metadata
            else _write_to_file(new_file_path, lrc, self._is_overwritable)
        )