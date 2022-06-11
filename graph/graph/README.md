# Graphs
A graph is a common data structure that consists of a finite set of nodes (or vertices) and a set of edges connecting them


## Challenge
The graph should be represented as an adjacency list, and should include the following methods:
add node
add edge
get nodes
get neighbors
size

## Approach & Efficiency
using two classes Node and Edge to represent the Vertex and its weight 
and save  the vertex in a dectionary and the connected nodes as linked list 

## API
- add node
Add a node to the graph
- add edge
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
- get nodes
Returns all of the nodes in the graph as a collection (set, list, or similar)

-get neighbors
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection

-size
Returns the total number of nodes in the graph