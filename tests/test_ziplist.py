import pytest
from data_structures_and_algorithms.linked_list.Linked_List import LinkedList, Node

# test if the two given linked list is same length
def test_twoLinkedList_SameLength(ll,lll):
    expected = f" 1 -> 5 -> 3 -> 9 -> 2 -> 4 -> NULL"
    actual = LinkedList.ziplists(ll,lll)
    actual = actual.__str__()
    assert expected == actual


# test if the first linked list is longer
def test_firstLonger(list1,lll):
    expected = f" 1 -> 5 -> 3 -> 9 -> 4 -> NULL"
    actual = LinkedList.ziplists(list1,lll)
    actual = actual.__str__()
    assert expected == actual


# test if the scond linked list is longer
def test_scondLonger(ll,list2):
    expected = f" 1 -> 5 -> 3 -> 9 -> 2 -> NULL"
    actual = LinkedList.ziplists(ll,list2)
    actual = actual.__str__()
    assert expected == actual

# Where the input is not linked list 
def test_notValid_Input():
    with pytest.raises(AttributeError):
        LinkedList.ziplists("list1","lll")




@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(Node(1))
    ll.append(Node(3))
    ll.append(Node(2))
    return ll

@pytest.fixture
def lll():
    lll = LinkedList()
    lll.append(Node(5))
    lll.append(Node(9))
    lll.append(Node(4))

    return lll

@pytest.fixture
def list1():
    list1 = LinkedList()
    list1.append(Node(1))
    list1.append(Node(3))

    return list1

@pytest.fixture
def list2():
    list2 = LinkedList()
    list2.append(Node(5))
    list2.append(Node(9))


    return list2


     