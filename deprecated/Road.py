

class Road:
    def __init__(self, source: int = 0, target: int = 1, path: list = None, length: int = 1):
        self.source = source
        self.target = target
        self.length = length
        self.capacity = length * 60
        self.infectiousness = len(path) / self.length * 100
        # print(self)

    def __str__(self):
        return "{}->{}: #{}/{}".format(self.source, self.target, self.length, self.infectiousness)
