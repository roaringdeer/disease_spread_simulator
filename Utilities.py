from Enums import Neighbour
from Point import Point

# E = +1, 0
# W = -1, 0
# NE = 0, +1
# NW = -1, +1
# SE = +1, -1
# SW = 0, -1


def conv_point2enum(point1, point2):
    diff = point2 - point1
    if diff == Point(1, 0):
        return Neighbour.E
    elif diff == Point(-1, 0):
        return Neighbour.W
    elif diff == Point(0, 1):
        return Neighbour.NE
    elif diff == Point(-1, 1):
        return Neighbour.NW
    elif diff == Point(1, -1):
        return Neighbour.SE
    elif diff == Point(0, -1):
        return Neighbour.SW
    else:
        return Neighbour.NOPE


def get_surrounding_converted(point, collection):
    to_return = []
    for element in collection:
        to_return.append(conv_point2enum(point, element.coordinates))
    return list(set(to_return))
