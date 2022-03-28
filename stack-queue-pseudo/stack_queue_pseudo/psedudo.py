
from stack_queue_pseudo.stack import Stack , Node

class Queue:
    '''
    utilize 2 Stack instances to create and manage the queue
    '''
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def __str__(self):
        '''
        this method is used to print in certain formate like 
       [a] -> [b] -> [c] -> [d] 
        
        '''
        output = ""
        if self.s1.top is None:
            output = "Empty Queue !"
        else:
            current = self.s1.top
            while(current):
                output+= f'{[current.value]} -> '
                current = current.next
            
        return output



    def enqueue(self, Value):
        '''
        Arguments: value
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        '''
        if (self.s1.top == None):
            self.s1.push(Value)
        else:
            while(self.s1.top != None):
                self.s2.push(self.s1.pop())
            self.s1.push(Value)
            while(self.s2.top != None):
                self.s1.push(self.s2.pop())


    

    def dequeue(self):
        '''
        Arguments: none
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        '''
        if (self.s1.top == None):
            raise Exception("Queue is empty")
        else:
            return self.s1.pop()




if __name__ == '__main__':
    Queue1 = Queue()
    Queue1.enqueue(10)
    Queue1.enqueue(15)
    Queue1.enqueue(20)
    Queue1.enqueue(5)

    print(Queue1)

    print(Queue1.dequeue())
    print(Queue1.dequeue())
    print(Queue1.dequeue())
