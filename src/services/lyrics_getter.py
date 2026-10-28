from result import Result, Ok, Err, is_err

from api.api_calls import lrc_lib_request
from models.lyric_container import LyricContainer
from models.track import Track
from utils.advanced_error import AdvancedError


class LyricsGetter:
    _ignore_errors: bool

    def __init__(self, is_ignoring_errors: bool):
        self._ignore_errors = is_ignoring_errors

    def get_lyrics(self, track: Track) -> Result[LyricContainer, AdvancedError[int]]:
        lyric_container: LyricContainer

        request: Result[dict, AdvancedError[int]] = lrc_lib_request(track)

        if is_err(request):
            return Err(request.err_value)

        file_path: str = track.audio_file.file_path
        lyric_container = LyricContainer(file_path, request.ok_value.get("plainLyrics"), request.ok_value.get("syncedLyrics"))
        return Ok(lyric_container)