import pytest
from stack_queue_animal_shelter.shelter import Cat, Dog, AnimalShelter

# test the enqueue Cat  
def test_enqueue_cat(shelter1):
    shelter1.enqueue("cat")
    actual = shelter1.__str__()
    expected = "['cat'] -> ['cat'] -> ['dog'] -> ['cat'] -> ['cat'] -> "
    assert actual == expected

# test the enqueue dog  
def test_enqueue_dog(shelter1):
    shelter1.enqueue("dog")
    actual = shelter1.__str__()
    expected = "['cat'] -> ['cat'] -> ['dog'] -> ['cat'] -> ['dog'] -> "
    assert actual == expected




#  test Dequeue method 
def test_dequeue_dog(shelter1):
    shelter1.dequeue("dog")
    actual = shelter1.__str__()
    expected = "['cat'] -> ['cat'] -> ['cat'] -> "
    assert actual == expected


#  test Dequeue Cat method 
def test_dequeue_cat(shelter1):
    shelter1.dequeue("cat")
    actual = shelter1.__str__()
    expected = "['cat'] -> ['dog'] -> ['cat'] -> "
    assert actual == expected


# check the dequque for empty queue
def test_dequeue_empty(shelter2):
    with pytest.raises(Exception):
        shelter2.dequeue("cat")

# check the dequque for other element 
def test_dequeue_empty(shelter1):
    actual = shelter1.dequeue("mouse")
    expected = None
    assert actual == expected



@pytest.fixture
def shelter1():
    shelter1 = AnimalShelter()
    shelter1.enqueue("cat")
    shelter1.enqueue("cat")
    shelter1.enqueue("dog")
    shelter1.enqueue("cat")
    return shelter1

@pytest.fixture
def shelter2():
    shelter2 = AnimalShelter()
    return shelter2


