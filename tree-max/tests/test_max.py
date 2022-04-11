import pytest
from tree_max.max import Node, BinaryTree


# test find max in happy path case 
def test_find_max(B2treetest):
  assert B2treetest.find_maximum_value() == 18

#test max at root 
def test_max_atRoot(B1treetest):
  assert B1treetest.find_maximum_value() == 23

# test max if n root or empty tree
def test_find_max_root_no_root():
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.find_maximum_value()


@pytest.fixture
def B1treetest():
    B1treetest = BinaryTree()
    B1treetest.root = Node(23)
    B1treetest.root.left = Node(18)
    B1treetest.root.right = Node(6)
    B1treetest.root.left.left = Node(4)
    B1treetest.root.left.right = Node(9)
    return B1treetest

@pytest.fixture
def B2treetest():
    B2treetest = BinaryTree()
    B2treetest.root = Node(6)
    B2treetest.root.left = Node(18)
    B2treetest.root.right = Node(9)
    B2treetest.root.left.left = Node(4)
    B2treetest.root.left.right = Node(9)
    return B2treetest