# Tests for HashTableSeparateChaining
#
#
# Author: Alireza Ghey
from algs_ds.datastructures.hashtable.hashtable_separatechaining import HashtableSeparateChaining
import pytest

class Test_HashTableSeparateChaining:

    def test_null_key(self):
        hp = HashtableSeparateChaining()

        with pytest.raises(ValueError):
            hp.put(None, 12)
    
    def test_illegal_creation(self):
        # This is just to test the constructor for bad values
        # We don't assign it to a variable because the linter
        # would complain. We also have no use for them.

        with pytest.raises(ValueError):
            HashtableSeparateChaining(-1)
        
        with pytest.raises(ValueError):
            HashtableSeparateChaining(10, -0.5)
        
        with pytest.raises(ValueError):
            HashtableSeparateChaining(-3, 0.5)

        with pytest.raises(ValueError):
            HashtableSeparateChaining(10, 1)

    def test_legal_creation(self):
        HashtableSeparateChaining(1, 0.5)

        HashtableSeparateChaining(10, 0.75)
    
    def test_adding_key_value_pairs(self):
        hp = HashtableSeparateChaining()

        hp.add(1, 1)
        assert hp.get(1) == 1

        hp.add(5, 4)
        assert hp.get(5) == 4

        hp.add(20, 35)
        assert hp.get(20) == 35


    def test_len_hashtable(self):
        hp = HashtableSeparateChaining()
        assert len(hp) == 0

        hp.add(1, 1)
        assert hp.get(1) == 1
        assert len(hp) == 1

        hp.add(5, 4)
        assert hp.get(5) == 4
        assert len(hp) == 2

        hp.add(23, 35)
        assert hp.get(23) == 35
        assert len(hp) == 3


    def test_updating_values(self):
        hp = HashtableSeparateChaining()

        hp.add(3, 4)
        assert hp.get(3) == 4
        assert len(hp) == 1

        hp.add(3, 10)
        assert hp.get(3) == 10
        assert len(hp) == 1

        hp.add(3, 32)
        assert hp.get(3) == 32
        assert len(hp) == 1

        hp.add(3, -23)
        assert hp.get(3) == -23
        assert len(hp) == 1

