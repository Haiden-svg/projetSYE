import networkx as nx
import matplotlib.pyplot as plt
from Task import *
from Tasksystem import *
class Main:
    t1 = Task("t1", ["e"], ["x"])
    def run1():

        print("++t1++")
    def run2():
        print("++t2++")
    def run3():
        print("++t3++")
    def run4():
        print("++t4++")
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], ["a"])
    t4 = Task("t4", ["y"], ["z"])
    t1.run = run1
    t2.run = run2
    t3.run = run3
    t4.run = run4
    dico={"t1": [t2], "t2": [t3], "t3": [], "t4": []}
    ts = Tasksystem([t1, t2, t3, t4], dico)
    ts.runseq()
