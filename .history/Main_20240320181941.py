import networkx as nx
import matplotlib.pyplot as plt
from Graphics import Graphics
from Task import *
from Tasksystem import *

class Main:
    t1 = Task("t1", [], ["x"])
    t2 = Task("t2", ["x"], ["y"])
    t3 = Task("t3", ["y"], [])
    t4 = Task("t4", ["y"], ["z"])
     
    ts = Tasksystem([t1, t2, t3, t4])

    print(ts.tasks[0].name)