from typing import Optional, Union
from typing import Iterable


class Stack:
    """A simple stack implementation with list."""

    _items: list

    def __init__(self, *items):
        self._items = list(*items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def clear(self) -> None:
        self._items.clear()

    def copy(self) -> 'Stack':
        stack = Stack()

        for item in self._items:
            stack.push(item)

        return stack

    def extend(self, other: Iterable) -> None:

        for item in reversed(other):
            self.push(item)

    def peek(self) -> Optional[object]:
        if self.is_empty():
            raise ValueError('Stack is empty.')

        return self._items[-1]

    def pop(self) -> Optional[object]:
        return self._items.pop()

    def push(self, item: object) -> None:
        self._items.append(item)

    def itervalues(self) -> Iterable:
        return reversed(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __contains__(self, item: object) -> bool:
        return item in self._items

    def __iter__(self) -> Iterable:
        return self.itervalues()

    def __repr__(self) -> str:
        return f'Stack({self._items})'

    def __reversed__(self) -> Iterable:
        return self._items

    def __add__(self, other: Union['Stack', Iterable]) -> 'Stack':
        stack = self.copy()

        if isinstance(other, Stack):
            stack.extend(other)
        else:
            stack.extend(other)

        return stack
