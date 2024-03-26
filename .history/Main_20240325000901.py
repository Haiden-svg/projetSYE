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
    ##############################################
    # Tasks #
    t1 = Task("t1", ["e"], ["x"])
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], ["a"])
    t4 = Task("t4", ["y"], ["z"])
    ##############################################
    # Run functions association #
    t1.run = run1
    t2.run = run2
    t3.run = run3
    t4.run = run4
    ##############################################
    # Task system #
    dico={"t1": [], "t2": [t1], "t3": [t2], "t4": [t2]}
    ts = Tasksystem([t1, t2, t3, t4], dico)
    ##############################################
    # instruction #
    #road=ts.getDependencie(t4)

    tsordered=OrderedTS(ts,t4)
    before,parallel,after=tsordered.getOrderedTasks()
   # beforeOrdered=tsordered.recursiveDependencies(before)
    if beforeOrdered and isinstance(beforeOrdered[0], list) and beforeOrdered[0]:
        print(beforeOrdered[0][0].name)
    else:
        print("beforeOrdered is empty or the first element is not a list or is an empty list")
    print(beforeOrdered[2][0].name)
    #ts.run() # Run the tasks in the tasksystem with parallelism
    #ts.bernsteinIntoTasks() # Run the Bernstein test
    #ts.draw() # Draw the graph of the task system
    #ts.runseq() # Run the tasks in the tasksystem sequentially
    #ts.getDependencies() # Get the dependencies of the task system
    ##############################################

