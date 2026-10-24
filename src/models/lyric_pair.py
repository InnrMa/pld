from dataclasses import dataclass

@dataclass
class LyricPair:
    file_path: str | None
    plain_lrc: str | None
    synced_lrc: str | None