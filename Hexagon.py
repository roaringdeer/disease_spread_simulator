import numpy as np
from Configuration import Configuration as cfg
from Point import Point


class Hexagon:

    def __init__(self, i: int = 0, j: int = 0, size: int = 1):
        self.size = cfg.get("hex_size")
        self.coordinates = Point(i, j)
        # self.person_id = 0

    def __str__(self):
        return "Hexagon<{}>@{}".format(self.size, self.coordinates)

    def __repr__(self):
        return self.__str__()

    def get_coordinates(self) -> tuple:
        return self.coordinates.i, self.coordinates.j

    def set_coordinates(self, i: int, j: int) -> None:
        self.coordinates.i = i
        self.coordinates.j = j

    def get_cartesian_coordinates(self):
        x = self.size * (np.sqrt(3) * self.coordinates.i + np.sqrt(3) / 2 * self.coordinates.j)
        y = self.size * (3. / 2 * self.coordinates.j)
        return x, y
