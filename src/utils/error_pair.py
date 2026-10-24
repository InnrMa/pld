from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class ErrorPair(Generic[T]):
    error_message: str
    error: T
    fatal: bool