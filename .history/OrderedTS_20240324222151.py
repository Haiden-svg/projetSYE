from Tasksystem import *
from Task import *

class OrderedTasks:
    tsks=([],{})
    before = []
    after = []
    parallel = []
    def __init__(self,tsks,task):
        self.tsks=tsks
        self.before = []
        self.after = []
        self.parallel = []
        self.task=task

    def getOrderedTasks(self):
        for task in self.tsks:
            if self.task.bernstein(task):
                self.parallel.append(task)
            elif self.task.bernstein(task) == False and task not in self.tsks[1][self.task.name]:
                self.after.append(task)
            elif self.task.bernstein(task) == False and task in self.tsks[1][self.task.name]:
                self.before.append(task)
        return self.before,self.parallel,self.after
  