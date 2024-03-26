from Tasksystem import *
from Task import *

class OrderedTask:
    tsks=([],{})
    before = [[]]
    after = [[]]
    parallel = [[]]
    def __init__(self,tsks):
        self.tsks=tsks
        self.before = [[]]
        self.after = [[]]

    def getOrderedTasks(self):
        tasks=self.tsks[0].copy()
        for i in range(100):
            for task in tasks:
                if task.bernstein(task) == False:
                    self.before[i].append(task)
                    tasks.remove(task)
                elif task.bernstein(task) == True:
                    self.after[i].append(task)
                    tasks.remove(task)
        return self.before,self.after