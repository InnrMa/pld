from mutagen import File, MutagenError
from returns.result import Result, Success, Failure

class AudioFile:
    file_type: str
    file_length: int
    file_path: str

    def __init__(self, file_path: str):
        self.file_path = file_path
        audio = File(file_path)
        if audio is None or audio.info is None: raise ValueError("Unsupported or invalid audio file.")
        self.file_length = int(audio.info.length)
        self.file_type = type(audio).__name__

    def get_metadata_as_dict(self) -> Result[dict, str]:
        try:
            audio = File(self.file_path)
            if audio is None or audio.info is None:
                return Failure(f"'{self.file_path}' is not a valid audio file.")

            return Success(dict(audio))

        except MutagenError as e:
            return Failure(f"Corrupt audio file: {e}")

        except (FileNotFoundError, PermissionError) as e:
            return Failure(f"OS error: {e}")
