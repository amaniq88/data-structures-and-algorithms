import pytest
from stack_and_queue.queue import Queue , Node


def test_enqueue(QueueTest):
    actual1 = QueueTest.front.value
    expected1 = "A"
    assert actual1 == expected1
    actual2 = QueueTest.rear.value
    expected2 = "C"
    assert actual2 == expected2




def test_dequeue(QueueTest):
    actual = QueueTest.dequeue()
    expected = "A"
    assert actual == expected 
    actual1 = QueueTest.front.value
    expected1 = "B"
    assert actual1 == expected1


def test_dequeue_empty(EmptyQueue):
    with pytest.raises(Exception):
        EmptyQueue.dequeue()


def test_dequeue_untillEmpty(QueueTest):
    QueueTest.dequeue()
    QueueTest.dequeue()
    QueueTest.dequeue()

    actual = QueueTest.isImpty()
    expected = True
    assert actual == expected  




def test_peek(QueueTest):
    actual = QueueTest.peek()
    expected = "A"
    assert actual == expected 


def test_peek_empty(EmptyQueue):
    with pytest.raises(Exception):
        EmptyQueue.peek()


def test_IsEmptyF(QueueTest):
    actual = QueueTest.isImpty()
    expected = False
    assert actual == expected 


def test_IsEmptyT(EmptyQueue):
    actual = EmptyQueue.isImpty()
    expected = True
    assert actual == expected 

@pytest.fixture
def QueueTest():
    QueueTest = Queue()
    QueueTest.enqueue("A")
    QueueTest.enqueue("B")
    QueueTest.enqueue("C")
    return QueueTest

@pytest.fixture
def EmptyQueue():
    EmptyQueue = Queue()
    return EmptyQueue


