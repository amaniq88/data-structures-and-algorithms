import pytest
from graph.code import *


# Node can be successfully added to the graph
def test_add_node(graph1):
    graph1.add_node("e")
    expected = graph1.get_nodes()
    actual = ['a', 'b', 'c', 'e']
    assert expected == actual


# An edge can be successfully added to the graph
def test_add_edge(graph1):
    a = graph1.add_node("f")
    b = graph1.add_node("w")
    graph1.add_edge(a,b)
    expected = graph1.get_neighbors(a)
    actual = " w w(0) -->"
    assert expected == actual

# A collection of all nodes can be properly retrieved from the graph
def test_retrive_nodes(graph1):
    expected = graph1.get_nodes()
    actual = ['a', 'b', 'c']
    assert expected == actual

# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors(graph1):
    a = graph1.add_node("t")
    b = graph1.add_node("m")
    c = graph1.add_node("n")
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    expected = graph1.get_neighbors(a)
    actual = " m w(0) --> n w(0) -->"
    assert expected == actual

# Neighbors are returned with the weight between nodes included
def test_get_neighbors_weight(graph1):
    a = graph1.add_node("t")
    b = graph1.add_node("m")
    c = graph1.add_node("n")
    graph1.add_edge(a,b , 4)
    graph1.add_edge(a,c, 5)
    expected = graph1.get_neighbors(a)
    actual = " m w(4) --> n w(5) -->"
    assert expected == actual

# The proper size is returned, representing the number of nodes in the graph
def test_size(graph1):
    expected = graph1.size()
    actual = 3
    assert expected == actual


# A graph with only one node and edge can be properly returned
def test_graph_one_node_one_edge():
    graph2 =Graph()
    a = graph2.add_node("t")
    b = graph2.add_node("m")
    graph2.add_edge(a,b)
    expected = graph2.__str__()
    actual = 't -> m -->\nm ->\n'
    assert expected == actual

# An empty graph properly returns null
def test_graph_one_node_one_edge():
    graph3 =Graph()
    expected = graph3.get_nodes()
    actual = None
    assert expected == actual


@pytest.fixture
def graph1():
    graph1 = Graph()
    a= graph1.add_node("a")
    b= graph1.add_node("b")
    c= graph1.add_node("c")
    graph1.add_edge(a, b)
    graph1.add_edge(b, c)
    graph1.add_edge(c, a)
    return graph1