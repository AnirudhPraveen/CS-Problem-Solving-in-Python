from typing import Generic, List, TypeVar
# creating a generic type
T = TypeVar('T')

class Stack[Generic[T]]:
    def __init__(self) -> None:
        self._container: List[T] = []