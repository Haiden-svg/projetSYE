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
        
    def bernstein(self, other_task):
    # Lecture-écriture exclusives
        if set(self.writes) & set(other_task.writes):
            return False
        # Écriture-écriture exclusives
        if set(self.writes) & set(other_task.reads) or set(other_task.writes) & set(self.reads):
            return False
        return True