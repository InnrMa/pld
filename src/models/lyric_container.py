from dataclasses import dataclass

@dataclass
class LyricContainer:
    file_path: str | None
    plain_lrc: str | None
    synced_lrc: str | None