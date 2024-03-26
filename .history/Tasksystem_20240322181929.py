from Task import *
from threading import Semaphore, Thread
import networkx as nx
import matplotlib.pyplot as plt
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
    #def getDependecies(self,String):
     #   return self.dico[String]
    def getDependencies(self):
        dependencies = {task: [] for task in self.tasks}
        for task in self.tasks:
            for task2 in self.tasks:
                if task == task2:
                    continue
                if not task.bernstein(task2):
                    dependencies[task].append(task2)
        return dependencies
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
                # Bernstain test
    def bernsteinIntoTasks(self):
        tasks_to_test=self.tasks.copy()
        tasks_passed=[]
        for task in tasks_to_test:
            for task2 in tasks_to_test:
                if task == task2 or task in tasks_passed or task2 in tasks_passed:
                    continue
                if task.bernstein(task2):
                    print("Bernstein passed between",task.name,"and",task2.name)
                else:
                    print("No Bernstein failed between",task.name,"and",task2.name)
            tasks_passed.append(task)        
