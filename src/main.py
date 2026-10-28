import argparse
import sys
from pathlib import Path

from result import Result, is_err

from services.lyrics_getter import LyricsGetter
from services.lyrics_processor import LyricsProcessor
from services.lyrics_writer import LyricsWriter
from services.dir_searcher import DirSearcher
from utils.advanced_error import AdvancedError
from utils.report import Report


def build_parser() -> argparse.ArgumentParser:
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

    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    target_dir: Path = args.dir
    verbose: bool = args.verbose
    overwrite: bool = args.overwrite
    ignore_errors: bool = args.ignore_errors
    write_metadata: bool = args.write_metadata

    if not target_dir.is_dir():
        parser.error(f"'{args.dir}' is not a valid directory.")

    searcher: DirSearcher = DirSearcher(target_dir)
    getter: LyricsGetter = LyricsGetter(ignore_errors)
    writer: LyricsWriter = LyricsWriter(write_metadata, overwrite)

    processor: LyricsProcessor = LyricsProcessor(searcher, getter, writer)

    try:
        report_res: Result[Report[str, AdvancedError[int]], AdvancedError[int]] = processor.process_all()
    except KeyboardInterrupt:
        print("\n\nOperation aborted by user.", file=sys.stderr)
        return 130

    if is_err(report_res):
        print(f"\n[FATAL] {report_res.err_value.error_message}", file=sys.stderr)
        return report_res.err_value.error

    report = report_res.ok_value
    print("\nPROCESSING COMPLETE")
    print("=" * 30)
    print(f"Total songs scanned: {report.total()}")
    print(f"Successfully downloaded lyrics: {report.no_successes()}")
    print(f"Failures: {report.no_failures()}")

    return 0

if __name__ == "__main__":
    sys.exit(main())