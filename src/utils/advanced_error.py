from dataclasses import dataclass

@dataclass
class AdvancedError:
    error_message: str
    error: int
    is_fatal: bool