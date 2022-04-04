class Node :
    '''
    a Node class that has properties for the value stored in the Node, and a pointer to the next node.
    '''
    def __init__(self,value):
        self.value = value 
        self.next = None

class Stack :
    '''
    has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created.
    '''
    def __init__(self, node = None):
        self.top = node 

    
    def push(self, value):
        '''
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance.
        '''
        node = Node(value)
        node.next = self.top
        self.top = node 


    def pop(self):
        '''
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        raise exception when called on empty stack
        '''
        if (self.top == None):
            raise Exception("stack is empty")
        else :
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value


    
    def peek(self):
        '''
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        '''
        if (self.top == None):
            raise Exception("stack is empty")
        else:
            return self.top.value

    
    def IsEmpty(self):
        '''
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.
        '''
        return self.top == None
