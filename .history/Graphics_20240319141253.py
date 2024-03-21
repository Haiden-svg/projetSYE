class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict

    def add_edge(self, parent, child):
        if parent not in self.graph_dict:
            self.graph_dict[parent] = []
        self.graph_dict[parent].append(child)

    def create_tree(self, root):
        tree = {}
        tree[root] = self.create_subtree(root)
        return tree

    def create_subtree(self, node):
        subtree = {}
        if node in self.graph_dict:
            children = self.graph_dict[node]
            for child in children:
                subtree[child] = self.create_subtree(child)
        return subtree