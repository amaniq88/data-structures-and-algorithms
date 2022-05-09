from tree_fizz_buzz.fizzbuzz import *
import pytest

# Test Happy path
def test_FizzBuzz():
    node6 = Node(9)
    node5 = Node(56)
    node4 = Node(25, [node5, node6])
    node3 = Node(32)
    node2 = Node(27)
    node1 = Node(15, [node2, node3, node4])
    root = node1

    copynode = fizz_buzz_tree(root)
    expected = treeprint(copynode, None)
    actual = ['FizzBuzz', 'Fizz', '32', 'Buzz', '56', 'Fizz']
    assert expected == actual


# Test one node 
def test_FizzBuzz_one_node():
    node1 = Node(5)
    root = node1

    copynode = fizz_buzz_tree(root)
    expected = treeprint(copynode, None)
    actual = ['Buzz']
    assert expected == actual

# Test egde Cases 
def test_FizzBuzz_not_int():
    root = Node("Ali")
    with pytest.raises(Exception):
        fizz_buzz_tree(root)

# Test None Root 
def test_FizzBuzz_empty():
    root = None
    with pytest.raises(Exception):
        fizz_buzz_tree(root)
  