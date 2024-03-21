class Task:
    name = ""
    reads = []
    writes = []
    run = None

    def __init__(nom, lis, ecrit):
        name = nom
        reads = lis
        writes = ecrit
