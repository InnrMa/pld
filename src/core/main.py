import os
from mutagen import File, MutagenError
from result import Result, Ok, Err, is_err, is_ok
from models.audio_file import AudioFile
from models.track import Track
from services.lyrics_getter import LyricsGetter

music_directory: str = "/home/betten/Music/Fujii Kaze"

def get_tracklist() -> list[Track]:
    tracklist: list[Track] = []
    print(os.getcwd())
    for (root,dirs,files) in os.walk(music_directory):
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

tracklist = get_tracklist()
for track in tracklist:
    print(track)

pairs = LyricsGetter.get_lyrics(tracklist)
for pair in pairs:
    print(pair)