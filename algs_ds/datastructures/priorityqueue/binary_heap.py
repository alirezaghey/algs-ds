# A binary heap implementation
#
#
# Author: Alireza Ghey

from typing import List, Any

class BinaryHeap:
    # construct a priority queue using heapify in O(n) time, if there are any elements
    # Explanation: http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
    def __init__(self, elems: List[Any]=None) -> None:
        self._heap = elems if elems else []
        self._heapSize = self._heapCapacity =  len(elems) if elems else 0

        # Heapify if there are any elements, O(n)
        for i in range(max(0, (self._heapSize // 2) -1), -1, -1):
            self.sink(i)
    
    # Whether priority queue is empty
    # TC: O(1)
    def isEmpty(self) -> bool:
        return self._heapSize == 0
    
    # Clears everything inside the heap
    # TC: O(n)
    def clear(self) -> None:
        pass

    # Returns the size of the heap
    def __len__(self) -> int:
        return self._heapSize
    
    def __str__(self) -> str:
        return str(self._heap)
    
    # Returns the element with the lowest value (highest priority/root of the heap)
    # If the priority queue is empty, returns None
    # TC: O(1)
    def peek(self) -> Any:
        if self.isEmpty(): return None
        return self._heap[0]
    
    # Removes the element with the lowest value (highest priority/root of the heap)
    # and returns it
    # If the heap is empty, returns None
    # TC: O(1)
    def poll(self) -> Any:
        return self.removeAt(0)
    
    # Whether element is in heap
    # TC: O(n)
    def contains(self, data: Any) -> bool:
        return data in self._heap
    
    # Adds element to priority queue
    # element cannot be None
    # TC: O(log n)
    def add(self, elem: Any) -> None:
        if elem == None:
            raise ValueError("Element cannot be None")

        if self._heapSize < self._heapCapacity:
            self._heap[self._heapSize] = elem
        else:
            self._heap.append(elem)
            self._heapCapacity += 1
        
        self.bubbleUp(self._heapSize)
        self._heapSize += 1
        
    # perform a bottom up node bubble
    # TC: O(log n)
    def bubbleUp(self, k: int):
        
        # Grap the index of the closest parent WRT k
        parent = (k - 1) // 2

        # keep bubbling up while we haven't reached the root
        # and our node's val is less than its parent
        while k > 0 and self._heap[k] < self._heap[parent]:
            # swapt parent and child
            self._heap[k], self._heap[parent] = self._heap[parent], self._heap[k]
            k = parent

            # grab the next parent index WRT k
            parent = (k-1) // 2

    # Top down node sink
    # TC: O(log n)
    def sink(self, k: int):
        while True:
            left = 2 * k + 1 # left child
            right = 2 * k + 2 # right child
            smallest = left # Assume left is the smallest node of the two children

            # find which is smaller, left or right
            # if right is smaller, set smallest to be right child
            if right < self._heapSize and self._heap[right] < self._heap[left]:
                smallest = right
        
            # Stop if we're outside of the bounds of the tree
            # or k is already smaller than smallest
            if left >= self._heapSize or self._heap[k] <= self._heap[smallest]:
                break

            self._heap[k], self._heap[smallest] = self._heap[smallest], self._heap[k]
            k = smallest

    # Removes a particular element in the heap
    # TC: O(n)
    def remove(self, elem: Any) -> bool:
        if elem == None:
            return False
        
        # linear removal through search, O(n)
        for i, el in enumerate(self._heap):
            if el == elem:
                self.removeAt(i)
                return True
        
        # elem not found
        return False
    
    # Removes a node at a particular index
    # TC: O(log n)
    def removeAt(self, i: int):
        if self.isEmpty(): return None

        self._heapSize -= 1
        removed_data = self._heap[i]
        # swap the node to be removed with the last node
        self._heap[self._heapSize], self._heap[i] = self._heap[i], self._heap[self._heapSize]
        # clear the last node
        self._heap[self._heapSize] = None

        # If removed data was already the last node from the beginning
        # no need to further sink anything
        if i == self._heapSize: return removed_data

        # We try both sinking and bubbling up if sinking did not work
        elem = self._heap[i]
        self.sink(i)

        # If sinking did not work, we bubble up
        if self._heap[i] == elem:
            self.bubbleUp(i)
        
        return removed_data

    # Recursively checks if this heap is a min heap
    # This method is just for testing purposes to make sure
    # the heap invariant is still being maintained
    # Call method with k == 0 to start at the root
    def _isMinHeap(self, k: int) -> bool:
        # If we are outside of the heap's bounds return true
        if k >= self._heapSize: return True

        left = 2 * k + 1
        right = 2 * k + 2

        if left < self._heapSize and self._heap[k] > self._heap[left]: return False
        if right < self._heapSize and self._heap[k] > self._heap[right]: return False

        return self._isMinHeap(left) and self._isMinHeap(right)

    
    
    


        