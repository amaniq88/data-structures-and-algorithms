import pytest
from tree_intersection.tree_intersection import *


# Happy_path
def test_challenge_example(T1,T2):
    expected = [100, 160, 125, 175, 200, 350, 500]
    Actual = printCommon(T1,T2)
    assert expected == Actual


# No Common Values are there 
def test_challenge_example(T1,T2):
    expected = [100, 160, 125, 175, 200, 350, 500]
    Actual = printCommon(T1,T2)
    assert expected == Actual


# Expected Failer
def test_Invalid_Input(T1,T3):
    with pytest.raises(Exception):
        printCommon(T1,T3)


@pytest.fixture
def T3():
    T3 = BinaryTree()
    return T3


@pytest.fixture
def T4():
    node1 = Node(99)
    node2 = Node(19)
    node3 = Node(9)
    node1.left = node2
    node1.right = node3
    
    T4 = BinaryTree()
    T4.root = node1
    return T4

@pytest.fixture
def T2():
    # Tree2
    node1 = Node(42)
    node2 = Node(100)
    node3 = Node(600)
    node4 = Node(15)
    node5 = Node(125)
    node6 = Node(200)
    node7 = Node(350)
    node8 = Node(160)
    node9 = Node(175)
    node10 = Node(4)
    node11 = Node(500)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    node7.left = node10
    node7.right = node11
    T2 = BinaryTree()
    T2.root = node1
    return T2

@pytest.fixture
def T1():
    node1 = Node(150)
    node2 = Node(100)
    node3 = Node(250)
    node4 = Node(75)
    node5 = Node(125)
    node6 = Node(200)
    node7 = Node(350)
    node8 = Node(160)
    node9 = Node(175)
    node10 = Node(300)
    node11 = Node(500)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    node7.left = node10
    node7.right = node11
    T1 = BinaryTree()
    T1.root = node1
    return T1

