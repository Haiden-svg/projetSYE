from Task import *
from Task import *
from Task import *
from threading import Semaphore, Thread
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
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', font_weight='bold')
        plt.show()
    def getDependecies(self,String):
        return self.dico[String]
   
    def runseq(self):
        x=0
        sem = Semaphore(1)
        effectued = []
        while x==0:
            for task in self.tasks:
                dependencies = self.getDependecies(task.name)
                if all(dep in effectued for dep in dependencies) or dependencies == []:
                    sem.acquire()  # Block the semaphore
                    task.run()  # Run the task
                    sem.release()  # Release the semaphore
                    effectued.append(task)
                else:  
                    continue
                if all(task in effectued for task in self.tasks):
                    x=1
                    break
            if all(task in effectued for task in self.tasks):
                x=1
        for task in effectued:
            print(task.name)
    def run(self):
        x=0
        effectued = []
        toeffectue = []
        while x==0:
            for task in self.tasks:
                dependencies = self.getDependecies(task.name)
                if dependencies == []:
                    toeffectue.append(task)

    def runsem(self,toeffectue):
        sem = Semaphore(toeffectue.__len__()) 

    def todosem(self,toeffectue):
        len=toeffectue.__len__()
        sem=Semaphore(len)
        for task in toeffectue:
           Thread(target=run_task, args=(task,)).start()