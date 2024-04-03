#modules
from Task import *
from Tasksystem import *
##############################################
class Main:
    ##############################################
    # Run functions #
    def run1():
        a=1
        print(a,"run 1 done")
        return a
    #def run1dup():
        #print("run 1 dup done")
    def run2(a):
        b=a+1
        print(b,"run 2 done")
        return b
    def run3(b):
        c=b+1
        print(c,"run 3 done")
        return c
    def run4(b):
        d=b+2
        print("run 4 done")
    def run5():
        print("run 5 done")
    def run6():
        print("run 6 done")
    def run7():
        print("run 7 done")
    ##############################################
    # Tasks #
    t1 = Task("t1", [], ["a"])
    #t1_dup = Task("t1", [], ["a"])
    t2 = Task("t2", ["a"], ["b"])
    t3 = Task("t3", ["b"], ["c"])
    t4 = Task("t4", ["b"], ["d"])
    t5 = Task("t5", ["c"], ["e"])
    t6 = Task("t6", ["d"], ["f"])
    t7 = Task("t7", ["e", "f"], ["g"])
    ##############################################
    # Run functions association #
    t1.run = run1
    #t1_dup.run = run1dup
    t2.run = run2
    t3.run = run3
    t4.run = run4
    t5.run = run5
    t6.run = run6
    t7.run = run7
    ##############################################
    # Task system #
    #dico={"t1": [], "t2": [t1], "t3": [t2], "t4": [t2]}
    ts = Tasksystem([t1, t2, t3, t4, t5, t6, t7], {}) 
    ts.dico = ts.createDep()
    ts.parCost()
    

    test=ts.getRoad()
    #test2=test[3][3]
    #print(test2.name)
    ##############################################
    # instruction #
    #road=ts.getDependencie(t4)
    #ts.run() # Run the tasks in the tasksystem with parallelism
    #ts.bernsteinIntoTasks() # Run the Bernstein test
    #ts.draw() # Draw the graph of the task system
    #ts.runseq() # Run the tasks in the tasksystem sequentially
    #ts.getDependencies() # Get the dependencies of the task system
    ##############################################








    ##############################################
    # test Verification de l'existence des noms de tâches dans le dictionnaire de précédence
    #try:
        #ts = Tasksystem([t1, t2, t3, t4, t5, t6, t7], {"t1": [], "t2": ["t1"], "t8": ["t2"]})
        #ts = Tasksystem([t1, t2, t3, t4, t5, t6, t7], {"t1": [], "t2": ["t9"]})
        #ts.dico = ts.createDep()
        #test = ts.getRoad()
        #ts.run() # Exécute le système de tâches avec parallélisme
    #except ValueError as e:
        #print(e)
    ##############################################
    # test Vérification des noms de tâches dupliqués
    #try:
        #ts = Tasksystem([t1, t1_dup, t2, t3, t4, t5, t6, t7], {"t1": [], "t2": ["t1"]})
        #ts.dico = ts.createDep()
        #test = ts.getRoad()
        #ts.run() # Exécute le système de tâches avec parallélisme
    #except ValueError as e:
        #print(e)
