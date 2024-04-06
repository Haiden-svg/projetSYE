# Description : Cette classe représente un système de tâches avec des dépendances entre elles. 

# Importation des bibliothèques (modules) nécessaires
from Task import *
from threading import Semaphore, Thread
import networkx as nx
import matplotlib.pyplot as plt
import time
import random
##############################################
#args: tks: liste de taks, dico: dictionnaire de dépendances vide par défaut
class Tasksystem:
        #constructor#
    def __init__(self, tks, dico):
        self.tasks = tks
        self.dico = dico
        self.verifyUniqueNames()
        self.verifyTaskNameDep()

##############################################
        
        # Verifier l'unicité des noms des tâches
    def verifyUniqueNames(self):
        task_names = []
        for task in self.tasks:
            task_names.append(task.name)
        if len(task_names) != len(set(task_names)): # Check if the total number of names matches the number of unique names
            raise ValueError("Error: Task names must be unique.")
        
##############################################
        
        # Verifier les noms des tâches dans les dépendances
    def verifyTaskNameDep(self):
        task_names = set()
        for task in self.tasks:
            task_names.add(task.name)
        for task_name, deps in self.dico.items():  # Parcourir les éléments du dictionnaire
            if task_name not in task_names: 
                raise ValueError(f"Erreur : La tâche '{task_name}' mentionnée dans les dépendances n'existe pas.")
            for dep in deps:
                if dep not in task_names:
                    raise ValueError(f"Erreur : La tâche dépendante '{dep}' de '{task_name}' n'existe pas dans la liste des tâches.")
                
##############################################
                
        # Dessiner le graphe des tâches
    def draw(self):
        G = nx.DiGraph()

        for task in self.tasks:
            G.add_node(task.name) # Ajouter un noeud pour chaque tâche

        for task in self.tasks:

            for t in self.dico[task.name]:

                if t == []: # Si la tâche n'a pas de dépendances,
                    continue  

                G.add_edge(t.name,task.name) # Ajouter un arc entre la tâche et ses dépendances

        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', font_weight='bold')
        plt.show()

##############################################
        
        # Liste des dépendances d'une tâche donnée
    def getDependeciesTS(self,task):
        return self.dico[task.name]      

##############################################  
    def getDependencie(self,task): # Donne la route avant la tâche
        dependances = [[]]
        x = 0
        runR=self.runRoad()
        for road in runR:
            dependances.append([]) #ajouter une nouvelle liste vide pour chaque itération pour eviter les erreurs
            dependances[x].extend(road)  # Ajouter les tâches de la route à la liste des dépendances
            x+=1

            if task in road:
                dependances.remove([]) # Supprimer la liste vide
                return dependances
        return 0   
    
##############################################   
    def runseqelementary(self,road): # Lance sequentiellement les tâches dans une route

        for task in road:
            task.run()
##############################################
    def runseq(self):               # Lance sequentiellement les tâches dans le système
        roads = self.runRoad()
        for road in roads:

            self.runseqelementary(road)
##############################################
    # Run the tasks in the tasksystem with parallelism but elementary function
    def runsem(self, toeffectue):
        sem = Semaphore(toeffectue.__len__())

        def run_task(task):
            task.run()
            sem.release()

        for task in toeffectue:
            sem.acquire()
            Thread(target=run_task, args=(task,)).start()
##############################################   
            
            # Run the tasks in the tasksystem with parallelism 
    def run(self):

        tasksII=self.runRoad()
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
        # Cout du parallelisme
    def parCost(self, runs=2):
        # Mesurer le temps d'exécution parallèle
        count = 0
        par_times = []
        seq_times = []
        dif_times = []
        while count < runs:
            start = time.time()
            self.run()
            end = time.time()
            par_times.append(end - start)
            start = time.time()
            self.runseq()
            end = time.time()
            seq_times.append(end - start)
            dif_times.append(seq_times[count] - par_times[count])
            count += 1
        # Calculer les moyennes
        avg_dif_time = sum(dif_times) / len(dif_times)
        print(f"Moyenne de la différence de temps d'exécution (sur {runs} runs): {avg_dif_time:.7f} secondes")
        # Afficher les résultats
        if avg_dif_time > 0:
            print("Le mode parallèle est plus rapide que le mode séquentiel.")
        if avg_dif_time < 0:
            print("Le mode séquentiel est plus rapide que le mode parallèle.")


    def printRoad(self):
        roads = self.runRoad()
        for road in roads:
            print([task.name for task in road])

    def printRoad2(self, roads):
        for road in roads:
            print([task.name for task in road])
    #####################################

    