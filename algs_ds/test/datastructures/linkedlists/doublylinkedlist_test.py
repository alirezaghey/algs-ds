# Tests for DoublyLinkedList
#
#
# Author: Alireza Ghey

from  algs_ds.datastructures.linkedlists.doublylinkedlist import DoublyLinkedList
import pytest
import random
from typing import List

class Test_DoublyLinkedList:
    LOOPS = 10000
    TEST_SZ = 40
    NUM_NULLS = TEST_SZ // 40
    MAX_RAND_NUM = 250

    def test_emptyList(self):
        l = DoublyLinkedList()
        assert l.isEmpty() == True
        assert len(l) == 0
    
    def test_removeFirstOfEmpty(self):
        l = DoublyLinkedList()
        with pytest.raises(RuntimeError):
            l.removeFirst()
    
    def test_removeLastOfEmpty(self):
        l = DoublyLinkedList()
        with pytest.raises(RuntimeError):
            l.removeLast()
    
    def test_peekFirstOfEmpty(self):
        l = DoublyLinkedList()
        with pytest.raises(RuntimeError):
            l.peekFirst()
    
    def test_peekLastOfEmpty(self):
        l = DoublyLinkedList()
        with pytest.raises(RuntimeError):
            l.peekLast()

    def test_addFirst(self):
        l = DoublyLinkedList()
        l.addFirst(1)
        assert len(l) == 1
        l.addFirst(4)
        assert len(l) == 2

    def test_addLast(self):
        l = DoublyLinkedList()
        l.addLast(3)
        assert len(l) == 1
        l.addLast(8)
        assert len(l) == 2
    
    def test_addAt(self):
        l = DoublyLinkedList()
        # 1 
        l.addAt(0, 1)
        assert len(l) == 1
        # 4 -> 1
        l.addAt(0, 4)
        assert len(l) == 2
        # 4 -> 5 -> 1
        l.addAt(1, 5)
        assert len(l) == 3
        # 4 -> 5 -> 10 -> 1
        l.addAt(2, 10)
        assert len(l) == 4
        # 4 -> 5 -> 10 -> 1 -> 10
        l.addAt(4, 10)
        assert len(l) == 5

        with pytest.raises(ValueError):
            l.addAt(6, 2)

    def test_removeFirst(self):
        l = DoublyLinkedList()
        l.addFirst(4)
        assert l.removeFirst() == 4
        assert len(l) == 0
        l.addLast(10)
        assert l.removeFirst() == 10
        assert len(l) == 0

    def test_removeLast(self):
        l = DoublyLinkedList()
        l.addLast(3)
        assert l.removeLast() == 3
        l.addFirst(6)
        assert l.removeLast() == 6
        assert len(l) == 0

    def test_peekFirst(self):
        l = DoublyLinkedList()
        l.addFirst(4)
        assert l.peekFirst() == 4
        assert l.peekFirst() == 4
        l.removeFirst()
        assert len(l) == 0
        l.addLast(4)
        assert l.peekFirst() == 4
        assert l.peekFirst() == 4


    def test_peekLast(self):
        l = DoublyLinkedList()
        l.addLast(4)
        assert l.peekLast() == 4
        assert l.peekLast() == 4
        l.removeLast()
        assert len(l) == 0
        l.addLast(10)
        assert l.peekLast() == 10
        assert l.peekLast() == 10

    def test_peeking(self):
        l = DoublyLinkedList()
        # 5
        l.addFirst(5)
        assert l.peekFirst() == 5
        assert l.peekLast() == 5

        # 6 -> 5
        l.addFirst(6)
        assert l.peekFirst() == 6
        assert l.peekLast() == 5

        # 7 -> 6 -> 5
        l.addFirst(7)
        assert l.peekFirst() == 7
        assert l.peekLast() == 5

        # 7 -> 6 -> 5 -> 8
        l.addLast(8)
        assert l.peekFirst() == 7
        assert l.peekLast() == 8

        # 7 -> 6 -> 5
        l.removeLast()
        assert l.peekFirst() == 7
        assert l.peekLast() == 5

        # 7 -> 6
        l.removeLast()
        assert l.peekFirst() == 7
        assert l.peekLast() == 6

        # 6
        l.removeFirst()
        assert l.peekFirst() == 6
        assert l.peekLast() == 6


    def test_removing(self):
        def toArr():
            arr = []
            curr = l._head
            while curr:
                arr.append(curr._data)
                curr = curr._next
            return arr
        
        text = "abcdef"
        l = DoublyLinkedList()
        for c in text:
            l.add(c)
        
        assert len(l) == 6
        assert "".join(toArr()) == text

        l.remove("a")
        text = text.replace("a", "")
        assert len(l) == 5
        assert "".join(toArr()) == text

        l.remove("f")
        text = text.replace("f", "")
        assert len(l) == 4
        assert "".join(toArr()) == text

        l.remove("c")      
        text = text.replace("c", "")
        assert len(l) == 3
        assert "".join(toArr()) == text

        l.remove("d")
        text = text.replace("d", "")
        assert len(l) == 2
        assert "".join(toArr()) == text

        l.remove("e")      
        text = text.replace("e", "")
        assert len(l) == 1
        assert "".join(toArr()) == text
        
        l.remove("b")      
        text = text.replace("b", "")
        assert len(l) == 0
        assert "".join(toArr()) == text


# TODO: Implement below funcitons
    def test_removeAt(self):
        l = DoublyLinkedList()

        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)
        l.removeAt(0)
        l.removeAt(2)
        assert l.peekFirst() == 2
        assert l.peekLast() == 3
        l.removeAt(1)
        assert l.peekFirst() == 2
        assert l.peekLast() == 2
        l.removeAt(0)
        assert len(l) == 0

    def test_clear(self):
        l = DoublyLinkedList()

        l.add(22)
        l.add(33)
        l.add(44)
        assert len(l) == 3
        l.clear()
        assert len(l) == 0
        l.add(22)
        l.add(33)
        l.add(44)
        assert len(l) == 3
        l.clear()
        assert len(l) == 0

    def test_randomizedRemoving(self):
        for _ in range(Test_DoublyLinkedList.LOOPS):
            dblActual = DoublyLinkedList()
            arrExpected = []

            randNums = self.genRandList(Test_DoublyLinkedList.TEST_SZ)

            for num in randNums:
                dblActual.add(num)
                arrExpected.append(num)

            random.shuffle(randNums)

            for num in randNums:
                assert dblActual.remove(num) == (num in arrExpected)
                arrExpected.remove(num)

                assert len(dblActual) == len(arrExpected)

                # TODO
                # Test for content to be exactly the same after iterator
                # for DoublyLinkedList has been implemented

            

                
    def test_randomizedRemoveAt(self):
        dblActual = DoublyLinkedList()
        arrExpected = []

        randArr = self.genRandList(Test_DoublyLinkedList.TEST_SZ)

        for num in randArr:
            dblActual.add(num)
            arrExpected.append(num)
        
        for _ in range(len(randArr)):
            removeIdx = random.randrange(0, len(arrExpected))

            assert dblActual.removeAt(removeIdx) == arrExpected[removeIdx]
            arrExpected = arrExpected[:removeIdx] + arrExpected[removeIdx+1:]

            assert len(dblActual) == len(arrExpected)

            # TODO
            # Test for content to be exactly the same after iterator
            # for DoublyLinkedList has been implemented


    def test_randomizedIndexOf(self):
        dblActual = DoublyLinkedList()
        arrExpected = []

        for _ in range(Test_DoublyLinkedList.LOOPS):
            randArr = self.genRandList(Test_DoublyLinkedList.TEST_SZ)

            for num in randArr:
                dblActual.add(num)
                arrExpected.append(num)

            random.shuffle(randArr)

            for num in randArr:
                assert dblActual.indexOf(num) == arrExpected.index(num)
                assert len(dblActual) == len(arrExpected)


                # TODO
                # Test for content to be exactly the same after iterator
                # for DoublyLinkedList has been implemented
                

    def genRandList(self, size: int) -> List[int]:
        arr = []
        for _ in range(size):
            arr.append(random.randint(0, Test_DoublyLinkedList.MAX_RAND_NUM))
        for _ in range(Test_DoublyLinkedList.NUM_NULLS):
            arr.append(None)
        
        random.shuffle(arr)
        return arr

    def genUniqueRandList(self, size: int) -> List[int]:
        arr = [i for i in range(size)]
        for _ in range(Test_DoublyLinkedList.NUM_NULLS):
            arr.append(None)
        
        random.shuffle(arr)
        return arr

    

    

