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



    def find_maximum_value(self):
        '''
        Find the Maximum Value in a Binary Tree
        where input is None 
        output the max number 
        '''
        if (self.root == None):
            raise Exception("Empty Tree !")

        def _findMax(node):
            # Base case
            if (node == None):
                return float('-inf')

            maxval = node.value
            leftmax = _findMax(node.left)
            rightmax = _findMax(node.right)
            if (leftmax > maxval):
                maxval = leftmax
            if (rightmax > maxval):
                maxval = rightmax
            return maxval

        return _findMax(self.root)