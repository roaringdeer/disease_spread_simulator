from enum import Enum, auto


class State(Enum):
    Susceptible = auto()
    Infectious = auto()
    Recovered = auto()
    Deceased = auto()
    Inactive = auto()


class NodeType(Enum):
    Dormitory = auto()
    CampusBuilding = auto()
    SportCentre = auto()
    PartyZone = auto()
    Road = auto()
    Quarantine = auto()


class TileType(Enum):
    Road = auto()
    Dormitory = auto()
    CampusBuilding = auto()
    PartyZone = auto()


class Action(Enum):
    GoHome = auto()
    GoStudy = auto()
    GoParty = auto()
    GoSleep = auto()
    GoSports = auto()
