from __future__ import annotations
from collections import deque
from typing import Any
from typing import Iterator
# A BST implementation
#
#
# Author: Alireza Ghey

# Private Node class for internal use
class _Node:
    def __init__(self, data: Any, left:Node=None, right:Node=None):
        self._data = data
        self._left = left
        self._right = right

# Enumerator class to define the type of traversal
class TraversalType:
    mapping = {0: "PreOrder", 1: "InOrder", 2: "PostOrder", 3: "LevelOrder"}
    PreOrder = 0
    InOrder = 1
    PostOrder = 2
    LevelOrder = 3

    # Static method to print out TraversalType for debugging purposes
    @staticmethod
    def toString(travType: TraversalType):
        return TraversalType.mapping[travType]


class BinarySearchTree:
    def __init__(self):
        # Tracks the number of nodes in this BST
        self._nodeCount = 0

        # Tracks the root of the BST
        self._root = None
    
    # Check if BST is empty
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    # Get the number of nodes in this BST
    def __len__(self) -> int:
        return self._nodeCount
    
    # Adds a node to the BST
    # Returns true if successful
    # TC: O(log n)
    def add(self, data: Any) -> bool:
        # Checks if value exists in BST
        # If it exists, ignore adding it
        if self.contains(data):
            return False
        
        # Otherwise add element to the BST
        self._root = self._add(self._root, data)
        self._nodeCount += 1
        return True
    
    # Private method to recursively add an element to the BST
    # TC: O(log n)
    def _add(self, node: _Node, data: Any) -> _Node:
        # Base case: Found a leaf node
        if not node:
            node = _Node(data)
            return node
        
        if data < node._data:
            node._left = self._add(node._left, data)
        else:
            node._right = self._add(node._right, data)
        
        return node
    
    # Removes a node from BST if exists
    # Returns true if successful
    # TC: O(log n) if the BST is skewed, it degenerates to O(n)
    def remove(self, data: Any) -> bool:
        # Make sure the node we want to remove exists
        if not self.contains(data):
            return False
        
        self._root = self._remove(self._root, data)
        self._nodeCount -= 1
        return True
        
    # Private method to recursively remove an element from the BST
    # TC: O(log n) if the BST is skewed, it degenerates to O(n)
    def _remove(self, node: _Node, data: Any) -> _Node:
        if not node: return None

        # Dig into the left subtree if data is smaller than current node
        if data < node._data:
            node._left = self._remove(node._left, data)
        
        # Dig into the right subtree if data is greater than current node
        elif data > node._data:
            node._right = self._remove(node._right, data)
        
        # Found the node we wish to remove
        else:
            # First case:
            # node to be removed has only a right subtree
            # or no subtrees at all.
            # Swap the node to be removed with its right child
            if node._left == None:
                rightChild = node._right
                
                node._data = None
                node = None

                return rightChild
            
            # Second case:
            # node to be removed has only a left subtree
            # Swap the node to be removed with its left child
            elif node._right == None:
                leftChild = node._left

                node._data = None
                node = None

                return leftChild

            # When removing a node which has both subtrees
            # the successor of the node being removed can either be
            # the largest node on the left subtree or the
            # smallest node on the right subtree
            # This implementation takes the smallest node on the right subtree
            else:
                # Find the leftmost node in the right subtree
                temp = self._findMin(node._right)

                # Swap the data
                node._data = temp._data

                # Go into the right subtree and remove the leftmost node
                # that we found and swapped data with.
                # Prevents the BST from having two nodes with the same data
                node._right = self._remove(node._right, temp._data)
        return node

        
    # Private method to find the leftmost node
    # TC: O(log n) deteriorates to O(n) in case the BST is left skewed
    def _findMin(self, node: _Node) -> _Node:
        while node._left != None:
            node = node._left
        return node
    
    # Private method to find the rightmost node
    # TC: O(log n) deteriorates to O(n) if the BST is right skewed
    def _findMax(self, node: _Node) -> _Node:
        while node._right != None:
            node = node._right
        return node

    # Returns true if the element is present in the BST
    # TC: O(log n) deteriorates to O(n) if BST is skewed
    def contains(self, data: Any) -> bool:
        return self._contains(self._root, data)

    # Private method to recursively find element in the tree
    # TC: O(log n) deteriorates to O(n) if BST is skewed
    def _contains(self, node: _Node, data: Any) -> bool:
        # Base case: reached bottom, value not found
        if node == None: return False

        # Dig left because the value we are seeking
        # is less than the current value
        if data < node._data:
            return self._contains(node._left, data)
        
        # Dig right because the value we are seeking
        # is greater than the current value
        elif data > node._data:
            return self._contains(node._right, data)
        
        # Found the value we are looking for
        else:
            return True

    # Computes the height of the BST
    # TC: O(n)
    def height(self) -> int:
        return self._height(self._root)
    
    # Private method to recursively compute the BST height
    # TC: O(n)
    def _height(self, node: _Node) -> int:
        if node == None: return 0
        return max(self._height(node._left), self._height(node._right)) + 1

    # Returns an iterator for a given TraversalType
    # preOrder, inOrder, postOrder, levelOrder
    def traverse(self, travType: TraversalType) -> Iterator:
        if travType == TraversalType.PreOrder:
            return self._preOrder()
        elif travType == TraversalType.InOrder:
            return self._inOrder()
        elif travType == TraversalType.PostOrder:
            return self._postOrder()
        elif travType == TraversalType.LevelOrder:
            return self._levelOrder()
        else:
            raise ValueError("Uknown traversal type")
    
    # Returns an iterator to traverse the tree in pre order
    def _preOrder(self) -> Iterator:
        stack = [self._root] if self._root else []

        while stack:
            node = stack.pop()
            if node._right: stack.append(node._right)
            if node._left: stack.append(node._left)
            yield node._data


    # Returns an iterator to traverse the tree in order
    def _inOrder(self) -> Iterator:
        stack = [self._root]
        trav: _Node = self._root

        while trav and stack:
            # Dig left
            while trav and trav._left:
                stack.append(trav._left)
                trav = trav._left
            
            node: _Node = stack.pop()

            # Try moving right once
            if node._right:
                stack.append(node._right)
                trav = node._right
            
            yield node._data
        

    # Returns an iterator to traverse the tree post order
    def _postOrder(self) -> Iterator:
        stack1 = [self._root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)
                if node._left: stack1.append(node._left)
                if node._right: stack1.append(node._right)
        while stack2:
            yield stack2.pop()._data
        


    def _levelOrder(self) -> Iterator:
        deq = deque([self._root]) if self._root else deque()
        
        while deq:
            node = deq.popleft()
            
            yield node._data

            if node._left: deq.append(node._left)
            if node._right: deq.append(node._right)