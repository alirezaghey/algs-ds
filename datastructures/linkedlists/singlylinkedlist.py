from typing import Any


# A singly linked list implementation
#
#
# Author: Alireza Ghey

class _Node:
    def __init__(self, data: Any, nextNode: _Node=None):
        self._data = data
        self._next = nextNode
    
    def __str__(self):
        return str(self._data)

class SinglyLinkedList:
    
    # private Node class for internal use

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    
    # Deletes all nodes in the linked list
    # TC: O(n)
    def clear(self) -> None:
        curr = self._head
        while curr != None:
            nextNode = curr._next
            curr._next = None
            curr = nextNode
        
        self._head = self._tail = None
        self._size = 0

    # Whether linked list is empty or not
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    # Adds a node to the tail of the linked list
    # TC: O(1)
    def addLast(self, data: Any) -> None:
        if self.isEmpty():
            self._head = self._tail = _Node(data)
        else:
            self._tail.next = _Node(data)
            self._tail = self._tail._next
        self._size += 1

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
            
    # Add a node at the specified index
    # TC: O(n)
    def addAt(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise ValueError("Specified index is out of range")
        
        if index == 0:
            self.addFirst(data)
        elif index == len(self):
            self.addLast(data)
        else:
            curr = self._head
            for _ in range(index-1):
                curr = curr._next
            newNode = _Node(data)
            newNode._next = curr._next
            curr._next = newNode
            self._size += 1
    
    # Return value of head if exists
    # TC: O(1)
    def peekFirst(self) -> Any:
        if len(self) == 0:
            raise RuntimeError("Linked list is empty")
        return self._head._data

    # Return value of tail if exists
    # TC: O(1)
    def peekLast(self) -> Any:
        if len(self) == 0:
            raise RuntimeError("Linked list is empty")
        return self._tail._data

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

    # Remove tail node and return its data
    # TC: O(n)
    def removeLast(self) -> Any:
        if self.isEmpty():
            raise RuntimeError("Linked list is empty")
        
        data = self._tail._data
        if len(self) == 1:
            self._head = self._tail = None            
        else:
            curr = self._head
            while curr._next and curr._next._next:
                curr = curr.next
            curr.next = None
            self._tail = curr
        
        self._size -= 1
        return data
            
    # Removes a node as specified index
    # TC: O(n)
    def removeAt(self, index: int) -> Any:
        if index < 0 or index >= len(self):
            raise ValueError("Index out of bounds")

        if index == 0:
            return self.removeFirst()
        if index == len(self)-1:
            return self.removeLast()
        
        curr = self._head
        for _ in range(index-1):
            curr = curr._next
        
        data = curr._next._data
        curr._next = curr._next._next
        self._size -= 1
        return data
        
    # Removes the first occurence the node with the specified data
    # TC: O(n)
    def remove(self, data: Any) -> bool:
        if len(self) == 0:
            raise RuntimeError("Linked list is empty")

        if self._head._data == data:
            self.removeFirst()
            return True

        curr = self._head
        while curr._next:
            if curr._next._data == data:
                if curr._next == self._tail:
                    self.removeLast()
                    return True
                removingNode = curr._next
                curr._next = removingNode._next
                removingNode._next = None
                self._size -= 1
                return True
        return False

    # Returns index of the first occurence of a node with data
    # TC: O(n)
    def indexOf(self, data: Any) -> int:
        curr = self._head
        index = 0
        while curr != None:
            if curr._data == data:
                return index
            index += 1
        return -1

    def contains(self, data: Any) -> bool:
        return self.indexOf(data) != -1

    # TODO: Implement iterator

    def __len__(self):
        return self._size
    
    