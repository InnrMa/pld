from api.api_calls import lrc_lib_call
from models.lyric_pair import LyricPair
from models.track import Track

class LyricsGetter:
    @staticmethod
    def get_lyrics(tracklist: list[Track]) -> list[LyricPair]:
        lyric_pairs: list[LyricPair] = []
        for track in tracklist:
            file_path: str = track.audio_file.file_path
            lrc: str = lrc_lib_call(track)
            lyric_pairs.append(LyricPair(file_path, lrc))
        return lyric_pairs