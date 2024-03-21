# Description: This file contains the Task class which is used to represent a task in the system.
class Task:
    # Attributes
    name = ""
    reads = []
    writes = []
    run = None

    # Constructor
    def __init__(self,nom, lis, ecrit):
        self.name = nom
        self.reads = lis
        self.writes = ecrit
        self.run = None
