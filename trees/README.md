# Trees
implemntaion for one of the datastructure Tress  by create a Node , BinaryTree , Binary sreach Tree .
where each node in this datastructure has two pointer to left and right and always the Nodes in the left has values less than the ones in  right 


## Challenge
Create Classes to implement  this datastructure type 
Node Class , value , left right 
Binary tree Class ,  with three 
    Define a method for each of the depth first traversals:
    pre order
    in order
    post order which returns an array of the values, ordered appropriately.
Binary sreach tree Class : which is subclass from Binary tree nd contain the following methods
add , contains

## Approach & Efficiency
space comlexsity = O(1)
Time Complexsity = Olog(n)
 the recurrsion approch been used for all methods in  both classes 


## API
by using the recursion function approch for all methods in the parent and inhereted class keep calling with changing the root each time to the next rootvalue either to left or right  