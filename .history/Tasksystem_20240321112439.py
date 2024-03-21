from Task import *
from Task import *
from Task import *
class Tasksystem:
    tasks = []
    dico = {}
    def __init__(self, tks, dico):
        self.tasks = tks
        self.dico = dico
    def draw(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.DiGraph()
        for task in self.tasks:
            G.add_node(task.name)
        for task in self.tasks:
            for t in self.dico[task.name]:
                if t == []:
                    continue    
                G.add_edge(t.name,task.name)
        #G.reverse()
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
        plt.show()
    def getDependecies(self,String):
        return self.dico[String]
   
    def runseq(self):
        sem=Semaphore(0)
        effectued=[]
        for task in self.tasks:

            if self.getDependecies(task.name)in effectued or self.getDependecies(task.name)==[]:
                task.run()
                #print(task.name)
                effectued.append(task)
            else:  
                continue
        for task in effectued:
            print(task.name)