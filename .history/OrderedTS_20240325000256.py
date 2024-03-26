from Tasksystem import *
from Task import *

class OrderedTS:
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
            elif self.task.bernstein(task) == False and task not in self.tsks.dico[self.task.name]:
                self.after.append(task)
            elif self.task.bernstein(task) == False and task in self.tsks[1][self.task.name]:
                self.before.append(task)
        tasks_failed=[]
        for task in self.parallel:
            for task2 in self.parallel:
                if task == task2 or task in tasks_failed or task2 in tasks_failed:
                    continue
                if task.bernstein(task2)==False:
                    tasks_failed.append(task)
                    if task2 not in self.tsks[1][task.name]:
                        self.after.append(task2)
                    else:
                        self.before.append(task2)
        self.parallel = [task for task in self.parallel if task not in tasks_failed]

        return self.before,self.parallel,self.after

    def getDependenciesbefore(self,tasks):    
        road=[]
        tasks_failed=[]
        for task in tasks:
            for task2 in tasks:
                if task == task2 or task in tasks_failed or task2 in tasks_failed:
                    continue
                if task.bernstein(task2)==False:
                    tasks_failed.append(task)
        road=[task for task in tasks if task not in tasks_failed]           
        return road,tasks_failed
    
    def recursiveDependencies(self, tasks):
        road = [[]]
        tasks_failed = []
        while tasks_failed != []:
            tasks, tasks_failed = self.getDependenciesbefore(tasks)
            road.append(tasks)
        return road