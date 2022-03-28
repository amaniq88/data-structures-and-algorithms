import pytest
from stack_queue_pseudo.psedudo import Queue

# test the enqueue method 
def test_enqueue(QueueTest):
    QueueTest.enqueue(5)
    actual = QueueTest.__str__()
    expected = "[20] -> [15] -> [10] -> [5] -> "
    assert actual ==  expected




# test Dequeue method 
def test_dequeue(QueueTest):
    actual = QueueTest.dequeue()
    expected = 20
    assert actual == expected 
    actual1 = QueueTest.dequeue()
    expected1 = 15
    assert actual1 == expected1 



# check the dequque for empty queue
def test_dequeue_empty(EmptyQueue):
    with pytest.raises(Exception):
        EmptyQueue.dequeue()



@pytest.fixture
def QueueTest():
    QueueTest = Queue()
    QueueTest.enqueue(20)
    QueueTest.enqueue(15)
    QueueTest.enqueue(10)
 


    return QueueTest

@pytest.fixture
def EmptyQueue():
    EmptyQueue = Queue()
    return EmptyQueue


