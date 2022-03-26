class Node :
    def __init__(self,value):
        self.value = value 
        self.next = None

class Stack :
    def __init__(self, node = None):
        self.top = node 

    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node 


    def pop(self):
        if (self.top == None):
            raise Exception("stack is empty")
        else :
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value


    
    def peek(self):
        if (self.top == None):
            raise Exception("stack is empty")
        else:
            return self.top.value

    
    def IsEmpty(self):
        return self.top == None
