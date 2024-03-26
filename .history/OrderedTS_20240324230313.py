from Tasksystem import *
from Task import *

class OrderedTS:
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
        tasks_passed=[]
        for task in self.parallel:
            for task2 in self.parallel:
                if task == task2 or task in tasks_passed or task2 in tasks_passed:
                    continue
                if task.bernstein(task2):
                    print("Bernstein passed between",task.name,"and",task2.name)
                else:
                    print("No Bernstein failed between",task.name,"and",task2.name)
            tasks_passed.append(task)
        self.parallel = tasks_passed
        
    def getDependencies(self):
        road = []