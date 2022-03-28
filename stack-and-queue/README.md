# Stacks and Queues
Implementation: Stacks and Queues and their related methods with their methods and tests files 

## Challenge
implement both a Stack and a Queue by creatin  the following methods and classes  : 
### Class Node : 
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
### Class Stack : 
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:
push
pop
peek
is empty

### Queue
enqueue
dequeue
peek
is empty

## Approach & Efficiency
Space completxty = O(1)
Time Complexsity = O(n)

all methods added direct without use of extra array or recursion functions the while itteration over the value 

## API
### Class Stack : 
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:
push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.
pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack
peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack
is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.
### Queue
a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:
enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.
dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue
peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack
is empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty