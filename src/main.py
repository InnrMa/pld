import argparse
import os
from argparse import Namespace
from pathlib import Path
from result import Result, is_err, is_ok

from models.audio_file import AudioFile
from models.lyric_container import LyricContainer
from models.track import Track
from services.lyrics_getter import LyricsGetter
from services.lyrics_writer import LyricsWriter
from utils.advanced_error import AdvancedError


def get_tracklist(target_dir: Path) -> list[Track]:
    tracklist: list[Track] = []
    print(os.getcwd())
    for (root,dirs,files) in os.walk(target_dir):
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

def main():
    parser = argparse.ArgumentParser(description="Get lyrics through LRCLIB for audio files in a directory")

    parser.add_argument(
        "dir",
        type=Path,
        help="Path to the directory containing files"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print detailed processing logs (currently does nothing)"
    )

    parser.add_argument(
        "-o", "--overwrite",
        action="store_true",
        help="Overwrite existing lyrics with newly pulled ones"
    )

    parser.add_argument(
        "-i", "--ignore-errors",
        action="store_true",
        help="Ignore all errors and writes lyrics regardless of the state"
    )

    parser.add_argument(
        "-w", "--write-metadata",
        action="store_true",
        help="Write lyrics directly into the metadata of files instead of writing to external files"
    )

    args = parser.parse_args()

    target_dir: Path = args.dir
    is_verbose: bool = args.verbose
    is_overwritable: bool = args.overwrite
    is_ignoring_errors: bool = args.ignore_errors
    is_writing_metadata: bool = args.write_metadata

    if not target_dir.is_dir():
        parser.error(f"'{args.dir}' is not a valid directory.")

    tracklist: list[Track] = get_tracklist(target_dir)
    getter: LyricsGetter = LyricsGetter(is_verbose, is_ignoring_errors)
    writer: LyricsWriter = LyricsWriter(is_writing_metadata, is_overwritable)

    for track in tracklist:
        lrc_containers: Result[LyricContainer, AdvancedError[int]] = getter.get_lyrics(track)
        if is_err(lrc_containers):
            ...


if __name__ == "__main__":
    main()