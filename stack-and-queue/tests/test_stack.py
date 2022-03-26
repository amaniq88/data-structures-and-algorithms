import pytest
from stack_and_queue.stack import Node, Stack


def test_push(stackTest):
    actual = stackTest.top.value
    expected = 3
    assert actual == expected 


def test_pop(stackTest):
    actual = stackTest.pop()
    expected = 3
    assert actual == expected 


def test_pop_empty(Emptystack):
    with pytest.raises(Exception):
        Emptystack.pop()


def test_pop_untillEmpty(stackTest):
    stackTest.pop()
    stackTest.pop()
    stackTest.pop()

    actual = stackTest.IsEmpty()
    expected = True
    assert actual == expected  




def test_peek(stackTest):
    actual = stackTest.peek()
    expected = 3
    assert actual == expected 


def test_peek_empty(Emptystack):
    with pytest.raises(Exception):
        Emptystack.peek()


def test_IsEmptyF(stackTest):
    actual = stackTest.IsEmpty()
    expected = False
    assert actual == expected 


def test_IsEmptyT(Emptystack):
    actual = Emptystack.IsEmpty()
    expected = True
    assert actual == expected 

@pytest.fixture
def stackTest():
    stackTest = Stack()
    stackTest.push(1)
    stackTest.push(2)
    stackTest.push(3)
    return stackTest

@pytest.fixture
def Emptystack():
    Emptystack = Stack()
    return Emptystack


