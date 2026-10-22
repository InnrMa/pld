from mutagen import File, MutagenError
from result import Result, Ok, Err

class AudioFile:
    file_path: str

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_metadata_as_dict(self) -> Result[dict, str]:
        try:
            audio = File(self.file_path)
            if audio is not None and audio.info is not None:
                metadata = dict(audio)
                metadata.setdefault("duration", [int(audio.info.length)])
                return Ok(metadata)

            return Err(f"'{self.file_path}' is not valid or unsupported.")

        except MutagenError as e:
            return Err(f"Corrupt audio file: {e}")

        except (FileNotFoundError, PermissionError) as e:
            return Err(f"OS error: {e}")