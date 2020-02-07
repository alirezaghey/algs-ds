# Tests for DisjointSet
#
#
# Author: Alireza Ghey

from algs_ds.datastructures.disjointset.disjointset import DisjointSet
import pytest

class Test_DisjointSet:
    def test_numComponents(self):
        ds = DisjointSet(5)
        assert ds.numComponents() == 5

        ds.unify(0, 1)
        assert ds.numComponents() == 4

        ds.unify(1, 0)
        assert ds.numComponents() == 4

        ds.unify(1, 2)
        assert ds.numComponents() == 3

        ds.unify(0, 2)
        assert ds.numComponents() == 3

        ds.unify(2, 1)
        assert ds.numComponents() == 3

        ds.unify(3, 4)
        assert ds.numComponents() == 2

        ds.unify(4, 3)
        assert ds.numComponents() == 2

        ds.unify(1, 3)
        assert ds.numComponents() == 1

        ds.unify(4, 0)
        assert ds.numComponents() == 1

    def test_componentSize(self):
        ds = DisjointSet(5)

        assert ds.componentSize(0) == 1
        assert ds.componentSize(1) == 1
        assert ds.componentSize(2) == 1
        assert ds.componentSize(3) == 1
        assert ds.componentSize(4) == 1

        ds.unify(0, 1)
        assert ds.componentSize(0) == 2
        assert ds.componentSize(1) == 2
        assert ds.componentSize(2) == 1
        assert ds.componentSize(3) == 1
        assert ds.componentSize(4) == 1

        ds.unify(1, 0)
        assert ds.componentSize(0) == 2
        assert ds.componentSize(1) == 2
        assert ds.componentSize(2) == 1
        assert ds.componentSize(3) == 1
        assert ds.componentSize(4) == 1

        ds.unify(1, 2)
        assert ds.componentSize(0) == 3
        assert ds.componentSize(1) == 3
        assert ds.componentSize(2) == 3
        assert ds.componentSize(3) == 1
        assert ds.componentSize(4) == 1

        ds.unify(0, 2)
        assert ds.componentSize(0) == 3
        assert ds.componentSize(1) == 3
        assert ds.componentSize(2) == 3
        assert ds.componentSize(3) == 1
        assert ds.componentSize(4) == 1

        ds.unify(2, 1)
        assert ds.componentSize(0) == 3
        assert ds.componentSize(1) == 3
        assert ds.componentSize(2) == 3
        assert ds.componentSize(3) == 1
        assert ds.componentSize(4) == 1

        ds.unify(3, 4)
        assert ds.componentSize(0) == 3
        assert ds.componentSize(1) == 3
        assert ds.componentSize(2) == 3
        assert ds.componentSize(3) == 2
        assert ds.componentSize(4) == 2

        ds.unify(4, 3)
        assert ds.componentSize(0) == 3
        assert ds.componentSize(1) == 3
        assert ds.componentSize(2) == 3
        assert ds.componentSize(3) == 2
        assert ds.componentSize(4) == 2

        ds.unify(1, 3)
        assert ds.componentSize(0) == 5
        assert ds.componentSize(1) == 5
        assert ds.componentSize(2) == 5
        assert ds.componentSize(3) == 5
        assert ds.componentSize(4) == 5

        ds.unify(4, 0)
        assert ds.componentSize(0) == 5
        assert ds.componentSize(1) == 5
        assert ds.componentSize(2) == 5
        assert ds.componentSize(3) == 5
        assert ds.componentSize(4) == 5

    def test_connectivity(self):


        size = 7
        ds = DisjointSet(size)
        for i in range(size):
            assert ds.connected(i, i) == True


        ds.unify(0, 2)

        assert ds.connected(0, 2) == True
        assert ds.connected(2, 0) == True

        assert ds.connected(0, 1) == False
        assert ds.connected(3, 1) == False
        assert ds.connected(6, 4) == False
        assert ds.connected(5, 0) == False

        for i in range(size):
            assert ds.connected(i, i) == True

        ds.unify(3, 1)

        assert ds.connected(0, 2) == True
        assert ds.connected(2, 0) == True
        assert ds.connected(1, 3) == True
        assert ds.connected(3, 1) == True

        assert ds.connected(0, 1) == False
        assert ds.connected(1, 2) == False
        assert ds.connected(2, 3) == False
        assert ds.connected(1, 0) == False
        assert ds.connected(2, 1) == False
        assert ds.connected(3, 2) == False

        assert ds.connected(1, 4) == False
        assert ds.connected(2, 5) == False
        assert ds.connected(3, 6) == False

        for i in range(size):
            assert ds.connected(i, i) == True

        ds.unify(2, 5)
        assert ds.connected(0, 2) == True
        assert ds.connected(2, 0) == True
        assert ds.connected(1, 3) == True
        assert ds.connected(3, 1) == True
        assert ds.connected(0, 5) == True
        assert ds.connected(5, 0) == True
        assert ds.connected(5, 2) == True
        assert ds.connected(2, 5) == True

        assert ds.connected(0, 1) == False
        assert ds.connected(1, 2) == False
        assert ds.connected(2, 3) == False
        assert ds.connected(1, 0) == False
        assert ds.connected(2, 1) == False
        assert ds.connected(3, 2) == False

        assert ds.connected(4, 6) == False
        assert ds.connected(4, 5) == False
        assert ds.connected(1, 6) == False

        for i in range(size):
            ds.connected(i, i) == True

        # Connect everything
        ds.unify(1, 2)
        ds.unify(3, 4)
        ds.unify(4, 6)

        for i in range(size):
            for j in range(size):
                assert ds.connected(i, j) == True

    
    def test_size(self):
        ds = DisjointSet(5)

        assert len(ds) == 5
        ds.unify(0, 1)
        ds.find(3)
        assert len(ds) == 5
        ds.unify(1, 2)
        assert len(ds) == 5
        ds.unify(0, 2)
        ds.find(1)
        assert len(ds) == 5
        ds.unify(2, 1)
        assert len(ds) == 5
        ds.unify(3, 4)
        ds.find(0)
        assert len(ds) == 5
        ds.unify(4, 3)
        ds.find(3)
        assert len(ds) == 5
        ds.unify(1, 3)
        assert len(ds) == 5
        ds.find(2)
        ds.unify(4, 0)
        assert len(ds) == 5

    def test_badDisjointSetConstructor(self):
        with pytest.raises(ValueError):
            # This is just to test the constructor for bad values
            # We don't assign it to a variable because the linter
            # would complain. We also have no use for them.
            DisjointSet(0)
        with pytest.raises(ValueError):
            DisjointSet(-1)
        with pytest.raises(ValueError):
            DisjointSet(-346)
