# A Disjoint Set implementation
#
#
# Author: Alireza Ghey

class DisjointSet:
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Size <= 0 is not allowed")
        # Number of elements in the whole disjoint set
        self._size = size

        # Size of each component. 1 at start as each element is in its own component
        self._componentSizes = [1] * size

        # parent of each element. id[i] points to parent of i. If id[i] == i then i is a root node
        # at the beginning every element is its own parent so for every i, i == id[i]
        self._id = [i for i in range(size)]

        # Tracks the number of components in the disjointset
        self._numComponents = size
    
    # Returns the number of all the elements in the disjoinset/unionfind
    def __len__(self) -> int:
        return self._size

    # Find which set/component 'p' belongs to, and compress paths along the way if necessary
    # TC: O(1) amortized
    def find(self, p: int) -> int:
        root = p
        while root != self._id[root]:
            root = self._id[root]
        
        # Compress the path leading back to the root.
        # This operation is called "path compression".
        # This is what gives us amortized time complexity.
        while p != root:
            nextNode = self._id[p]
            self._id[p] = root
            p = nextNode
        return root

    # Recursive alternative for the find method
    # def find(self, p: int) -> int:
    #     if p == self._id[p]: return p
    #     self._id[p] = self.find(self._id[p])
    #     return self._id[p]
    
    # whether elements 'p' and 'q' are in the same
    # set/component
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    # Returns the number of elements in the component/set that 'p' belongs to
    def componentSize(self, p: int) -> bool:
        return self._componentSizes[self.find(p)]

    # Returns the number of remaining sets/components
    def numComponents(self) -> int:
        return self._numComponents

    # Unify the sets/components containing elements 'p' and 'q'
    def unify(self, p: int, q: int) -> None:
        root1 = self.find(p)
        root2 = self.find(q)

        # No need to unify as 'p' and 'q' are already in the same set/component
        if root1 == root2: return

        # Merge smaller component into the larger one
        if self._componentSizes[root1] > self._componentSizes[root2]:
            self._componentSizes[root1] += self._componentSizes[root2]
            self._componentSizes[root2] = 0
            self._id[root2] = root1
        else:
            self._componentSizes[root2] += self._componentSizes[root1]
            self._componentSizes[root1] = 0
            self._id[root1] = root2
        
        self._numComponents -= 1


    
    