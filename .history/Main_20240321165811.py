import networkx as nx
import matplotlib.pyplot as plt
from Task import *
from Tasksystem import *
##############################################
class Main:
    ##############################################
    def run1():
        print("run 1 done")
    def run2():
        print("run 2 done")
    def run3():
        print("run 3 done")
    def run4():
        print("run 4 done")
    ##############################################
    t1 = Task("t1", ["e"], ["x"])
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], ["a"])
    t4 = Task("t4", ["y"], ["z"])
    ##############################################
    t1.run = run1
    t2.run = run2
    t3.run = run3
    t4.run = run4
    ##############################################
    # Task system #
    dico={"t1": [t4,t3], "t2": [], "t3": [], "t4": []}
    ts = Tasksystem([t1, t2, t3, t4], dico)
    ##############################################
    # instruction #
    ts.run() # Run the tasks in the tasksystem with parallelism
    ts.draw() # Draw the graph of the task system
    #ts.runseq() # Run the tasks in the tasksystem sequentially
    ##############################################

