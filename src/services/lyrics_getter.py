from api.api_calls import lrc_lib_request
from models.lyric_container import LyricContainer
from models.track import Track
from result import Result, Ok, Err, is_ok, is_err

from utils.advanced_error import AdvancedError


class LyricsGetter:
    _is_verbose: bool
    _is_ignoring_errors: bool

    def __init__(self, is_verbose: bool, is_ignoring_errors: bool):
        self._is_verbose = is_verbose
        self._is_ignoring_errors = is_ignoring_errors

    def get_lyrics(self, track: Track) -> Result[LyricContainer, AdvancedError[int]]:
        lyric_container: LyricContainer

        request: Result[dict, AdvancedError[int]] = lrc_lib_request(track)

        if is_err(request):
            return Err(request.err_value)

        file_path: str = track.audio_file.file_path
        lyric_container = LyricContainer(file_path, request.ok_value.get("plainLyrics"), request.ok_value.get("syncedLyrics"))
        return Ok(lyric_container)