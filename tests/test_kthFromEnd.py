import pytest
from data_structures_and_algorithms.linked_list.Linked_List import LinkedList, Node


# # Where k is greater than the length of the linked list
def test_K_GreaterThanLength(ll):
    with pytest.raises(Exception):
        ll.kthFromEnd(5)


#Where k and the length of the list are the same
def test_K_sameLength(ll):
    with pytest.raises(Exception):
        ll.kthFromEnd(5)


# Where k is not a positive integer
def test_K_negative(ll):
    with pytest.raises(ValueError):
        ll.kthFromEnd(-9)


# Where the linked list is of a size 1
def test_linkedLise_l1(lll):
    actual = "xx"
    expected = lll.kthFromEnd(0)
    assert actual == expected

#  where k is not at the end, but somewhere in the middle of the linked list
def test_k_midlle(ll):
    actual = "bb"
    expected = ll.kthFromEnd(1)
    assert actual == expected

#  additional test
def test_k_head(ll):
    actual = "aa"
    expected = ll.kthFromEnd(2)
    assert actual == expected


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(Node("aa"))
    ll.append(Node("bb"))
    ll.append(Node("cc"))
    return ll

@pytest.fixture
def lll():
    lll = LinkedList()
    lll.append(Node("xx"))
    return lll