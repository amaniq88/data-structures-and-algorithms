

from asyncio import gather
from hashlib import new
from locale import currency
from os import link
from platform import node
from re import A
from signal import raise_signal
from tkinter.messagebox import NO
from typing_extensions import Self


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
            while (current.nextval is not None):
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
                    self.append(newNode)
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
        previous_data = ""

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

    def kthFromEnd(self,k):
        '''
        method to find 
        k-th value from the end of a linked list.
        argument: a number, k, as a parameter.
        Return the node’s value that is k places from the tail of the linked list.
        '''
        # check if the value k is negative then rais error 
        if (k < 0):
            raise ValueError("Enter Positive number only")
            
        else:
            arrlinked = []
            current = self.head
            while (current):
                arrlinked.append(current.dataval)
                current = current.nextval
            if(k < len(arrlinked)):
                    valueFromEnd = arrlinked[len(arrlinked) - k -1]
                    return valueFromEnd
            else:  # incase the value k larger than the length of linked list rais exeption 
                raise Exception("the Number is greater than the length of linked list")


    @staticmethod
    def ziplists(linkList1, linkList2):
        '''
        method ziplist which will zip two given linked list and merge them in a certin format
        input : Two linked list 
        output : merged linked List
        '''
        try:
            current1 = linkList1.head
            current2 = linkList2.head
        except AttributeError:
            raise AttributeError

        while(current1 != None  and current2 != None):
            nextL1 = current1.nextval
            datasave = current2
            nextL2 = current2.nextval
            linkList1.insert_after(current1.dataval ,current2.dataval)
            current1 = nextL1
            current2 = nextL2 
        if (current2 != None):
            while(current2 != None):
                linkList1.insert_after(datasave.dataval ,current2.dataval)
                datasave = current2
                current2 = current2.nextval
        return linkList1
     
        
    
                
if __name__ == '__main__':
        link1 = LinkedList()
        a = 2
        b = 3
        c = 1
        link1.append(Node(a))
        link1.append(Node(b))
        link1.append(Node(c))

        print(link1)

        link2 = LinkedList()
        e= 4
        f = 9
        g= 5
        link2.append(Node(e))
        link2.append(Node(f))
        link2.append(Node(g))

        print(link2)
    

        print(LinkedList.ziplists(link1,link2)) 
    
   
  
    
