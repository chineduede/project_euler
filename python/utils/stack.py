from typing import Generic, List, TypeVar

__all__ = ["Stack"]


T = TypeVar("T", int, list)


class Stack(Generic[T]):
    """A minimal implementation of a stack"""

    def __init__(self) -> None:
        self._container: List[int] = []

    @property
    def is_empty(self) -> bool:
        return not self._container

    @property
    def length(self) -> int:
        return len(self._container)

    def pop(self) -> T:
        return self._container.pop()

    def push(self, item: T) -> None:
        self._container.append(item)

    def stackify(self, array: List) -> None:
        """Takes an array and adds its elements to the stack"""
        for ele in array:
            self._container.append(ele)

    def __repr__(self):
        return repr(self._container)
