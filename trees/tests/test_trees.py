from tkinter.messagebox import NO
import pytest
from trees.trees import Node, BinarySearchTree, BinaryTree


# Can successfully instantiate an empty tree
def test_empty_tree():
    tree1 = BinaryTree()
    expected = None
    actual = tree1.root
    assert expected == actual


# Can successfully instantiate a tree with a single root node
def test_tree_single_root(treetest):
    expected = 1
    actual = treetest.root.value
    assert expected == actual


# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_binary_add(Btreetest):
    Btreetest.add(3)
    expected1 = Btreetest.root.left.value
    actual1 = 3
    assert expected1 == actual1
    Btreetest.add(8)
    expected2 = Btreetest.root.right.value
    actual2 = 8
    assert expected2 == actual2




# Can successfully return a collection from a preorder traversal
def test_preorder_tree(B1treetest):
    expected = B1treetest.preorder()
    actual = [4,3,8]
    assert expected == actual

#Can successfully return a collection from an inorder traversal
def test_inorder_tree(B1treetest):
    expected = B1treetest.inorder()
    actual = [3,4,8]
    assert expected == actual


# Can successfully return a collection from a postorder traversal
def test_postorder_tree(B1treetest):
    expected = B1treetest.postorder()
    actual = [3,8,4]
    assert expected == actual

# def Returns true	 contains method, given an existing  node value
def test_Contains_True(B1treetest):
    expected = True
    actual = B1treetest.Contains(3)
    assert expected == actual


# def Returns False	 contains method, given not excesting node value
def test_Contains_False(B1treetest):
    expected = False
    actual = B1treetest.Contains(5)
    assert expected == actual


@pytest.fixture
def treetest():
    treetest = BinaryTree()
    node1 = Node(1)
    treetest.root = node1
    return treetest

@pytest.fixture
def Btreetest():
    Btreetest = BinarySearchTree()
    node1 = Node(5)
    Btreetest.root = node1
    return Btreetest

@pytest.fixture
def B1treetest():
    B1treetest = BinarySearchTree()
    B1treetest.add(4)
    B1treetest.add(3)
    B1treetest.add(8)
    return B1treetest