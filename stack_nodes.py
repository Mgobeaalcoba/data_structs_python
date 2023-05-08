from typing import Optional, Union
from typing import Iterable

from node import Node


class Stack:
    """A simple stack implementation."""

    _size: int
    _top: Optional[Node]

    def __init__(self, *items):
        """Initializes the stack."""

        self._top = None
        self._size = 0

        if len(items) > 0 and isinstance(items[0], Iterable):
            items = items[0]

        for item in items:
            self.push(item)

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """

        return self._size <= 0

    def clear(self):
        """Clears the stack."""

        self._top = None
        self._size = 0

    def copy(self):
        """Returns a copy of the stack.

        Caution: This method returns a shallow copy.

        Returns:
            Stack: A copy of the stack.
        """

        new_stack = Stack()

        new_stack._top = self._top

        return new_stack

    def depthcopy(self):
        """Returns a deep copy of the stack.

        Returns:
            Stack: A deep copy of the stack.
        """

        new_stack = Stack()

        new_stack._top = self._top.depthcopy()

        new_stack._size = self._size

        return new_stack

    def extend(self, other: 'Stack'):
        """Extends the current stack with the items of the other stack.

        Time complexity: O(n) where n is the length of the other stack.

        Args:
            other: The other stack to extend the current stack with.
        """

        if other._top is None:
            return None

        bottom_node = other._top

        while bottom_node.next is not None:
            bottom_node = bottom_node.next

        bottom_node.next = self._top

        self._top = other._top

        self._size += other._size

        return None

    def peek(self, raw: bool = False) -> Union[None, Node, object]:
        """Returns the top item of the stack.

        Raises IndexError if the stack is empty.

        Args:
            raw: If True returns the Node, otherwise it will return the node value.

        Returns:
            object: The top item of the stack.
        """

        if not self._top:
            raise IndexError('The stack is empty.')

        if raw:
            return self._top

        return self._top.value

    def push(self, value: object):
        """Pushes an item onto the stack.

        Time complexity: O(1)

        Args:
            item: The item to be pushed onto the stack.
        """

        self._top = Node(value, self._top)
        self._size += 1

    def pop(self, raw: bool = False):
        """Pops an item off the stack.

        Raises IndexError if the stack is empty.

        Time complexity: O(1)

        Args:
            raw: If True returns the Node, otherwise it will return the node value.

        Returns:
            object: The item that was popped off the stack.
        """

        if self._top is None:
            raise IndexError('The stack is empty.')

        temp = self._top

        self._top = temp.next

        self._size -= 1

        if raw:
            return temp

        return temp.value

    def __len__(self):
        """Returns the length of the stack.

        Time complexity: O(1)

        Returns:
            int: The length of the stack.
        """

        return self._size

    def __str__(self) -> str:
        """Returns a string representation of the stack.

        Time complexity: O(n)
        Space complexity: O(n)

        Returns:
            str: A string representation of the stack.
        """

        items = list(self)

        return str(items)

    def __contains__(self, item: object) -> bool:
        """Checks if the stack contains an item.

        Args:
            item: The item to check if the stack contains.

        Returns:
            bool: True if the stack contains the item, False otherwise.
        """

        pointer = self._top
        while pointer is not None:
            if pointer.value == item:
                return True

            pointer = pointer.next

        return False

    def itervalues(self) -> Iterable:
        """Returns an iterator over the values of the stack.

        Returns:
            iterator: An iterator over the values of the stack.
        """

        pointer = self._top

        while pointer is not None:
            yield pointer
            pointer = pointer.next

    def __iter__(self) -> Iterable:
        """Returns an iterator over the stack.

        Returns:
            iterator: An iterator over the stack.
        """

        return self.itervalues()

    def __add__(self, other):
        """Returns a new stack containing the items of both stacks.

        Args:
            other: The other stack to add to the current stack.

        Returns:
            Stack: A new stack containing the items of both stacks.
        """

        new_stack = self.depthcopy()
        new_stack.extend(other.depthcopy())

        return new_stack