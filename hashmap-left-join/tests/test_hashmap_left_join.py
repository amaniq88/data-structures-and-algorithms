from hashmap_left_join.left_join import *
from hashmap_left_join.hashtable import Hashtable
import pytest


# Test Happy path
def test_join(H1,H2):
    expected = [['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    actual = leftjoin(H1,H2)
    assert expected == actual


# test Invlid input
def test_Invalid_Input():
    with pytest.raises(Exception):
        leftjoin(10,H2)

@pytest.fixture
def H1():
    H1 = Hashtable()
    H1.set("diligent", "employed")
    H1.set("fond", "enamored")
    H1.set("guide","usher")
    H1.set("outfit","garb")
    H1.set("wrath", "anger")
    return H1

@pytest.fixture
def H2():
    H2 = Hashtable()
    H2.set("diligent", "idle")
    H2.set("fond", "averse")
    H2.set("guide","follow")
    H2.set("flow","jam")
    H2.set("wrath", "delight")
    return H2

