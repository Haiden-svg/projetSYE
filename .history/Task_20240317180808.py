class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"Task: {self.name}, Priority: {self.priority}"