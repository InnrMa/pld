from api.api_calls import lrc_lib_request
from models.lyric_pair import LyricPair
from models.track import Track
from result import Result, Ok, Err, is_ok, is_err

from utils.error_pair import ErrorPair


class LyricsGetter:
    @staticmethod
    def get_lyrics(tracklist: list[Track]) -> Result[list[LyricPair], ErrorPair[int]]:
        lyric_pairs: list[LyricPair] = []

        for track in tracklist:
            request = lrc_lib_request(track)

            if is_err(request) and not request.err_value.fatal:
                if request.err_value.error in (400, 404, 503):
                    continue
                if request.err_value.error == 429:
                    return Err(request.err_value)
            if is_err(request):
                return Err(request.err_value)

            if is_ok(request):
                file_path: str = track.audio_file.file_path
                lyric_pairs.append(LyricPair(file_path, request.ok_value.get("plainLyrics"), request.ok_value.get("syncedLyrics")))
                print(file_path)
                print(request.ok_value.get("plainLyrics"))

        return Ok(lyric_pairs)