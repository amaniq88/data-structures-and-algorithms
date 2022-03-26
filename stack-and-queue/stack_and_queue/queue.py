class Node :
    def __init__(self,value):
        self.value = value 
        self.next = None


class Queue:

    def __init__(self):
        self.front  = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.front:
            self.rear = node
            self.front = node

        else:
            self.rear.next = node 
            self.rear = node 
    
    def dequeue(self):
        if (self.front == None):
            raise Exception("Queue is empty")
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value


    def isImpty(self):
        return self.front == None


    def peek(self):
        if (self.front == None):
            raise Exception("Queue is empty")
        else:
            return self.front.value