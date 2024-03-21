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

    def __init__(nom, lis, ecrit):
        name = nom
        reads = lis
        writes = ecrit
