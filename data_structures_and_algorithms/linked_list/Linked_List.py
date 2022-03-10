from os import curdir
from Node import Node

class LinkedList:
    def __init__(self):
      self.head = None
    

    def __str__(self):
        list = ""
        current = self.head
        list = f'"{ "{self.head}" } ->"'
        while(current):
            list += f'"{ "{current}" } ->"'
            current = current.next
        
            return list


    def insert(self, newElement):
        newNode = Node(newElement) 
        if(self.head == "None"):
            newNode.next = self.head
            self.head = newNode
        else:    
            temp = self.head
            newNode.next = temp.next
            temp.next = newNode  
     
    
    
    def includes(self , value ): 
        current = self.head
        # loop till current not equal to None
        while (current):
            if current.data == value:
                return True # data found
             
            current = current.next
         
        return False # Data Not found

if __name__ == '__main__':
    list = LinkedList()
    list.head("testA")
    print(list)