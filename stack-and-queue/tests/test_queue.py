import pytest
from stack_and_queue.queue import Queue , Node

# test the enqueue method 
def test_enqueue(QueueTest):
    actual1 = QueueTest.front.value
    expected1 = "A"
    assert actual1 == expected1
    actual2 = QueueTest.rear.value
    expected2 = "C"
    assert actual2 == expected2



# test Dequeue method 
def test_dequeue(QueueTest):
    actual = QueueTest.dequeue()
    expected = "A"
    assert actual == expected 
    actual1 = QueueTest.front.value
    expected1 = "B"
    assert actual1 == expected1



# check the dequque for empty queue
def test_dequeue_empty(EmptyQueue):
    with pytest.raises(Exception):
        EmptyQueue.dequeue()


# test keep dequeue untill empty the queue 
def test_dequeue_untillEmpty(QueueTest):
    QueueTest.dequeue()
    QueueTest.dequeue()
    QueueTest.dequeue()

    actual = QueueTest.isImpty()
    expected = True
    assert actual == expected  



# test method peek 
def test_peek(QueueTest):
    actual = QueueTest.peek()
    expected = "A"
    assert actual == expected 


# test the peek method for empty queue
def test_peek_empty(EmptyQueue):
    with pytest.raises(Exception):
        EmptyQueue.peek()


# test Is empty method 
def test_IsEmptyF(QueueTest):
    actual = QueueTest.isImpty()
    expected = False
    assert actual == expected 

# test Is empty method 
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


