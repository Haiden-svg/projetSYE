#modules
from Task import *
from Tasksystem import *
##############################################
class Main:
    global a,b,c,d,e
    a=0
    b=0
    c=0
    d=0
    e=0
    ##############################################
    # Run functions #
    def run1():
        a=1
        return a
    def run2():
        b=a+10
        return b
    def run3():
        c=b+5
        return c
    def run4():
        d=b+1
        return d
    def run5():
        e=c+2

        print(e, " = ", c, " + 2")
        return e
    ##############################################
    # Tasks #
    t1 = Task("t1", [], ["a"])
    t2 = Task("t2", ["a"], ["b"])
    t3 = Task("t3", ["b"], ["c"])
    t4 = Task("t4", ["b"], ["d"])
    t5 = Task("t5", ["c"], ["e"])
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
    

    test=ts.getRoad()
    test2=test[3][3]
    print(test2.name)
    ##############################################
    # instruction #
    #road=ts.getDependencie(t4)
    #ts.run() # Run the tasks in the tasksystem with parallelism
    #ts.bernsteinIntoTasks() # Run the Bernstein test
    #ts.draw() # Draw the graph of the task system
    ts.runseq() # Run the tasks in the tasksystem sequentially
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
