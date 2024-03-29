#modules
from Task import *
from Tasksystem import *
##############################################
class Main:
    ##############################################
    # Run functions #
    def run1():
        print("run 1 done")
    def run2():
        print("run 2 done")
    def run3():
        print("run 3 done")
    def run4():
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
    t2 = Task("t2", ["a"], ["b"])
    t3 = Task("t3", ["b"], ["c"])
    t4 = Task("t4", ["b"], ["d"])
    t5 = Task("t5", ["c"], ["e"])
    t6 = Task("t6", ["d"], ["f"])
    t7 = Task("t7", ["e", "f"], ["g"])
    ##############################################
    # Run functions association #
    t1.run = run1
    t2.run = run2
    t3.run = run3
    t4.run = run4
    t5.run = run5
    t6.run = run6
    t7.run = run7
    ##############################################
    # Task system #
    #dico={"t1": [], "t2": [t1], "t3": [t2], "t4": [t2]}
    ts = Tasksystem([t1, t2, t3, t4,t5,t6,t7], {})
    ts.dico = ts.createDep()
    test=ts.getRoad()
    test2=test[0]
    for test in test2:
        print(test.name)
    ##############################################
    # instruction #
    #road=ts.getDependencie(t4)
    #ts.run() # Run the tasks in the tasksystem with parallelism
    #ts.bernsteinIntoTasks() # Run the Bernstein test
    #ts.draw() # Draw the graph of the task system
    #ts.runseq() # Run the tasks in the tasksystem sequentially
    #ts.getDependencies() # Get the dependencies of the task system
    ##############################################

