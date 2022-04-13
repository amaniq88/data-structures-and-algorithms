import pytest
from tree_breadth_first.trav import *


# traverse corrctly level by level 
def test_happypath_case(tree):
    expected = [2,7,5,2,6,9,5,11,4] 
    actual = breadthFirst(tree)
    assert expected == actual


# test  empty tree
def test_empty_tree(Btreetest):
    expected = None
    actual = breadthFirst(Btreetest)
    assert expected == actual


# traverse corrctly level by level 
def test_happypath_case2(treetest):
    expected = [7, 9, 3, 12, 12]
    actual = breadthFirst(treetest)
    assert expected == actual




@pytest.fixture
def treetest():
    treetest = BinaryTree()
    node1 = Node(7)
    node2 = Node(9)
    node3 = Node(3)
    node4 = Node(12)
    node5 = Node(12)
    # node6 = Node(9)
    # node7 = Node(5)
    # node8 = Node(11)
    # node9 = Node(4)

    node1.left = node2
    node1.right = node3
    node2.right = node5
    node2.left = node4
    # node3.right = node6
    # node5.left = node7
    # node5.right = node8
    # node6.left = node9
    treetest.root = node1
    return treetest

@pytest.fixture
def Btreetest():
    Btreetest = BinaryTree()
    return Btreetest

@pytest.fixture
def tree():
    node1 = Node(2)
    node2 = Node(7)
    node3 = Node(5)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(9)
    node7 = Node(5)
    node8 = Node(11)
    node9 = Node(4)

    node1.left = node2
    node1.right = node3
    node2.right = node5
    node2.left = node4
    node3.right = node6
    node5.left = node7
    node5.right = node8
    node6.left = node9
    tree = BinaryTree()
    tree.root = node1
    return tree