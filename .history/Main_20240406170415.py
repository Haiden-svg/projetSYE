#modules
from Task import *
from Tasksystem import *
import time
##############################################
class Main:
    global a,b,c,d,e   #global variables
    a,b,c,d,e=0,0,0,0,0
##############################################
    def detTestRnd(ts):  #Test de déterminisme
        intTable = [[]]
        index=[]
        intTable.append([]) #Creation des tableaux a utiliser pour la comparaison

        #mise en place des variables globales randomiséess
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

                   
        index=[a,b,c,d,e]   
        print("-----------------------------------")
        for __ in range(2): #boucle pour les deux tests de déterminisme

            print("les valeurs a compter=",a,b,c,d,e)

            if __ == 0:
                ts.run()
                intTable[0] = [a,b,c,d,e]

            else:  
                a,b,c,d,e=index
                ts.run()
                intTable[1]=[a,b,c,d,e]

        if intTable[0] != intTable[1]:
            print("Non-determinism detected") #Si les deux tableaux sont différents, le système est non-déterministe
            print(intTable[0] ,"and", intTable[1])
            return False
        
        print("Compare",intTable[0] ,"and", intTable[1])
        print("The system is deterministic.") #Si les deux tableaux sont identiques, le système est déterministe
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
    # Les fonctions run pour les tasks #
    t1.run = run1
    t2.run = run2
    t3.run = run3
    t4.run = run4
    t5.run = run5
    ##############################################
    # Task system #
    ts = Tasksystem([t1, t2, t3, t4, t5], {}) 
    ts.dico = ts.createDep()
    ##############################################
    # Phase de test #
    ts.printRoad2( ts.getDependencie(t2))
    ts.printRoad()
    #detTestRnd(ts)
