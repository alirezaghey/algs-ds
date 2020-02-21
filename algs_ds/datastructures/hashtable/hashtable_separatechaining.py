# A Hashtable implementation
#
#
# Author: Alireza Ghey

from __future__ import annotations
from typing import Any, Optional, List, Iterator
from collections.abc import Hashable

class Entry:
    def __init__(self, k: Any, v: Any):
        if not isinstance(k, Hashable):
            raise TypeError(f"Unhashable type {type(k)}")
        self.key = k
        self.value = v
        self.hash = hash(k)
        

    def __eq__(self, other: Entry) -> bool:
        if not isinstance(other, Entry) or self.hash != other.hash: return False
        return self.key == other.key

    def __str__(self):
        return str(self.key) + " => " + str(self.value)
    

class HashtableSeparateChaining:
    DEFAULT_CAPACITY = 3
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, capacity: Optional[int]=None, max_load_factor: Optional[float]=None):
        if capacity and capacity < 0: raise ValueError("Illegal capacity")
        if max_load_factor != None and (max_load_factor <= 0 or max_load_factor >= 1):
            raise ValueError("Max load factor must be between 0 and 1, exclusive")

        self.max_load_factor = max_load_factor or HashtableSeparateChaining.DEFAULT_LOAD_FACTOR
        self.capacity = capacity or HashtableSeparateChaining.DEFAULT_CAPACITY
        self.threshold = int(self.capacity * self.max_load_factor)
        self.table = [None] * self.capacity
        self.size = 0

    # Returns number of elements currently inside the hashtable
    def __len__(self) -> int:
        return self.size

    # Returns whether hashtable is empty
    def isEmpty(self) -> bool:
        return len(self) == 0

    
    # Converts a hash value to an index in table.
    # Strips potential negative sign and places the hashvalue
    # in the domain [0, capacity)
    def _normalize_index(self, key_hash) -> int:
        return key_hash % self.capacity


    # Clears all the contents of the hashtable
    def clear(self):
        for i in range(len(self)):
            self.table[i] = None
        self.size = 0


    # Returns whether hashtable contains specific key
    def contains_key(self, k: Any) -> bool:
        return self.has_key(k)

    
    # Returns whether hashtable contains specific key
    def has_key(self, k: Any) -> bool:
        bucket_index = self._normalize_index(hash(k))
        return self._bucket_seek_entry(bucket_index, k) != None


    # insert, put, and add all place a key value pair in hashtable
    def put(self, k: Any, v: Any) -> Any:
        return self.insert(k, v)

    
    def add(self, k: Any, v: Any) -> Any:
        return self.insert(k, v)


    def insert(self, k: Any, v: Any) -> Any:
        if k == None: raise ValueError("Null key")

        new_entry = Entry(k, v)
        bucket_index = self._normalize_index(new_entry.hash)
        return self._bucket_insert_entry(bucket_index, new_entry)


    # Gets a key's value from the map and returns the value.
    # NOTE: returns None if the value is None AND also returns
    # None if the key does not exists.
    def get(self, k: Any) -> Any:
        if k == None: return None

        bucket_index = self._normalize_index(hash(k))
        entry = self._bucket_seek_entry(bucket_index, k)
        if not entry is None: return entry.value


    # Removes a key from the map and returns the value
    # NOTE: returns None if the value is None AND also
    # returns None if the key does not exist.
    def remove(self, k: Any) -> Any:
        if k == None: raise ValueError("Null key")

        bucket_index = self._normalize_index(k)
        return self._bucket_remove_entry(bucket_index, k)

    
    # Removes an entry from a given bucket if it exists
    # and returns its value
    def _bucket_remove_entry(self, bucketIndex: int, k: Any) -> Any:
        if k == None: raise ValueError("Null key")

        l = self.table[bucketIndex]
        if l == None: return None
        entry = Entry(k, 0)
        data = l.remove(entry)
        if data != None: return data.value
        else: return None


    # Inserts an entry in a given bucket only if the entery does not already
    # exist in the given bucket, otherwise updates the entry value
    # Returns old value if entry existed, else None
    def _bucket_insert_entry(self, bucket_index: int, entry: Entry) -> Any:
        bucket = self.table[bucket_index]
        if bucket == None:
            bucket = self.table[bucket_index] = SinglyLinkedList()
        
        existent_entry = bucket.find(entry.key)
        if existent_entry == None:
            bucket.add(entry)
            self.size += 1
            if self.size > self.threshold:
                self._resize_table()
            return None # Indicates that the entry was non-existent
        else:
            old_val = existent_entry.value
            existent_entry.value = entry.value
            return old_val
        

    # Finds and returns a particular entry in a given bucket if it exists,
    # returns None otherwise    
    def _bucket_seek_entry(self, bucketIndex: int, k: Any) -> Entry:
        if k == None: raise ValueError("Null key")

        l = self.table[bucketIndex]
        if l == None: return None
        entry = l.find(k)
        if entry != None:
            return entry
        return None


    
    # Resizes the internal table holding buckets of entries
    def _resize_table(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.max_load_factor)

        newTable = [None] * self.capacity

        for i in range(len(self.table)):
            if self.table[i] == None: continue
            for entry in self.table[i].entries():
                bucket_index = self._normalize_index(entry.hash)
                bucket = newTable[bucket_index] if newTable[bucket_index] != None else SinglyLinkedList()
                newTable[bucket_index] = bucket
                bucket.add(entry)
            
            self.table[i].clear()
            self.table[i] = None
        
        self.table = newTable

    # Returns an Iterator over the keys found in the hashtable
    def keys(self) -> Iterator:
        for el in self.table:
            if el == None: continue
            for entry in el.entries():
                yield entry.key


    # Returns an Iterator over the values found in the hashtable
    def values(self) -> Iterator:
        for el in self.table:
            if el == None: continue
            for entry in el.entries():
                yield entry.value

    
    # Returns an Iterator over the key/value pairs in the hashtable
    # Key and values are packages ad (key, value) tuples
    def items(self) -> Iterator:
        for el in self.table:
            if el == None: continue
            for entry in el.entries():
                yield (entry.key, entry.value)


    # Returns a string representation of the hashtable
    def __str__(self) -> str:
        res = ["{"]
        for el in self.table:
            if el == None: continue
            for entry in el.entries():
                res.extend(["\n", "\t", str(entry)])
        res.extend(["\n", "}"])
        return "".join(res)





# A singly linked list implementation
# for use in a hashtable with separate chaining
#
# Author: Alireza Ghey

# private Node class for internal use
class _Node:
    def __init__(self, data: Any, nextNode: _Node=None):
        self._data: Any = data
        self._next: _Node = nextNode
    
    def __str__(self):
        return str(self._data)

class SinglyLinkedList:
    

    def __init__(self):
        self._size: int = 0
        self._head: _Node = None
        self._tail: _Node = None

    def __len__(self):
        return self._size

    
    # Deletes all nodes in the linked list
    # TC: O(n)
    def clear(self) -> None:
        curr = self._head
        while curr != None:
            nextNode = curr._next
            curr._next = None
            curr._data = None
            curr = nextNode
        
        self._head = self._tail = None
        self._size = 0

    # Whether linked list is empty or not
    def isEmpty(self) -> bool:
        return len(self) == 0
    

    # Add a node to the head of the linked list
    # Wrapper for addFirst
    # TC: O(1)
    def add(self, entry) -> None:
        self.addFirst(entry)
    
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

    # Adds a node to the tail of the linked list
    # TC: O(1)
    def addLast(self, data: Any) -> None:
        if self.isEmpty():
            self._head = self._tail = _Node(data)
        else:
            self._tail.next = _Node(data)
            self._tail = self._tail._next
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
    # Returns the removed node's data or None if not found
    # TC: O(n)
    def remove(self, data: Any) -> Any:
        if len(self) == 0:
            raise RuntimeError("Linked list is empty")

        if self._head._data == data:
            return self.removeFirst()

        curr = self._head
        while curr._next:
            if curr._next._data == data:
                if curr._next == self._tail:
                    return self.removeLast()
                removingNode = curr._next
                curr._next = removingNode._next
                removingNode._next = None
                self._size -= 1
                return removingNode._data
        return None

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

    # finds and returns an entry if keys are equal, else None
    # TC: O(n)
    def find(self, k: Any):
        curr = self._head

        while curr:
            if curr._data.key == k:
                return curr._data
            curr = curr._next
        return None

    def entries(self) -> Iterator:
        curr = self._head
        while curr:
            yield curr._data
            curr = curr._next

    def contains(self, data: Any) -> bool:
        return self.indexOf(data) != -1

    # TODO: Implement iterator
    

    











    








    
