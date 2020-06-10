from enum import Enum, auto


class State(Enum):
    Susceptible = auto()
    Infectious = auto()
    Recovered = auto()
    Deceased = auto()
    Inactive = auto()


class Neighbour(Enum):
    NOPE = 0
    E = 1
    W = 2
    NE = 3
    NW = 4
    SE = 5
    SW = 6


class Move(Enum):
    NOPE = 0
    E = 1
    W = 2
    NE = 3
    NW = 4
    SE = 5
    SW = 6
