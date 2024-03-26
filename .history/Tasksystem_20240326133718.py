from Task import *
from threading import Semaphore, Thread
import networkx as nx
import matplotlib.pyplot as plt
##############################################
#args: tks: list of tasks, dico: dictionnary of dependencies
class Tasksystem:
#constructor#
    def __init__(self, tks, dico):
        self.tasks = tks
        self.dico = dico
##############################################
        # Draw the graph of the task system
    def draw(self):
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
    def getDependeciesTS(self,task):
        return self.dico[task.name]        
    def getDependencie(self,task):
        return 0    
##############################################   
        # Run the tasks in the tasksystem sequentially
    def runseq(self):
        x=0
        sem = Semaphore(1)
        effectued = []
        tasks = self.tasks.copy()  # Create a copy of the tasks list
        while x==0:
            for task in tasks:
                dependencies = self.getDependeciesTS(task)
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
    # Run the tasks in the tasksystem with parallelism but elementary function
    def runsem(self, toeffectue):
        len = toeffectue.__len__()
        sem = Semaphore(len)
        for task in toeffectue:
            sem.acquire()
            Thread(target=task.run(), args=(task,)).start()
            sem.release()
##############################################   
            # Run the tasks in the tasksystem with parallelism 
    def run(self):
        x = 0
        effectued = []
        tasks = self.tasks.copy()  # Create a copy of the tasks list
        while x==0:
            toeffectue = []
            for task in tasks:
                dependencies = self.getDependeciesTS(task)
                if all(dep in effectued for dep in dependencies) or dependencies == []:
                    toeffectue.append(task)
            self.runsem(toeffectue)
            for task in toeffectue:
                effectued.append(task)
                tasks.remove(task)  # Remove the task from the tasks list
            if all(task in effectued for task in self.tasks):
                x=1
##############################################    
                # Bernstain test
 ##############################################   
    def checkdep(self, task):
        readlist = task.reads
        deplist = []
        for task2 in self.tasks:
            if task2.name != task.name:
            
                if any(read in task2.writes for read in task.reads):
                    print("!!!")
                    deplist.append(task2)   
        return deplist  
##############################################
    def createDep(self):
        dep = {}
        for task in self.tasks:
            dep[task.name] = self.checkdep(task)
        return dep
    
    def bernsteinIntoEachOver(self, tasks):
        succed = []
        tasksAlter = tasks.copy()
        taskEffectued = []
        failed = []
        for task in tasksAlter:
            for task2 in (task for task in tasksAlter if task not in taskEffectued):
                if task.name == task2.name:
                    continue
                if task.bernstein(task2):
                    succed.append(task)
                else:
                    failed.append(task) 
            taskEffectued.append(task)
    def getRoad(self):
        