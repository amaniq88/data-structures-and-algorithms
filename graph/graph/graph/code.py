class Node:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight = 0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def __str__(self):
        output = ''
        for node in self._adjacency_list.keys():
            output+=f'{node.value} ->'

            for edge in self._adjacency_list[node]:
                output+= f' {edge.vertex.value} -->'
            output+= '\n'
        return output

    def add_node(self, value):
        """ method to add a node to the graph   
                Args:   value: the value of the node
                Returns: None
        """
        vertex = Node(value)
        self._adjacency_list[vertex] = []
        return vertex


    def add_edge(self, vertex1, vertex2, weight=0):
        """ method to add an edge to the graph  
                Arguments: 2 nodes to be connected by the edge, weight (optional)
                Returns: nothing
        """

        if not vertex1  in self._adjacency_list.keys():
            raise KeyError('Vertice 1 is not in the Graph')

        if not vertex2 in self._adjacency_list.keys():
            raise KeyError('Vertice  2 is  not in the Graph')

        edge = Edge(vertex2,weight=weight)

        adjacencieslist = self._adjacency_list[vertex1]
        adjacencieslist.append(edge)

    def get_nodes(self):
        """method to return the nodes of the graph  
            Arguments: none
            Returns all of the nodes in the graph as a collection 

        """
        if not self._adjacency_list.keys():
            return None
        nodes = []
        for node in self._adjacency_list.keys():
            nodes.append(node.value)
        return nodes  

    def get_neighbors(self, vertex):
        """method to return the neighbors of a vertex
                Arguments: node
                Returns a collection of edges connected to the given node
                Include the weight of the connection in the returned collection
        """
        if not self._adjacency_list[vertex]:
            return None
        neighbors = ''
        for edge in self._adjacency_list[vertex]:
                neighbors+= f' {edge.vertex.value} w({edge.weight}) -->'
        return neighbors
    
    def size(self):
        """method to return the size of the graph
            Arguments: none
            Returns the total number of nodes in the graph
        """
        return len(self._adjacency_list)






if __name__ == '__main__':
    graph = Graph()
    a= graph.add_node("a")
    b= graph.add_node("b")
    c= graph.add_node("c")
    
    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, a)
    
    print(graph)    
    print(graph.size())
    
    print(graph.get_neighbors(a))
    print(graph.get_neighbors(b))
    print(graph.get_neighbors(c))
    graph.add_node("e")

    print(graph.get_nodes())
    
