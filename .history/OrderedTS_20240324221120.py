from Tasksystem import *
from Task import *

class OrderedTask:
    task= None
    tsks=([],{})
    before = [[]]
    after = [[]]
    parallel = [[]]
    def __init__(self,tsks,task):
        self.tsks=tsks
        self.before = [[]]
        self.after = [[]]
        self.parallel = [[]]
        self.task=task

    def getOrderedTasks(self):
        tasks=self.tsks[0].copy()
        for i in range(100):
            for task in tasks:
                if task.bernstein(task):
                    self.parallel[i].append(task)
                    tasks.remove(task)
                elif task.bernstein(task) == False and task not in self.tsks[1][task.name]:
                    self.after[i].append(task)
                    tasks.remove(task)
                else:
                    self.before[i].append(task)
                    tasks.remove(task)
        return self.before,self.after