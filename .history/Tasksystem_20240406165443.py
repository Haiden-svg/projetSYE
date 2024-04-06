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
    def runsem(self, toeffectue): # Lance les tâches dans une route avec parallélisme
        sem = Semaphore(toeffectue.__len__()) # Créer un sémaphore avec le nombre de tâches à effectuer

        def run_task(task): # Fonction pour exécuter une tâche
            task.run() # Exécuter la tâche
            sem.release() # Libérer le sémaphore

        for task in toeffectue: # Parcourir les tâches à effectuer
            sem.acquire() # Acquérir le sémaphore
            Thread(target=run_task, args=(task,)).start() # Démarrer un thread pour exécuter la tâche
##############################################   
    def run(self): # Lance les tâches dans le système avec parallélisme

        tasksII=self.runRoad() # Obtenir les routes
        for road in tasksII: # Parcourir les routes

            self.runsem(road) # Exécuter les tâches dans la route avec parallélisme
###############################################   
                
    def runRoad(self): # Obtenir les routes des tâches
        x = 0
        y= 0
        road = [[]]
        effectued = []
        tasks = self.tasks.copy()  # Copier la liste des tâches
        
        while x==0:
            toeffectue = [] # Liste des tâches à effectuer
            road.append([])     # Ajouter une nouvelle liste vide pour chaque itération pour éviter les erreurs
            
            for task in tasks: # Parcourir les tâches
                dependencies = self.getDependeciesTS(task) # Obtenir les dépendances de la tâche
                
                if all(dep in effectued for dep in dependencies) or dependencies == []: # Si toutes les dépendances sont effectuées
                    toeffectue.append(task) # Ajouter la tâche à la liste des tâches à effectuer
           
            if self.bernsteinIntoEachOverTest(toeffectue):
                road[y].extend(toeffectue) # Ajouter les tâches à la route
            y+=1  # Incrémenter le compteur de route parallèle
             
            for task in toeffectue:
                effectued.append(task) # Ajouter la tâche à la liste des tâches effectuées
                tasks.remove(task) # Supprimer la tâche de la liste des tâches à effectuer
            
            if all(task in effectued for task in self.tasks): # Si toutes les tâches sont effectuées
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

    