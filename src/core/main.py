import os
from result import is_err, is_ok
from models.audio_file import AudioFile
from models.track import Track
from services.lyrics_getter import LyricsGetter
from services.lyrics_writer import LyricsWriter

MSC_DIR: str = "/home/betten/Music/"

def get_tracklist() -> list[Track]:
    tracklist: list[Track] = []
    print(os.getcwd())
    for (root,dirs,files) in os.walk(MSC_DIR):
        if len(files) == 0:
            continue

        for file in files:
            file_path = root + "/" + file
            audio_file: AudioFile = AudioFile(file_path)
            audio_metadata = audio_file.get_metadata_as_dict()
            if is_err(audio_metadata):
                print(audio_metadata.err_value)
                continue
            #tracklist.append(
            #    Track(audio_file))
            print(audio_file.get_metadata_as_dict().ok_value)
    return tracklist


tracklist = get_tracklist()
'''
for track in tracklist:
    print(track)

request = LyricsGetter.get_lyrics(tracklist)
if is_ok(request):
    pairs = request.ok_value
    for pair in pairs:
        answer = LyricsWriter.write_to_file(pair)
        if is_ok(answer):
            print(answer.is_ok())
        if is_err(answer):
            print(answer.err_value)
if is_err(request):
    print(request.err_value.error_message)
'''