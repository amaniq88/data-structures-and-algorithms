from hashtable.hashtable import Hashtable
import pytest


# Setting a key/value to your hashtable results in the value being in the data structure
def test_set_key_value(hashtable):
    expected = "pass"
    hashtable.set("Test2","pass")
    actual = hashtable.get("Test2")
    assert expected == actual

# Retrieving based on a key returns the value stored
def test_Retrive_key_value(hashtable):
    expected = "Rainy"
    actual = hashtable.get("ttt")
    assert expected == actual

# Successfully returns null for a key that does not exist in the hashtable
def test_Retrive_key_Not_having_value(hashtable):
    expected = None
    actual = hashtable.get("nosuchkey")
    assert expected == actual


# Successfully returns a list of all unique keys that exist in the hashtable
def test_return_keys(hashtable):
    expected = ['nest', 'estn', 'ttt', 'cloud']
    actual = hashtable.keys()
    assert expected == actual


# Successfully handle a collision within the hashtable
def test_handle_collision(hashtable):
    hashtable.set("cat","pass1")
    hashtable.set("act","pass2")
    assert hashtable.contains("act") == True
    assert hashtable.contains("cat") == True

# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_retrive_ifcollision(hashtable):
    expected1 = "pass1"
    actual1 = hashtable.get("nest")
    assert expected1 == actual1
    expected2 = "pass2"
    actual2 = hashtable.get("estn")
    assert expected2 == actual2

# Successfully hash a key to an in-range value
def test_hash(hashtable):
    actual = hashtable.hash("code")
    expected = 641
    assert actual == expected



@pytest.fixture
def hashtable():
    hashtable = Hashtable()
    hashtable.set("cloud", "Azure")
    hashtable.set("nest","pass1")
    hashtable.set("estn","pass2")
    hashtable.set("ttt", "Rainy")
    return hashtable
