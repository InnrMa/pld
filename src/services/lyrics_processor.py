from pathlib import Path

from result import Result, Err, Ok, is_err

from models.lyric_container import LyricContainer
from models.track import Track
from services.lyrics_getter import LyricsGetter
from services.lyrics_writer import LyricsWriter
from services.dir_searcher import DirSearcher
from utils.advanced_error import AdvancedError
from utils.report import Report


class LyricsProcessor:
    searcher: DirSearcher
    getter: LyricsGetter
    writer: LyricsWriter

    def __init__(self, searcher: DirSearcher, getter: LyricsGetter, writer: LyricsWriter):
        self.searcher = searcher
        self.getter = getter
        self.writer = writer

    def process_all(self) -> Result[Report[str, AdvancedError[int]], AdvancedError[int]]:
        report: Report[str, AdvancedError[int]] = Report()

        tracklist: list[Track] = self.searcher.get_tracklist()
        for track in tracklist:
            lrc_res: Result[LyricContainer, AdvancedError[int]] = self.getter.get_lyrics(track)
            if is_err(lrc_res):
                if lrc_res.err_value.is_fatal:
                    return Err(lrc_res.err_value)
                report.failure.append(lrc_res.err_value)
                if lrc_res.err_value.error == 429:
                    return Ok(report)
                continue

            write_res = self.writer.write_lyrics(lrc_res.ok_value)
            if is_err(write_res):
                if write_res.err_value.is_fatal:
                    return Err(write_res.err_value)
                report.failure.append(write_res.err_value)
                continue

            report.success.append(write_res.ok_value)

        return Ok(report)