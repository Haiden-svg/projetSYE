import networkx as nx
import matplotlib.pyplot as plt
from Graphics import Graphics
from Task import *
from Tasksystem import *

class Main:
    t1 = Task("t1", [], ["x"])
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], [])
    t4 = Task("t4", ["y"], ["z"])
     
    ts = Tasksystem([t1, t2, t3, t4], {"t1": [], "t2": [t1], "t3": [t2], "t4": [t3,t2,t1]})
    # Create a directed graph from the tasksystem
    G = nx.DiGraph()

    # Add nodes to the graph
    for task in ts.tasks:
        G.add_node(task.name)

    # Add edges to the graph
    for task in ts.tasks:
        for dependency in ts.dependencies[task.name]:
            G.add_edge(dependency, task.name)

    # Draw the graph
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')

    # Show the graph
    plt.show()