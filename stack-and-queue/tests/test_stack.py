import pytest
from stack_and_queue.stack import Node, Stack

# test push stack 
def test_push(stackTest):
    actual = stackTest.top.value
    expected = 3
    assert actual == expected 

# test pop stack 
def test_pop(stackTest):
    actual = stackTest.pop()
    expected = 3
    assert actual == expected 

# test pop over empty stack 
def test_pop_empty(Emptystack):
    with pytest.raises(Exception):
        Emptystack.pop()

#test the pop untill empty 
def test_pop_untillEmpty(stackTest):
    stackTest.pop()
    stackTest.pop()
    stackTest.pop()

    actual = stackTest.IsEmpty()
    expected = True
    assert actual == expected  



#test the peek 
def test_peek(stackTest):
    actual = stackTest.peek()
    expected = 3
    assert actual == expected 


#test when peek empty stack 
def test_peek_empty(Emptystack):
    with pytest.raises(Exception):
        Emptystack.peek()

# test IS empty function 
def test_IsEmptyF(stackTest):
    actual = stackTest.IsEmpty()
    expected = False
    assert actual == expected 

# test IS empty function 
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


