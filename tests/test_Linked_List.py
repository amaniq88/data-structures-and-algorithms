import pytest
from data_structures_and_algorithms.linked_list.Linked_List import LinkedList, Node

# Test empty linked list
def test_is_empty_ll():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


# Test appendig 3 values
def test_appended_3_values(ll):
    expected = f" Amani -> Ali -> 33 -> NULL"
    actual = ll.__str__()
    assert expected == actual
# Test add to an existing linked list


def test_add_to_existing_ll(ll):
    expected = f" Amani -> Ali -> 33 -> True -> NULL"
    ll.append(Node(True))
    actual = ll.__str__()
    assert expected == actual

# Test insert method linked list

def test_add_insert(ll):
    expected = f" test -> Amani -> Ali -> 33 -> NULL"
    ll.insert("test")
    actual = ll.__str__()
    assert expected == actual

# Test include (True ) method linked list

def test_includesT(ll):
    expected = True
    actual = ll.includes("Amani")
    assert expected == actual

# Test include (False ) method linked list

def test_includesF(ll):
    expected = False
    actual = ll.includes("Ahmed")
    assert expected == actual


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(Node("Amani"))
    ll.append(Node("Ali"))
    ll.append(Node("33"))
    return ll