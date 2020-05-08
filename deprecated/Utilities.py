from Enums import Move


# E = +1, 0
# W = -1, 0
# NE = 0, +1
# NW = -1, +1
# SE = +1, -1
# SW = 0, -1


def get_direction(i1, j1, direction):
    diff = (i2 - i1, j2 - j1)
    if diff == (1, 0):
        return Move.E
    elif diff == (-1, 0):
        return Move.W
    elif diff == (0, 1):
        return Move.NE
    elif diff == (-1, 1):
        return Move.NW
    elif diff == (1, -1):
        return Move.SE
    elif diff == (0, -1):
        return Move.SW
    else:
        return Move.NOPE