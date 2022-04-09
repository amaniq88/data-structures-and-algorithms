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
    '''
    Class for defining the depth first traversals methods 
    '''
    def __init__(self):
        self.root = None
        self.output= []

    def preorder(self):
        if (self.root == None):
            raise Exception("you have to spify the root !")
        def _walk(node):
            self.output.append(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return self.output
     

    def inorder(self):
        if (self.root == None):
            raise Exception("you have to spify the root !")
        
        def _walk(node):
            if node.left:
                _walk(node.left)
            self.output.append(node.value)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return(self.output)

    def postorder(self):
        if (self.root == None):
            raise Exception("you have to spify the root !")
        
        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            self.output.append(node.value)
        _walk(self.root)
        return self.output



class BinarySearchTree(BinaryTree):
    '''
    A binary search tree Class  is a binary tree that satisfies the following conditions:
    The left subtree of any node only contains nodes with keys less than the node’s key
    The right subtree of any node only contains nodes with keys greater than the node’s key
    '''

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



    def Contains(self, val):
        '''
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        def _findnode(node,val):
            if node == None:
                return False
            elif node.value == val:
                return True
            elif node.value > val:
                if node.left == None:
                    return False
                else:
                    node = node.left
                    return _findnode(node, val)
            elif node.value < val:
                if node.right == None:
                    return False
                else:
                    node = node.right
                    return _findnode(node,val)
        return _findnode(self.root, val)


if __name__== "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.left = node2
    node1.right = node3
    node2.right = node5
    node2.left = node4
    node3.left = node6


    tree = BinaryTree()
    tree.root = node1
    test = BinarySearchTree()
    # test.root = node1
    test.add(3)
    test.add(4)
    test.add(5)
    test.add(6)
    test.add(1)
    # print("*********preorder************")
    print(test.preorder())
    print(test.Contains(2))
        # print("**********inorder***********")
        # tree.inorder()
        # print("*********postorder************")
        # tree.postorder()

