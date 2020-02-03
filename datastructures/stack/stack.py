from __future__ import annotations
from typing import Any, List

# A stack implementation using Python's built in lists
#
#
# Author: Alireza Ghey

class Stack:
    def __init__(self, firstElem: Any=None):
        self._data: List[Any] = [firstElem] if firstElem != None else []

    def __len__(self):
        return len(self._data)
    
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    def push(self, el: Any) -> None:
        self._data.append(el)

    def pop(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Stack is empty")
        return self._data.pop()

    def peek(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Stack is empty")
        return self._data[-1]