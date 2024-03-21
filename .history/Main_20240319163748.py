from networkx import networkx as nx
import matplotlib.pyplot as plt
from Graphics import Graphics

class Main:
    # Create a graph
    graph_dict = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    graph = Graphics(graph_dict)

    # Create a NetworkX graph from the graph_dict
    G = nx.DiGraph(graph_dict)

    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()