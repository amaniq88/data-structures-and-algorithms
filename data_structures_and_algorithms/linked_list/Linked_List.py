

from hashlib import new
from platform import node
from re import A
from tkinter.messagebox import NO


class Node:
    '''
    Class Node which define the node value and initial the next to None
    '''
    
    def __init__(self, dataval):  
            self.dataval = dataval
            self.nextval = None
       
        


class LinkedList:
    '''
    Class LinkedList which used to represent the Linked List with initial value of Head to None and it has 
    the following methods : 
    append which Take input Node instancetce and define the head and next 
    insert which insert new element after the head of the node if exsist 
    Includes which check if this elemnt is there or not 
    '''
    def __init__(self):
      self.head = None
   
   
    def append(self, node):
        '''
        append menthod which used to append the new node to the linked list  at the end of the list and keep the last elent is null 
        Input :  Node instance 
        '''
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.nextval is not None:
                current = current.nextval
            current.nextval = node

    def __str__(self):
        '''
        this method is used to print in certain formate like 
        {a} -> {b} -> {c} -> {d} -> NULL
        
        '''
        output = ""
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
            while(current):
                output+= f' {current.dataval} ->'
                current = current.nextval
            
            output+= " NULL"
        return output
    
    
    
    def insert(self, newElement):
        '''
        method to insert new element after the head element 
        input : element to added in the linked list
        '''
        #except NameError:
 

        if(self.head == None):
            newNode = Node(newElement)
            self.append(newNode)
        else:
            newNode = Node(newElement)     
            temp = self.head
            newNode.nextval = temp
            self.head = newNode


    def includes(self , value ): 
        '''
        Arguments: value
        Returns: Boolean
        Indicates whether that value exists as a Node’s value somewhere within the list.
        '''
        current = self.head
        # loop till current not equal to None
        while (current):
            if current.dataval == value:
                return True # data found
             
            current = current.nextval
         
        return False # Data Not found

    def insert_after(self, value, newElement):
        '''
        arguments: value, newElement
        adds a new node with the given new value immediately after the first node that has the value specified
        '''
        current = self.head
        if (self.includes(value) == False):
            print("sorry the Node not on the linked list ")
        while (current):
            if current.dataval == value:
                newNode = Node(newElement)
                if (current.nextval == None ):
                    current.nextval = newNode
                    newNode.nextval = None
                    print(newNode.nextval)
                else:
                    temp = current.nextval     
                    current.nextval = newNode
                    newNode.nextval = temp
                break
            current = current.nextval

    def insert_before(self, value, newElement):
        '''
        arguments: value, newElement
        adds a new node with the given new value immediately before the first node that has the value specified
        '''
        current = self.head
        if (self.includes(value) == False):
            print("sorry the Node not on the linked list ")
        while (current):
            if current.dataval == value:
                if ( current.dataval == self.head.dataval):
                    self.insert(newElement)
                else:
                    newNode = Node(newElement) 
                    previous_data.nextval = newNode
                    newNode.nextval = current
                    break
            previous_data = current
            current = current.nextval

    

            
    
                
if __name__ == '__main__':
    a = LinkedList()
  
    
