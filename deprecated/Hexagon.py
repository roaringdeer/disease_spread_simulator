import numpy as np
from Configuration import Configuration as cfg
from deprecated.Point import Point


class Hexagon:

    def __init__(self, i: int = 0, j: int = 0, size: int = 1):
        self.coordinates = Point(i, j)

    def __str__(self):
        return "Hexagon@{}".format(self.coordinates)

    def __repr__(self):
        return self.__str__()

    def get_cartesian_coordinates(self):
        x = cfg.get("hex_size") * (np.sqrt(3) * self.coordinates.i + np.sqrt(3) / 2 * self.coordinates.j)
        y = cfg.get("hex_size") * (3. / 2 * self.coordinates.j)
        return x, y
