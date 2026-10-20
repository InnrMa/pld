from typing import Literal

type AudioFile = Literal["mp3", "opus", "flac", "wav", "ogg", "m4a", "aac"]

def get_file_type(file_path: str) -> AudioFile:
    if _is_mp3(file_path): return "mp3"
    if _is_opus(file_path): return "opus"
    if _is_flac(file_path): return "flac"
    if _is_wav(file_path): return "wav"
    if _is_ogg(file_path): return "ogg"
    if _is_m4a(file_path): return "m4a"
    if _is_aac(file_path): return "aac"
    raise ValueError("Unsupported or invalid audio file.")

def _is_mp3(file_path: str) -> bool:
    """Check if file is a valid MP3 by magic bytes."""
    signature = bytes([0x49, 0x44, 0x33])
    with open(file_path, "rb") as f:
        return f.read(3) == signature

def _is_opus(file_path: str) -> bool:
    """Check if file is a valid OPUS by magic bytes."""
    signature = bytes(
        [0x4F, 0x67, 0x67, 0x53, 0x00, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E,
         0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x2E, 0x4F, 0x70, 0x75, 0x73, 0x48, 0x65, 0x61,
         0x64])
    with open(file_path, "rb") as f:
        return f.read(36) == signature

def _is_flac(file_path: str) -> bool:
    """Check if file is a valid FLAC by magic bytes."""
    signature = bytes([0x66, 0x4C, 0x61, 0x43])
    with open(file_path, "rb") as f:
        return f.read(4) == signature

def _is_wav(file_path: str) -> bool:
    """Check if file is a valid WAV by magic bytes."""
    signature = bytes([0x52, 0x49, 0x46, 0x46, 0x2E, 0x2E, 0x2E, 0x2E, 0x57, 0x41, 0x56, 0x45])
    with open(file_path, "rb") as f:
        return f.read(12) == signature

def _is_ogg(file_path: str) -> bool:
    """Check if file is a valid OGG by magic bytes."""
    signature = bytes([0x4F, 0x67, 0x67, 0x53, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    with open(file_path, "rb") as f:
        return f.read(14) == signature

def _is_m4a(file_path: str) -> bool:
    """Check if file is a valid M4A by magic bytes at offset 4."""
    signature = bytes([0x66, 0x74, 0x79, 0x70, 0x4D, 0x34, 0x41, 0x20])
    with open(file_path, "rb") as f:
        f.seek(4)
        return f.read(8) == signature

def _is_aac(file_path: str) -> bool:
    """Check if file is a valid AAC by magic bytes."""
    signature = bytes([0xFF, 0xF1])
    with open(file_path, "rb") as f:
        return f.read(2) == signature