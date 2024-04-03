from Task import *
from threading import Semaphore, Thread
import networkx as nx
import matplotlib.pyplot as plt
import time
import random
import io
import sys
##############################################
#args: tks: list of tasks, dico: dictionnary of dependencies
class Tasksystem:
        #constructor#
    def __init__(self, tks, dico):
        self.tasks = tks
        self.dico = dico
        self.verifyUniqueNames()
        self.verifyTaskNameDep()

##############################################
        
        # Checking for duplicate task names
    def verifyUniqueNames(self):
        task_names = []
        for task in self.tasks:
            task_names.append(task.name)
        if len(task_names) != len(set(task_names)): # Check if the total number of names matches the number of unique names
            raise ValueError("Error: Task names must be unique.")
        
##############################################
        
        # Checking the existence of task names in the dictionary
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
        
        # get the dependencies of a task
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
    def runseqelementary(self,road):
        for task in road:
            #sem.acquire()
            task.run()
            #sem.release()

        # Run the tasks in the tasksystem sequentially
    def runseq(self):
        roads = self.runRoad()
        sem=Semaphore(1)
        for road in roads:
            self.runseqelementary(road)
##############################################
    def detTestRnd(self, num_trials=10):
        global a, b, c, d, e
        intTable = [[]]

        for _ in range(num_trials):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            c = random.randint(1, 100)
            d = random.randint(1, 100)
            e = random.randint(1, 100)
                    # Rest of the code...
            for __ in range(2):
                self.run()
                intTable.append([a, b, c, d, e])
            if intTable[1] != intTable[2]:
                print("Non-determinism detected")
                print(intTable[0] ,"and", intTable[1])
                return False
        print("The system is deterministic.")
        return True

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
    def parCost(self, runs=10):
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
    #####################################
        # Test Randomisé de déterministe 
    

    #methode 1

    """
    def detTestRnd(self, num_trials=10, num_executions=2):
    # Identifier toutes les variables uniques impliquées
        all_variables = set()
        for task in self.tasks:
            all_variables.update(task.reads)
            all_variables.update(task.writes)

    # Définir une fonction pour générer un jeu de valeurs aléatoires pour les variables
        def generate_random_values():
            return {var: random.randint(1, 100) for var in all_variables}

    # Fonction pour exécuter le système et collecter les résultats
        def execute_and_collect():
            self.run()
            return {var: globals()[var] for var in all_variables if var in globals()}

    # Tester avec num_trials jeux de données
        for _ in range(num_trials):
            dataset = generate_random_values()

        # Initialiser les variables globales
            for var, value in dataset.items():
                globals()[var] = value

        # Exécuter le système num_executions fois et collecter les résultats
            results = []
            for _ in range(num_executions):
            # Réinitialiser les variables avant chaque exécution
                for var, value in dataset.items():
                    globals()[var] = value

                result = execute_and_collect()
                results.append(result)

        # Vérifier la cohérence des résultats
            if not all(result == results[0] for result in results):
                print("Non-déterminisme détecté avec le jeu de données :", dataset)
                return False

        print("Le système est déterministe pour tous les jeux de données testés.")
        return True"""
    


    #methode 2
    
    """
    def detTestRnd(self, num_trials=10):
        for _ in range(num_trials):
            results = []
            for _ in range(2):  # Deux exécutions pour comparer
                # Rediriger la sortie standard pour capturer les impressions
                capturedOutput = io.StringIO()
                sys.stdout = capturedOutput
                self.run()  # Exécute les tâches
                sys.stdout = sys.__stdout__  # Restaurer la sortie standard
                results.append(capturedOutput.getvalue())

            # Vérifier si les résultats des deux exécutions sont identiques
            if results[0] != results[1]:
                print("Non-déterminisme détecté")
                return False

        print("Le système est déterministe.")
        return True"""
