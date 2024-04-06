# Description: Cette classe représente une tâche dans un graphe de tâches.
class Task:
    # Attributes
    name = ""
    reads = [] #Les tâches lues
    writes = [] #Les tâches écrites
    run = None
    result = None

    # Constructor
    def __init__(self,nom, lis, ecrit):
        self.name = nom
        self.reads = lis
        self.writes = ecrit
        self.run = None
        self.result =None
        
    def bernstein(self, other_task):
    # Lecture-écriture exclusives
        if set(self.writes) & set(other_task.writes):
            return False
        # Écriture-écriture exclusives
        if set(self.writes) & set(other_task.reads) or set(other_task.writes) & set(self.reads):
            return False
        return True