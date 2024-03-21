from Task import *
from threading import Semaphore, Thread
##############################################
#args: tks: list of tasks, dico: dictionnary of dependencies
class Tasksystem:
    tasks = []
    dico = {}
#constructor#
    def __init__(self, tks, dico):
        self.tasks = tks
        self.dico = dico
##############################################
        # Draw the graph of the task system
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
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', font_weight='bold')
        plt.show()
##############################################
        #get the dependencies of a task
    def getDependecies(self,String):
        return self.dico[String]
##############################################   
        # Run the tasks in the tasksystem sequentially
    def runseq(self):
        x=0
        sem = Semaphore(1)
        effectued = []
        tasks = self.tasks.copy()  # Create a copy of the tasks list
        while x==0:
            for task in tasks:
                dependencies = self.getDependecies(task.name)
                if all(dep in effectued for dep in dependencies) or dependencies == []:
                    sem.acquire()  # Block the semaphore
                    task.run()  # Run the task
                    sem.release()  # Release the semaphore
                    effectued.append(task)
                    tasks.remove(task)  # Remove the task from the tasks list
                else:  
                    continue
                if all(task in effectued for task in self.tasks):
                    x=1
                    break
            if all(task in effectued for task in self.tasks):
                x=1
        for task in effectued:
            print(task.name)
##############################################
    def runsem(self, toeffectue):
        len = toeffectue.__len__()
        sem = Semaphore(len)
        for task in toeffectue:
            sem.acquire()
            Thread(target=task.run(), args=(task,)).start()
            sem.release()
##############################################    
    def run(self):
        x = 0
        sem = Semaphore(3)
        effectued = []
        tasks = self.tasks.copy()  # Create a copy of the tasks list
        while x==0:
            toeffectue = []
            for task in tasks:
                dependencies = self.getDependecies(task.name)
                if all(dep in effectued for dep in dependencies) or dependencies == []:
                    toeffectue.append(task)
            self.runsem(toeffectue)
            for task in toeffectue:
                effectued.append(task)
                tasks.remove(task)  # Remove the task from the tasks list
            if all(task in effectued for task in self.tasks):
                x=1
##############################################            
