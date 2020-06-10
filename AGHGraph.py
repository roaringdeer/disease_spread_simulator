import random
import sys
from copy import deepcopy
from Configuration import graph_param as sim_param
import ExcelReader as exr
from Enumeration import NodeType


class AGHGraph:
    def __init__(self):
        # wczytanie macierzy kosztów
        self.cost_matrix = exr.go()

        # wypisanie macierzy kosztów
        print("---------- COST MATRIX ----------")
        self.preview_cost_matrix()
        print("---------------------------------")

        # lista wierzchołków identyfikujących budynki (w. 0 to mieszkania poza akademikami)
        self.dormitories = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 13, 14, 15, 24, 36]
        self.campus_buildings = [18, 19, 20,
                                 21, 22, 23, 25, 26, 27, 28, 29, 30,
                                 31, 32, 33, 34, 35, 37, 38, 39, 40,
                                 41, 42, 43, 44, 45, 46, 47, 48]
        self.sport_centre = [5, 6, 16]
        self.party_zone = [12, 17]
        self.quarantine = ["quarantine"]

        # współczynnik zarażalności w zależności od miejsca
        self.place_infectiousness = {
            NodeType.Dormitory: sim_param["infectiousness"]["dormitory"],
            NodeType.CampusBuilding: sim_param["infectiousness"]["campus_building"],
            NodeType.SportCentre: sim_param["infectiousness"]["sport_centre"],
            NodeType.PartyZone: sim_param["infectiousness"]["party_zone"],
            NodeType.Road: sim_param["infectiousness"]["road"],
            NodeType.Quarantine: sim_param["infectiousness"]["quarantine"]
        }

        # stworzenie wszystkich tras za pomocą algorytmu Dijkstry
        self.shortest_paths = {}
        for i in range(len(self.cost_matrix)):
            if i not in self.shortest_paths:
                self.shortest_paths[i] = {}
            d = self.dijkstra(i)
            for j in range(len(d)):
                if i == j:
                    self.shortest_paths[i][j] = None
                else:
                    self.shortest_paths[i][j] = d[j]

        # wypisanie wszystkich ścieżek z kosztami
        # for k, v in self.shortest_paths.items():
        #     for kk, vv in v.items():
        #         if vv is not None:
        #             if 0 in vv[0]:
        #                 print("!!!!!!!!!!")
        #         print(k, kk, vv)

    # obliczenie najkrótszych ścieżek pomiędzy wierzchołkami
    # TODO - źle oblicza niektóre ścieżki, trzeba naprawić
    def dijkstra(self, src):
        dist = []
        prev = []
        queue = []
        vertex_set = set(i for i in range(len(self.cost_matrix)))
        # print(vertex_set)
        for v in vertex_set:
            dist.append(sys.maxsize)
            prev.append(None)
            queue.append(v)
        dist[src] = 0
        while len(queue) > 0:
            min_cost = sys.maxsize
            u = None
            for i in queue:
                if min_cost > dist[i]:
                    u = i
                    min_cost = dist[i]
            queue.pop(queue.index(u))
            neighbours = [self.cost_matrix[u].index(i) for i in self.cost_matrix[u] if i is not None]

            for v in neighbours:
                alt = dist[u] + self.cost_matrix[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        paths = [[i] for i in range(len(self.cost_matrix))]
        returner = []
        for u in set(i for i in range(len(self.cost_matrix))):
            if prev[u] is not None:
                v = prev[u]
                while v is not None:
                    paths[u].insert(0, v)
                    v = prev[v]
            returner.append((paths[u], dist[u]))
        #     print(u, paths[u])
        #
        # print(dist)
        # print(prev)
        return returner

    # sprawdzenie czy macierz kosztów jest symetryczna
    def is_symetric(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != matrix[i][j]:
                    return False
        return True

    # zwraca najkrótszą drogę pomiędzy dwoma wierzchołkami
    def find_path(self, source, target):
        try:
            # print(self.graph.shortest_paths[source][target][0])
            return deepcopy(self.shortest_paths[source][target][0])
        except TypeError:
            return []

    # metody zwracające losowe wierzchołki w zależności od klasyfikacji
    def get_party_node(self):
        return random.choice(self.party_zone)

    def get_campus_building_node(self):
        return random.choice(self.campus_buildings)

    def get_sport_node(self):
        return random.choice(self.sport_centre)

    # metoda zwracająca typ danego wierzchołka
    def get_node_type(self, location):
        if isinstance(location, str):
            if location in self.quarantine:
                return NodeType.Quarantine
        elif isinstance(location, tuple):
            return NodeType.Road
        elif isinstance(location, int):
            if location in self.dormitories:
                return NodeType.Dormitory
            elif location in self.campus_buildings:
                return NodeType.CampusBuilding
            elif location in self.party_zone:
                return NodeType.PartyZone
            elif location in self.sport_centre:
                return NodeType.SportCentre
        else:
            return None

    # metoda wypisująca macierz kosztów
    def preview_cost_matrix(self):
        for i in self.cost_matrix:
            for j in i:
                if j is None:
                    print("{:>5}".format("-"), end=" ")
                else:
                    print("{:>5}".format(j), end=" ")
            print()