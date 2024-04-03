#modules
from Task import *
from Tasksystem import *
import time
##############################################
class Main:
    global a,b,c,d,e
    a,b,c,d,e=0,0,0,0,0
    ##############################################
    def detTestRnd(ts,num_trials=3):
        intTable = [[]]
        intTable.append([])
        for _ in range(num_trials):
            global a
            a = random.randint(1, 100)
            global b
            b = random.randint(1, 100)
            global c
            c = random.randint(1, 100)
            global d
            d = random.randint(1, 100)
            global e
            e = random.randint(1, 100)
                    # Rest of the code...
            print("-----------------------------------")  
            print("Testing for change... for",a,b,c,d,e)      
            for __ in range(2):
                print("les valeurs a compter=",a,b,c,d,e)
                run()
                if __ == 0:
                    intTable[0] = [a,b,c,d,e]
                else:  
                    intTable[1]=[a,b,c,d,e]

            if intTable[0] != intTable[1]:
                print("Non-determinism detected")
                print(intTable[0] ,"and", intTable[1])
                return False
            print("Compare",intTable[0] ,"and", intTable[1])
        print("The system is deterministic.")
        print("-----------------------------------")
        return True

    ##############################################
    # Run functions #
    def run1():
        global a
        a=a

    def run2():
        global b
        b=b+a

    def run3():
        global c
        c=c+b

    def run4():
        time.sleep(1)
        global d
        d=d+b

    def run5():
        global e
        e=e+b
        print(e, " = ", b,"+",e)
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
    ts.detTestRnd()
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
