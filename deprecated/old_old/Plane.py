import random
from typing import List
import Utilities as util
from deprecated.new_old.Enums import Neighbour
from Hexagon import *


class Plane:

    def __init__(self, width: int = 1, height: int = 1, radius: int = 1, plane_type: str = 'hexagon'):
        self.hexagons = []

        if plane_type == 'hexagon':
            self.__make_hexagons_hexagon(radius)
        elif plane_type == 'rectangle':
            self.__make_hexagons_rectangle(width, height)

    def __make_hexagons_rectangle(self, x_size, y_size) -> None:
        for j in range(-y_size, y_size):
            j_off = j//2
            for i in range(-j_off, x_size - j_off):
                self.hexagons.append(Hexagon(i, j))

    def __make_hexagons_hexagon(self, radius) -> None:
        for i in range(-radius, radius+1):
            j1 = max(-radius, -i - radius)
            j2 = min(radius, -i + radius)
            for j in range(j1, j2+1):
                self.hexagons.append(Hexagon(i, j))

    def get_surrounding(self, point) -> List[Neighbour]:
        return util.get_surrounding_converted(point, self.hexagons)

    def get_random_hexes(self, hex_num):
        return random.sample(self.hexagons, k=hex_num)
