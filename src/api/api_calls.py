import requests
import urllib.parse
from models.track import Track
from result import Result, Ok, Err

from utils.advanced_error import AdvancedError

HEADERS = {'user-agent': 'pld v0.0.1 (innmax001@gmail.com)'}
BASE_URL: str = "https://lrclib.net"

def lrc_lib_request(track: Track) -> Result[dict, AdvancedError[int]]:
    i: int = 0
    while True:
        r = requests.get(
            BASE_URL + "/api/get?" + urllib.parse.urlencode({
                "artist_name": track.artist_name,
                "track_name": track.track_name,
                "album_name": track.album_name,
                "duration": track.duration
            }),
            headers=HEADERS)
        if r.status_code != 503 or i == 2:
            break
        i += 1

    status_code: int = r.status_code

    match status_code:
        # success cases
        case 200:
            return Ok(r.json())
        # error cases
        case 400:
            return Err(AdvancedError(f"A parameter failed validation. status-code: {status_code}", status_code, False))
        case 404:
            return Err(AdvancedError(f"No lyrics record matched the request. status-code: {status_code}", status_code, False))
        case 429:
            return Err(AdvancedError(f"Rate limit exceeded. Try again later. status-code: {status_code}", status_code, False))
        case 503:
            return Err(AdvancedError(f"The requested server is busy. status-code: {status_code}", status_code, False))
        # fatal error cases
        case 401:
            return Err(AdvancedError(f"The server doesn't recognise this application as trusted. status-code: {status_code}", status_code, True))
        case 403:
            return Err(AdvancedError(f"The client does not have access rights to the content. status-code: {status_code}", status_code, True))
        case 500:
            return Err(AdvancedError(f"The server has encountered a situation it does not know how to handle. status-code: {status_code}", status_code, True))
        case 501:
            return Err(AdvancedError(f"The request method is not supported by the server and cannot be handled. status-code: {status_code}", status_code, True))

    return Err(AdvancedError(f"An unknown server error occurred. status-code: {status_code}", status_code, True))