from Tasksystem import *
from Task import *

class OrderedTask:
    tsks=([],{})
    before = [[]]
    after = [[]]
    def __init__(self,tsks):
        self.tsks=tsks
        self.before = [[]]
        self.after = [[]]