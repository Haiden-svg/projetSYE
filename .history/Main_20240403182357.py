#modules
from Task import *
from Tasksystem import *
import time
##############################################
class Main:
    a,b,c,d,e=0,0,0,0,0 # Variables globales
    ##############################################
    # Run functions #
    def printest():
        print("test",a)
    def run1():
        #global a
        a=+1
        return a
    def run2():
        global b
        global a
        a=a+1
        b=a+10
        return b
    def run3():
        global c
        c=b+5
        return c
    def run4():
        time.sleep(1)
        global d
        d=b+1
        return d
    def run5():
        global e
        e=b+2

        print(e, " = ", b, " + 2")
        return e
    ##############################################
    # Tasks #
    t1 = Task("t1", [], ["a"])
    t2 = Task("t2", ["a"], ["b"])
    t3 = Task("t3", ["b"], ["c"])
    t4 = Task("t4", ["b"], ["d"])
    t5 = Task("t5", ["b"], ["e"])
    ##############################################
    # Run functions association #
    t1.run = run1
    #t1_dup.run = run1dup
    t2.run = run2
    t3.run = run3
    t4.run = run4
    t5.run = run5
    ##############################################
    # Task system #
    #dico={"t1": [], "t2": [t1], "t3": [t2], "t4": [t2]}
    ts = Tasksystem([t1, t2, t3, t4, t5], {}) 
    ts.dico = ts.createDep()
    #ts.parCost()
    #ts.parCost()
    ts.printRoad()
    ts.detTestRnd(a,b,c,d,e)
    printest()
    #test=ts.getRoad()
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
