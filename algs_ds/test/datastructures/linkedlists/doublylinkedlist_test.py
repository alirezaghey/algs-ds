# Tests for DoublyLinkedList
#
#
# Author: Alireza Ghey

from  algs_ds.datastructures.linkedlists.doublylinkedlist import DoublyLinkedList
import pytest

class Test_DoublyLinkedList:

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
        pass

    def test_clear(self):
        pass

    def test_randomizedRemoving(self):
        pass

    def test_randomizedRemoveAt(self):
        pass

    def test_randomizedIndexOf(self):
        pass

    def genRandList(self):
        pass


    

    

