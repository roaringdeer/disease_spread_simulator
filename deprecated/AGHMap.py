import random
from copy import deepcopy
from AGHGraph import AGHGraph
from deprecated.CampusBuilding import CampusBuilding
from deprecated.Dormitory import Dormitory
from deprecated.PartyZone import PartyZone
from deprecated.Road import Road
from deprecated.SportCentre import SportCentre
from Enumeration import NodeType


class AGHMap:
    def __init__(self):
        self.graph = AGHGraph()
        self.buildings = {}
        self.roads = {}
        self.connections = {}
        # self.__make_roads()
        # self.__make_buidings()

        # for k1, v1 in self.roads.items():
        #     for k2, v2 in v1.items():
        #         print(k1, k2, v2.length, v2.infectiousness)

    def __make_buidings(self):
        for k, v in self.graph.nodes.items():
            for vv in v:
                if k == NodeType.Dormitory:
                    self.buildings[vv] = Dormitory()
                elif k == NodeType.PartyZone:
                    self.buildings[vv] = PartyZone()
                elif k == NodeType.SportCentre:
                    self.buildings[vv] = SportCentre()
                elif k == NodeType.CampusBuilding:
                    self.buildings[vv] = CampusBuilding()

    def __make_roads(self):
        for k, v in self.graph.shortest_paths.items():
            for kk, vv in v.items():
                if self.graph.cost_matrix[k][kk] is not None:
                    if k not in self.roads:
                        self.roads[k] = {}
                    if k not in self.connections:
                        self.connections[k] = {}
                    if vv is not None:
                        self.roads[k][kk] = Road(k, kk, vv[0], vv[1])
                        self.connections[k][kk] = []

    def find_path(self, source, target):
        try:
            # print(self.graph.shortest_paths[source][target][0])
            return deepcopy(self.graph.shortest_paths[source][target][0])
        except TypeError:
            return []

    def get_party_node(self):
        return random.choice(self.graph.nodes[NodeType.PartyZone])

    def get_campus_building_node(self):
        return random.choice(self.graph.nodes[NodeType.CampusBuilding])

    def get_sport_node(self):
        return random.choice(self.graph.nodes[NodeType.SportCentre])
