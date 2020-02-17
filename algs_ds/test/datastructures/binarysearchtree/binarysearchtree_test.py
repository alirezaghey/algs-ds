# Tests for BinarySearchTree
#
#
# Author: Alireza Ghey
from __future__ import annotations
from typing import Any
from algs_ds.datastructures.binarysearchtree.binarysearchtree import BinarySearchTree, TraversalType
from typing import List
import pytest
import random
from collections import deque

class NotATestTreeNode:
    def __init__(self, data: Any, l: NotATestTreeNode, r: NotATestTreeNode):
        self._data = data
        self._left = l
        self._right = r
    
    @staticmethod
    def add(node: NotATestTreeNode, data: Any):
        if node == None:
            node = NotATestTreeNode(data, None, None)
        else:
            if data < node._data:
                node._left = NotATestTreeNode.add(node._left, data)
            else:
                node._right = NotATestTreeNode.add(node._right, data)
        return node
    
    @staticmethod
    def preOrder(node: NotATestTreeNode, res: List[int]):
        if not node: return

        res.append(node._data)
        NotATestTreeNode.preOrder(node._left, res)
        NotATestTreeNode.preOrder(node._right, res)
    
    @staticmethod
    def inOrder(node: NotATestTreeNode, res: List[int]):
        if not node: return

        NotATestTreeNode.inOrder(node._left, res)
        res.append(node._data)
        NotATestTreeNode.inOrder(node._right, res)

    @staticmethod
    def postOrder(node: NotATestTreeNode, res: List[int]):
        if not node: return

        NotATestTreeNode.postOrder(node._left, res)
        NotATestTreeNode.postOrder(node._right, res)
        res.append(node._data)

    @staticmethod
    def levelOrder(node: NotATestTreeNode, res: List[int]):
        deq = deque([node]) if node else deque()

        while deq:
            curr = deq.popleft()
            res.append(curr._data)

            if curr._left: deq.append(curr._left)
            if curr._right: deq.append(curr._right)
        
        
class Test_BinarySearchTree:
    LOOPS = 100

    def test_isEmpty(self):
        tree = BinarySearchTree()

        assert tree.isEmpty() == True

        tree.add("Hello world!")

        assert tree.isEmpty() == False
    
    def test_len(self):
        tree = BinarySearchTree()

        assert len(tree) == 0

        tree.add("Hello World!")

        assert len(tree) == 1

    def test_height(self):
        tree = BinarySearchTree()
        # Tree should look like:
        #        M
        #      J  S
        #    B   N Z
        #  A

        # No tree
        assert tree.height() == 0

        # Layer One
        tree.add("M")
        assert tree.height() == 1

        # Layer Two
        tree.add("J")
        assert tree.height() == 2
        tree.add("S")
        assert tree.height() == 2

        # Layer Three
        tree.add("B")
        assert tree.height() == 3
        tree.add("N")
        assert tree.height() == 3
        tree.add("Z")
        assert tree.height() == 3

        # Layer 4
        tree.add("A")
        assert tree.height() == 4

    def test_add(self):
        tree = BinarySearchTree()

        # Add element which does not exist
        assert tree.add("A") == True

        # Add duplicated element
        assert tree.add("A") == False

        # Add another element  
        assert tree.add("B") == True


    def test_contains(self):
        tree = BinarySearchTree()

        tree.add('B')
        tree.add('A')
        tree.add('C')

        # Try looking for an element which doesn't exist
        assert tree.contains('D') == False

        # Try looking for an element which exists in the root
        assert tree.contains('B') == True

        # Try looking for an element which exists as the left child of the root
        assert tree.contains('A') == True

        # Try looking for an element which exists as the right child of the root
        assert tree.contains('C') == True
        

    def test_remove(self):
        tree = BinarySearchTree()

        # Trying to remove an element that doesn't exist
        tree.add("A")
        assert len(tree) == 1
        assert tree.remove("B") == False
        assert len(tree) == 1
        assert tree.height() == 1

        # Removing an element that exists
        tree.add("B")
        assert tree.contains("B") == True
        assert len(tree) == 2
        assert tree.height() == 2
        assert tree.remove("B") == True
        assert len(tree) == 1
        assert tree.height() == 1

        # Try removing the root
        assert tree.remove("A") == True
        assert len(tree) == 0
        assert tree.height() == 0

    def test_randomRemove(self):
        for i in range(Test_BinarySearchTree.LOOPS):
            size = i
            tree = BinarySearchTree()
            arr = self._getRandList(size)
            
            for el in arr:
                tree.add(el)
            
            random.shuffle(arr)
            # remove all the elements we place in the tree
            # but with a different order
            for j in range(i):
                assert tree.contains(arr[j]) == True
                assert tree.remove(arr[j]) == True
                assert tree.contains(arr[j]) == False
                assert len(tree) == size - j - 1
            
            assert tree.isEmpty() == True
        
    def _getRandList(self, size:int) -> List[int]:
        arr = [i for i in range(size)]
        random.shuffle(arr)
        return arr

    
    def _validateTreeTraversal(self, travOrder: TraversalType, arr: List[int]) -> bool:
        testTree = None
        tree = BinarySearchTree()

        # Building the trees for test
        for el in arr:
            testTree = NotATestTreeNode.add(testTree, el)
            tree.add(el)
        
        expectedTrav = []
        actualTrav = []

        if travOrder == TraversalType.PreOrder:
            NotATestTreeNode.preOrder(testTree, expectedTrav)
        elif travOrder == TraversalType.InOrder:
            NotATestTreeNode.inOrder(testTree, expectedTrav)
        elif travOrder == TraversalType.PostOrder:
            NotATestTreeNode.postOrder(testTree, expectedTrav)
        elif travOrder == TraversalType.LevelOrder:
            NotATestTreeNode.levelOrder(testTree, expectedTrav)
        
        travIter = tree.traverse(travOrder)
        for el in travIter:
            actualTrav.append(el)
        
        if len(expectedTrav) != len(actualTrav): return False

        for i in range(len(expectedTrav)):
            if expectedTrav[i] != actualTrav[i]:
                return False
        
        return True

    def test_preOrderTraversal(self):
        for i in range(Test_BinarySearchTree.LOOPS):
            arr = self._getRandList(i)
            assert self._validateTreeTraversal(TraversalType.PreOrder, arr) == True

    def test_inOrderTraversal(self):
        for i in range(Test_BinarySearchTree.LOOPS):
            arr = self._getRandList(i)
            assert self._validateTreeTraversal(TraversalType.InOrder, arr) == True

    def test_postOrderTraveral(self):
        for i in range(Test_BinarySearchTree.LOOPS):
            arr = self._getRandList(i)
            assert self._validateTreeTraversal(TraversalType.PostOrder, arr) == True

    def test_levelOrderTraversal(self):
        for i in range(Test_BinarySearchTree.LOOPS):
            arr = self._getRandList(i)
            assert self._validateTreeTraversal(TraversalType.LevelOrder, arr) == True



        