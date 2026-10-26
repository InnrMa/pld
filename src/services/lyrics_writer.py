from pathlib import Path
from result import Result, Ok, Err
from models.lyric_pair import LyricPair

def _write_lyrics(file_path: str, lrc: str) -> str:
    if Path(file_path).exists():
        return f"Skipping '{file_path}' - file already exists."
    else:
        file = open(file_path, "w")
        file.write(lrc)
        file.close()
        return f"'{file_path}' has been written to disk."


class LyricsWriter:
    @staticmethod
    def write_to_file(lyric_pair: LyricPair) -> Result[str, str]:
        if lyric_pair.file_path is None:
            return Err("Failed to write one file. Attribute `file_path` is [None].")

        new_file_path: str = lyric_pair.file_path.rsplit(".", 1)[0]
        if lyric_pair.synced_lrc is not None:
            new_file_path = ".".join((new_file_path, "lrc"))
            return Ok(_write_lyrics(new_file_path, lyric_pair.synced_lrc))
        if lyric_pair.plain_lrc is not None:
            new_file_path = ".".join((new_file_path, "txt"))
            return Ok(_write_lyrics(new_file_path, lyric_pair.plain_lrc))

        return Err(f"Failed to write lyrics for '{lyric_pair.file_path}'. Attributes `synced_lrc` and `plain_lrc` are [None].")
