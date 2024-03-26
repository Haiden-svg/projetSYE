from Tasksystem import *
from Task import *

class OrderedTask:
    task= None
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
        tasks=self.tsks[0].copy()
  