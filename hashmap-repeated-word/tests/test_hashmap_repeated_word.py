from hashmap_repeated_word.hashmap import Hashtable
import pytest


# Test Case 1 
def test_case_1(hashtable):
    expected = "a" 
    actual = hashtable.firstRepeat("Once upon a time, there was a brave princess who...")
    assert expected == actual


# Test Case 2
def test_case_2(hashtable):
    expected = "it"
    actual = hashtable.firstRepeat("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    assert expected == actual



# Test Case 3
def test_case_3(hashtable):
    expected = "summer"
    actual = hashtable.firstRepeat("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")


# Test Case 4
def test_case_4(hashtable):
    expected = "No Repated Words"
    actual = hashtable.firstRepeat("It was a queer as doing in New York...")



@pytest.fixture
def hashtable():
    hashtable = Hashtable()
    return hashtable