# A Hashtable implementation
#
#
# Author: Alireza Ghey

from typing import Any, Optional, List, Iterator
from collections.abc import Hashable
from singlylinkedlist import SinglyLinkedList

class Entry:
    def __init__(self, k: Any, v: Any):
        if not isinstance(k, Hashable):
            raise TypeError(f"Unhashable type {type(k)}")
        self.key = k
        self.value = v
        self.hash = hash(k)
        

    def __eq__(self, other: Entry) -> bool:
        if self.hash != other.hash: return False
        return self.key == other.key

    def __str(self):
        return str(self.key) + " => " + str(self.value)
    

class HashtableSeparateChaining:
    DEFAULT_CAPACITY = 3
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, capacity: Optional[int], max_load_factor: Optional[float]):
        if capacity < 0: raise ValueError("Illegal capacity")
        if 0 >= max_load_factor >= 1: raise ValueError("Max load factor must be between 0 and 1, exclusive")

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
        if entry != None: return entry.value


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
            self.table[bucket_index] = SinglyLinkedList()
        
        existent_entry = bucket.find(entry.k)
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
                res.append("\n", "\t", str(entry))
        res.append("\n", "}")
        return "".join(res)
    











    








    
