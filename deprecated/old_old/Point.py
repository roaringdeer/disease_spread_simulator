
class Point:
    def __init__(self, i: int = 0, j: int = 0):
        self.i = i
        self.j = j

    def __eq__(self, other) -> bool:
        if self.i == other.i:
            if self.j == other.j:
                return True
        return False

    def __str__(self):
        return "({},{})".format(self.i, self.j)

    def __format__(self, format_spec):
        raw = self.__str__()
        return "{r:{f}}".format(r=raw, f=format_spec)

    def __add__(self, other):
        return Point(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return Point(self.i-other.i, self.j-other.j)
