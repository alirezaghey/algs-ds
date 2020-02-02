from __future__ import annotations
from typing import Any

# A doubly linked list implementation
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

    # Add node to the head of linked list
    # TC: O(1)
    def addFirst(self, data: Any) -> None:
        if self.isEmpty():
            self._head = self._tail = _Node(data)
        else:
            self._head.prev = _Node(data, None, self._head)
            self._head = self._head._prev
        self._size += 1

    # Add node at the specified index
    # TC: O(n)
    def addAt(self, index: int, data: Any) -> None:
        if index < 0 or index >= len(self):
            raise ValueError("Specified index is out of range")

        if index == 0:
            self.addFirst(data)
        elif index == len(self):
            self.addLast(data)
        else:
            curr = self._head
            for _ in range(index-1):
                curr = curr._next
            newNode = _Node(data, curr, curr._next)
            curr._next = newNode
            curr._next._prev = newNode
        
        self._size += 1


    # Return data of head node
    # TC: O(1)
    def peekFirst(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")
        return self._head._data

    # Return data of tail node
    # TC: O(1)
    def peekLast(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")
        return self._tail._data

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
    
    # Removes tail node and returns its data
    # TC: O(1)
    def removeLast(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")

        if len(self) == 1:
            data = self._tail._data
            self._head = self._tail = None
        else:
            data = self._tail._data
            self._tail = self._tail._prev
            self._tail._next.prev = None
            self._tail._next = None
        
        self._size -= 1
        return data
        


    # Removes node at specified index and returns its data
    # TC: O(n)
    def removeAt(self, index: int) -> Any:
        if index < 0 or index >= len(self):
            raise ValueError("Index out of range")

        if index == 0:
            return self.removeFirst()
        elif index == len(self)-1:
            return self.removeLast()
        else:
            curr = self._head
            for _ in range(index):
                curr = curr._next
            data = curr._data
            curr._prev._next = curr._next
            curr._next._prev = curr._prev
            curr._next = curr._prev = None
            self._size -= 1
            return data
    
    # Removes the first node that has data equal to data
    # TC: O(n)
    def remove(self, data: Any) -> bool:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")

        curr = self._head
        while curr != None:
            if curr._data == data:
                curr._prev._next = curr._next
                curr._next._prev = curr._prev
                self._size -= 1
                return True
            curr = curr._next
        
        return False

    # Returns index of first node with data equal to data
    # Returns -1 if not found
    # TC: O(n)
    def indexOf(self, data: Any) -> int:
        index, curr = 0, self._head

        while curr != None:
            if curr._data == data:
                return index
            index += 1
            curr = curr._next
        
        return -1

    # Returns whether linked list has a node with data that equals data
    # TC: O(n)
    def contains(self, data: Any) -> bool:
        return self.indexOf(data) != -1

    
    # TODO: Implement iterator