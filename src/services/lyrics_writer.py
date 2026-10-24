from result import Result, Ok, Err

from models.lyric_pair import LyricPair


class LyricsWriter:
    @staticmethod
    def write_to_file(lyric_pair: LyricPair) -> Result[str, str]:
        if lyric_pair.file_path is None:
            return Err("Failed to write one file. Attribute `file_path` is [None].")

        new_file_path: str = lyric_pair.file_path.rsplit(".", 1)[0]
        if lyric_pair.synced_lrc is not None:
            new_file_path = ".".join((new_file_path, "lrc"))
            file = open(new_file_path, "w")
            file.write(lyric_pair.synced_lrc)
            file.close()
            return Ok(f"'{new_file_path}' has been written to disk. (synced lyrics)")
        if lyric_pair.plain_lrc is not None:
            new_file_path = ".".join((new_file_path, "txt"))
            file = open(new_file_path, "w")
            file.write(lyric_pair.plain_lrc)
            file.close()
            return Ok(f"'{new_file_path}' has been written to disk. (plain lyrics)")

        return Err("Failed to write one file. Attributes `synced_lrc` and `plain_lrc` are [None].")
