# Challenge Summary
Implement a Queue using two Stacks.

## Whiteboard Process
![Challenge 11](/Challenge11.jpg)

## Approach & Efficiency
using two stack instances as one work as the place to save the nodes and the other one for keeping the  node incase to enqueue new node  which O(n) for the enqueue method while its O(1) for dequque

## Solution
1- the dequeue :  raise error if the Queue is empty
2- pop from stack 1 the top element and returm its value
3- for  enqueue check first if the  stack 1 is empty then push the value direct .
4- if not empty move all value from stack 1 to stack 2
5- push the new value to stack1
6-  move the value again from stack2 to stack 1