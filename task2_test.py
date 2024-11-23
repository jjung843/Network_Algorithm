import pytest
from module_lab2_task2 import *

# Test for Method 1: add_node
def test_add_node ():
    # Create test1 instances of Network class
    test1 = Network()
    # Add a node
    test1.add_node("Node1", 10)

    assert test1.get_node("Node1").name == "Node1"
    assert test1.get_node("Node1").value == 10

# Test for Method 2: add_arc
def test_add_arc_two_nodes():
    # Create test2 instances of Network class
    test2 = Network()

    # Add the two nodes
    test2.add_node("Node1")
    test2.add_node("Node2")
    node1 = test2.get_node("Node1")
    node2 = test2.get_node("Node2")

    # Add an arc in between the nodes
    test2.add_arc(node1, node2, 2)

    # Check arc attributes with assert conditions
    assert len(test2.arcs) == 1
    assert test2.arcs[0].from_node is node1
    assert test2.arcs[0].to_node is node2
    assert test2.arcs[0].weight == 2

    # Check if the arc has node1 as start node
    assert node1 in [arc.from_node for arc in test2.arcs]
    # Check if the arc has node2 as end node
    assert node2 in [arc.to_node for arc in test2.arcs]
    # Check length of arcs between two nodes
    assert len(node1.arcs_out) == 1
    assert len(node2.arcs_in) == 1

# Test for Method 3: read_network
def test_read_network():
    # Create test3 instances of Network class
    test3 = Network()

    # Read test data text file and form the network
    test3.read_network("network.txt")

    # Check the number of nodes and arcs in the network
    assert len(test3.nodes) == 6
    assert len(test3.arcs) == 9

    # Check each arc information
    arc_AB = test3.arcs[0]
    assert arc_AB.from_node.name == 'A'
    assert arc_AB.to_node.name == 'B'
    assert arc_AB.weight == 2

    arc_AC = test3.arcs[1]
    assert arc_AC.from_node.name == 'A'
    assert arc_AC.to_node.name == 'C'
    assert arc_AC.weight == 4

    arc_BC = test3.arcs[2]
    assert arc_BC.from_node.name == 'B'
    assert arc_BC.to_node.name == 'C'
    assert arc_BC.weight == 1

    arc_BD = test3.arcs[3]
    assert arc_BD.from_node.name == 'B'
    assert arc_BD.to_node.name == 'D'
    assert arc_BD.weight == 4

    arc_CD = test3.arcs[4]
    assert arc_CD.from_node.name == 'C'
    assert arc_CD.to_node.name == 'D'
    assert arc_CD.weight == 2

    arc_CE = test3.arcs[5]
    assert arc_CE.from_node.name == 'C'
    assert arc_CE.to_node.name == 'E'
    assert arc_CE.weight == 1

    arc_DE = test3.arcs[6]
    assert arc_DE.from_node.name == 'D'
    assert arc_DE.to_node.name == 'E'
    assert arc_DE.weight == 2

    arc_DF = test3.arcs[7]
    assert arc_DF.from_node.name == 'D'
    assert arc_DF.to_node.name == 'F'
    assert arc_DF.weight == 2

    arc_EF = test3.arcs[8]
    assert arc_EF.from_node.name == 'E'
    assert arc_EF.to_node.name == 'F'
    assert arc_EF.weight == 3

