###################################################################################
##########################   classes used to create the tree instance #############
###################################################################################

from platform import node


class Node :
    '''
    Define Node in Trees which has two pointer to the left and to the right 
    and the value of the Node
    '''
    def __init__(self , value):
        self.value = value 
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.output= []


class BinarySearchTree(BinaryTree):
    def add(self,val):
        '''
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        '''
        def _addnode(node,val):
            if node == None:
                self.root = Node(val)
            elif node.value == val:
                raise Exception("Duplicate not allowed!")   
            elif node.value > val:
                if node.left == None:
                    node.left = Node(val)
                else:
                    node = node.left
                    _addnode(node, val)
            elif node.value < val:
                if node.right == None:
                    node.right = Node(val)
                else:
                    node = node.right
                    _addnode(node,val)

        _addnode(self.root, val)

################################ Challenge 17 ##########################################
#############################  newly added functions ###################################
########################################################################################
def breadthFirst(tree):
    '''
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered
    '''
    if tree.root == None:
        return None
    levelout = []   
    h = height(tree.root)
    for i in range(1, h+1):
       output = printCurrentLevel(tree.root, i , levelout)
    return output




def printCurrentLevel(root, level , levelout):
    '''
    helper function used to count the nodes for each level 
    input : the root of the tree
    output : return the  counts for the current level 
    '''
    if root is None:
        return
    if level == 1:
        levelout.append(root.value)
    elif level > 1:
        printCurrentLevel(root.left, level-1 , levelout)
        printCurrentLevel(root.right, level-1 , levelout)
    return levelout


def height(node):
    '''
    function used to find the height for the tree
    input : node 
    output : length of the tree
    '''
    if node == None:
        return 0
    else:
        lefth = height(node.left)
        righth = height(node.right)

		# take the longest path 
        if lefth > righth:
            return lefth+1
        else:
            return righth+1



