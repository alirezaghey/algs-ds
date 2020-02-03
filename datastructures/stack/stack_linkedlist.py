from __future__ import annotations
from typing import Any

# A stack implementation using a custom singly linked list
#
#
# Author: Alireza Ghey

# private Node class for internal use
class _Node:
    def __init__(self, data: Any, nextNode: _Node=None):
        self._data: Any = data
        self._next: _Node = nextNode
    
    def __str__(self):
        return str(self._data)

# private bare minimum singly linked list for use by StackLinkedList
class SinglyLinkedList:
    

    def __init__(self):
        self._size: int = 0
        self._head: _Node = None
        self._tail: _Node = None

    def __len__(self):
        return self._size

    

    # Whether linked list is empty or not
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    # Add a node to the head of the linked list
    # TC: O(1)
    def addFirst(self, data: Any) -> None:
        if self.isEmpty():
            self._head = self._tail = _Node(data)
        else:
            newHead = _Node(data)
            newHead._next = self._head
            self._head = newHead
        self._size += 1
    
    # Return value of head if exists
    # TC: O(1)
    def peekFirst(self) -> Any:
        if len(self) == 0:
            raise RuntimeError("Linked list is empty")
        return self._head._data


    # Remove head node and return its data
    # TC: O(1)
    def removeFirst(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")
        
        data = self._head._data
        newHead = self._head._next
        self._head._next = None
        self._head = newHead
        
        self._size -= 1

        if self.isEmpty():
            self._tail = None
        
        return data  
    
class StackLinkedList:
    def __init__(self, firstElem: Any=None):
        self._data: SinglyLinkedList = SinglyLinkedList()
        if firstElem != None:
            self._data.addFirst(firstElem)
        
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self) == 0

    def push(self, el: Any):
        self._data.addFirst(el)

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Stack is empty")
        return self._data.removeFirst()

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Stack is empty")
        return self._data.peekFirst()


