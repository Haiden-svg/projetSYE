from Task import *
from threading import Semaphore, Thread
import networkx as nx
import matplotlib.pyplot as plt
import time
##############################################
#args: tks: list of tasks, dico: dictionnary of dependencies
class Tasksystem:
#constructor#
    def __init__(self, tks, dico):
        self.tasks = tks
        self.dico = dico
        self.verify_unique_task_names()
        self.verify_task_existence_in_dependencies()
##############################################
        #Verification des noms des tâches dupliqués
    def verify_unique_task_names(self):
        task_names = [task.name for task in self.tasks]
        if len(task_names) != len(set(task_names)):
            raise ValueError("Error: Task names must be unique.")
##############################################
        #Verification de l'existence des noms de tâches dans le dictionnaire de précédence
    def verify_task_existence_in_dependencies(self):
        task_names = set(task.name for task in self.tasks)
        for task_name, deps in self.dico.items():  # Parcourir les éléments du dictionnaire
            if task_name not in task_names:
                raise ValueError(f"Erreur : La tâche '{task_name}' mentionnée dans les dépendances n'existe pas.")
            for dep in deps:
                if dep not in task_names:
                    raise ValueError(f"Erreur : La tâche dépendante '{dep}' de '{task_name}' n'existe pas dans la liste des tâches.")
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
        dependances = [[]]
        x = 0
        for road in self.runRoad():
            dependances.append([])
            dependances[x].extend(road)
            x+=1

            if task in road:
                return road
        return 0   
##############################################   
        # Run the tasks in the tasksystem sequentially
    
    def runseq(self):
        sem = Semaphore(1)
        roads=self.getRoad()
        effectued = []
        for tasks in roads:
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

        tasksII=self.getRoad()
        for road in tasksII:
            self.runsem(road)
###############################################   
    def runRoad(self):
        x = 0
        y= 0
        road = [[]]
        effectued = []
        tasks = self.tasks.copy()  # Create a copy of the tasks list
        while x==0:
            toeffectue = []
            road.append([])  # Add a new empty list for each iteration
            for task in tasks:
                dependencies = self.getDependeciesTS(task)
                if all(dep in effectued for dep in dependencies) or dependencies == []:
                    toeffectue.append(task)
            if self.bernsteinIntoEachOverTest(toeffectue):
                #print("Bernstein test passed")
                road[y].extend(toeffectue)
            #road = self.addToRoad(road, toeffectue, y)
            y+=1
            for task in toeffectue:
                effectued.append(task)
                tasks.remove(task)  # Remove the task from the tasks list
            if all(task in effectued for task in self.tasks):
                x=1
        return road
##############################################    
                # Bernstain test
 ##############################################   
    def checkdep(self, task):
        readlist = task.reads
        deplist = []
        for task2 in self.tasks:
            if task2.name != task.name:
            
                if any(read in task2.writes for read in task.reads):
                    deplist.append(task2)   
        return deplist  
##############################################
    def createDep(self):
        dep = {}
        for task in self.tasks:
            dep[task.name] = self.checkdep(task)
        return dep
##############################################
    # Function to verify bernstein between every task in a list
##############################################    
    def bernsteinIntoEachOverTest(self, tasks):
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
        return succed, failed
    ##############################################
    

    def getRoad(self):
        road = [[]]
        linear = []
        index = self.tasks.__len__()
        for task in self.tasks:
            if self.getDependeciesTS(task) == []:
                road[0].append(task)
                linear.append(task)
                
        for i in range(index):
            road.append([])  # Add a new empty list for each iteration
            for task in self.tasks:
                if all(dep in linear for dep in self.getDependeciesTS(task)):
                    road[i+1].append(task)
                    linear.append(task)
        return road
    

##############################################
        # Cout du parallelisme
    
    def parCost(self, runs=10):
        # Mesurer le temps d'exécution séquentiel
        count = 0
        seq_times = []
        while count < runs:
            start = time.time()
            self.runseq()  # Exécution séquentielle
            end = time.time()
            seq_times.append(end - start)  # Enregistrement du temps d'exécution
            count += 1  # Incrémentation du compteur

        # Mesurer le temps d'exécution parallèle
        count = 0
        par_times = []
        while count < runs:
            start = time.time()
            self.run()
            end = time.time()
            par_times.append(end - start)
            count += 1

        # Calculer les moyennes
        avg_seq_time = sum(seq_times) / len(seq_times)
        avg_par_time = sum(par_times) / len(par_times)

        # Afficher les résultats
        print(f"Moyenne du temps d'exécution séquentielle (sur {runs} runs): {avg_seq_time:.7f} secondes")
        print(f"Moyenne du temps d'exécution parallèle (sur {runs} runs): {avg_par_time:.7f} secondes")

        # Comparer les temps d'exécution
        if avg_seq_time > avg_par_time:
            print("Le mode parallèle est plus rapide que le mode séquentiel.")
        if avg_seq_time < avg_par_time:
            print("Le mode séquentiel est plus rapide que le mode parallèle.")
        else:
            print("Les modes séquentiel et parallèle ont des temps d'exécution égaux.")