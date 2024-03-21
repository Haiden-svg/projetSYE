import threading
from threading import Semaphore
from time import sleep
from random import uniform
import networkx as nx
class Task:
    name = ""
    reads = []
    writes = []
    run = None

    def __init__(self,nom, lis, ecrit):
        self.name = nom
        self.reads = lis
        self.writes = ecrit
        self.run = None
