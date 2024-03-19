import Graphics  
if __name__ == "__main__":
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

        # Create a tree from the graph
        root = 'A'
        tree = graph.create_tree(root)

        # Print the tree
        print(tree)