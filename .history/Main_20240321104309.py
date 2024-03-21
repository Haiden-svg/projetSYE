import networkx as nx
import matplotlib.pyplot as plt
from Graphics import Graphics
from Task import *
from Tasksystem import *
class Main:
    t1 = Task("t1", ["e"], ["x"])
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], ["a"])
    t4 = Task("t4", ["y"], ["z"])
    dico={"t1": [], "t2": [], "t3": [t2], "t4": [t3,t2,t1]}
    ts = Tasksystem([t1, t2, t3, t4], dico)
    # Create a directed graph from the tasksystem
    ts.draw()
    value=ts.getDependecies("t4").name
    print(value)