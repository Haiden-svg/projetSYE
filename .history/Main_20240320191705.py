import networkx as nx
import matplotlib.pyplot as plt
from Graphics import Graphics
from Task import *
from Tasksystem import *
class Main:
    t1 = Task("t1", ["e"], ["x"])
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], ["a"])
    t4 = Task("t4", ["y"], ["z"])
    ts = Tasksystem([t1, t2, t3, t4], {"t1": [], "t2": [t1], "t3": [t2], "t4": [t3,t2,t1]})
    # Create a directed graph from the tasksystem
    G = nx.DiGraph()

    # Add nodes to the graph
    for task in ts.tasks:
        G.add_node(task.name)

    # Add edges to the graph
    
    for task in ts.tasks:
        for dictionary_name in ts.dictionary:
            G.add_edge(dictionary_name, task.name)
    # Draw the graph
    print(dictionary_name[2])
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')

    

    # Show the graph
    plt.show()