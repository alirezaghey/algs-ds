from __future__ import annotations
from typing import Any

# A Queue implementation using a custom doubly linked list
#
#
# Author: Alireza Ghey



# A private Node implementation for the doubly linked list
class _Node:
    def __init__(self, data: Any, prevNode: _Node=None, nextNode: _Node=None):
        self._data: Any = data
        self._next: _Node = nextNode
        self._prev: _Node = prevNode
    
    def __str__(self):
        return str(self._data)

# A private DoublyLinkedList implementation for the Queue
class DoublyLinkedList:
    def __init__(self):
        self._size: int = 0
        self._head: _Node = None
        self._tail: _Node = None
    
    def __len__(self):
        return self._size
    
    # Empties the linked list
    # TC: O(n)
    def clear(self) -> None:
        curr = self._head
        while curr:
            nextNode = curr._next
            curr._next = curr._prev = None
            curr._data = None
            curr = nextNode
        self._head = self._tail = None
        self._size = 0

    # Whether linked list is empty or not
    # TC: O(1)
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    # Add node to the tail of linked list
    # TC: O(1)
    def addLast(self, data: Any) -> None:
        if self.isEmpty():
            self._head = self._tail = _Node(data)
        else:
            self._tail._next = _Node(data, self._tail, None)
            self._tail = self._tail._next
        self._size += 1

    # Return data of head node
    # TC: O(1)
    def peekFirst(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")
        return self._head._data

    # Removes head node and returns its data
    # TC: O(1)
    def removeFirst(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")

        if len(self) == 1:
            data = self._head._data
            self._head = self._tail = None
        else:
            data = self._head._data
            self._head = self._head._next
            self._head._prev._next = None
            self._head._prev = None

        self._size -= 1
        return data


class Queue:
    def __init__(self, firstEl: Any=None):
        self._data: DoublyLinkedList = DoublyLinkedList()
        if firstEl != None:
            self._data.addLast(firstEl)
    
    def __len__(self):
        return len(self._data)

    def isEmpty(self) -> int:
        return len(self) == 0
    
    def enque(self, el: Any) -> None:
        self._data.addLast(el)

    def deque(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Queue is empty")
        return self._data.removeFirst()

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Queue is empty")
        return self._data.peekFirst()