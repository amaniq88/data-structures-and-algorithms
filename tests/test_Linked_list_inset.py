import pytest
from data_structures_and_algorithms.linked_list.Linked_List import LinkedList, Node



# Test add a node to the end of the linked list
def test_append_to_the_end(ll):
    expected = f" Amani -> Ali -> 33 -> True -> NULL"
    ll.append(Node(True))
    actual = ll.__str__()
    assert expected == actual

# Test add multiple nodes to the end of a linked list
def test_append_multi(ll):
    expected = f" Amani -> Ali -> 33 -> A -> B -> C -> NULL"
    ll.append(Node("A"))
    ll.append(Node("B"))
    ll.append(Node("C"))
    actual = ll.__str__()
    assert expected == actual

# Test insert a node before a node located i the middle of a linked list
def test_insert_before_middle(ll):
    expected = f" Amani -> Before -> Ali -> 33 -> NULL"
    ll.insert_before("Ali","Before")
    actual = ll.__str__()
    assert expected == actual

# Test insert a node before the first node of a linked list
def test_insert_before_first(ll):
    expected = f" Before -> Amani -> Ali -> 33 -> NULL"
    ll.insert_before("Amani","Before")
    actual = ll.__str__()
    assert expected == actual

# Test insert after a node in the middle of the linked list
def test_insert_After_middle(ll):
    expected = f" Amani -> Ali -> After -> 33 -> NULL"
    ll.insert_after("Ali","After")
    actual = ll.__str__()
    assert expected == actual


# Test insert a node after the last node of the linked list
def test_insert_After_last(ll):
    expected = f" Amani -> Ali -> 33 -> After -> NULL"
    ll.insert_after("33","After")
    actual = ll.__str__()
    assert expected == actual




@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(Node("Amani"))
    ll.append(Node("Ali"))
    ll.append(Node("33"))
    return ll