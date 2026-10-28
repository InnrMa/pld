from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class AdvancedError(Generic[T]):
    error_message: str
    error: T
    is_fatal: bool