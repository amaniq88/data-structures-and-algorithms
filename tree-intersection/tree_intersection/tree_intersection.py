class Hashtable(object):
    def __init__(self, size = 1024):
    
        self.size = size
        self.map = [None]*size


    def hash(self, key):
        """
        - ascii code of a key summation
        - encode chars in key into oct and add it to ascii sum
        - Prime = 19 then multiply it by ascii sum
        - mod the result over self.size
        - return the hashed value
        """
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)
            sum_of_ascii+=ch_ascii
        hashed_key = (sum_of_ascii*19)%self.size

        return hashed_key

    def set(self, key, value):
    # def __setitem__(self, key, value):
        # get index from get_hash
        idx = key
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])


    def contains(self,key):
        '''
        contains
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        '''
        # call the get hash method and send the key to it 
        idx = key
        if (self.map[idx] != None):
            return True
        else:
            return False

    def keys(self):
        '''
        Returns: Collection of keys
        '''
        keysList = []
        for x in range(self.size):
            if (self.map[x] != None):
                for i in range(len(self.map[x])):
                    keysList.append(self.map[x][i][0])
        return keysList
    

    def get(self,key):
        '''
        Arguments: key
        Returns: Value associated with that key in the table
        '''
        if self.contains(key) == False:
            return None
        else:
            v = []
            idx = self.hash(key)
            for i in range(len(self.map[idx])):
                if (key == self.map[idx][i][0]):
                    v.append(self.map[idx][i][1])
            return ','.join(v)


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

        #############################################################################33
        ##############################################################################
        ####################   the Challenge Code #####################################

def printCommon(tree1, tree2):
    '''
    Find common values in 2 binary trees.
    input : Two binary tree
    output : list of the common value 

    '''
    if (tree1.root == None or tree2.root == None):
        raise Exception("There are issues with the trees root !")
    common = []
    hashclass = Hashtable()
    arrtree1 = tree1.inorder()
    for i in arrtree1:
        hashclass.set(i,"1")

    arrtree2 = tree2.inorder()
    for x in arrtree2:
        if (hashclass.contains(x) == True):
            common.append(x)
    if common == []:
        return "No Common Values !"
    return common
	



