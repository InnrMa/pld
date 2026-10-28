from typing import TypeVar, Generic

T = TypeVar('T')
E = TypeVar('E')

class Report(Generic[T, E]):
    success: list[T]
    failure: list[E]

    def __init__(self):
        self.success = []
        self.failure = []

    def total(self) -> int:
        return len(self.success) + len(self.failure)

    def no_successes(self) -> int:
        return len(self.success)

    def no_failures(self) -> int:
        return len(self.failure)