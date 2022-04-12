###################################################################################
##########################   classes used to create the tree instance #############
###################################################################################

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
    h = height(tree.root)
    for i in range(1, h+1):
       output = printCurrentLevel(tree.root, i)
    return output



levelout = []
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        levelout.append(root.value)
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
    return levelout


def height(node):
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




if __name__== "__main__":
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
    print(breadthFirst(tree))