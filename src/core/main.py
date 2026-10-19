import os

from mutagen import File
from mutagen.flac import FLAC
from models import Track
from ..services.api_calls import get_lyrics

music_directory: str = "/home/betten/Music/Fujii Kaze"
tracks: list[Track] = []

def is_flac(file_path: str) -> bool:
    signature = bytes([0x66, 0x4C, 0x61, 0x43])
    with open(file_path, "rb") as f:
        return f.read(4) == signature

def get_audio_duration(file_path: str) -> int:
    audio = File(file_path)
    if audio is not None and audio.info is not None:
        return int(audio.info.length)
    raise ValueError("Unsupported or invalid audio file.")

def get_songs_in_directory():
    print(os.getcwd())
    for (root,dirs,files) in os.walk(music_directory):
        if len(files) == 0:
            continue

        for file in files:
            if is_flac(root + "/" + file):
                file_path = root + "/" + file
                metadata = dict(FLAC(file_path).tags)
                tracks.append(Track(metadata["album"][0], metadata["title"][0], metadata["artist"][0], get_audio_duration(file_path)))



get_songs_in_directory()
for track in tracks:
    print(track.get_url())