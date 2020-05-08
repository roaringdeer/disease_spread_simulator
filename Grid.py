import random
from Enums import Move
import numpy as np
from Configuration import Configuration as cfg


class Grid:  # class representing grid
    def __init__(self, width: int = 1, height: int = 1, radius: int = 1, plane_type: str = 'hexagon'):
        self.__data = {}  # (i, j) -> data
        self.__hashmap_loc_by_id = {}
        self.__converted_coordinates = []
        if plane_type == 'hexagon':
            self.__make_hexagons_hexagon(radius)
        elif plane_type == 'rectangle':
            self.__make_hexagons_rectangle(width, height)
        self.__fill_moves()

    def __getitem__(self, item):
        return self.__data[item[0]][item[1]]

    def __make_data(self, i, j):
        try:
            self.__data[i]
        except KeyError:
            self.__data[i] = {}
        self.__data[i][j] = {}
        self.__data[i][j]['person'] = 0
        self.__data[i][j]['allowed_moves'] = [Move.NOPE]

    def __make_hexagons_rectangle(self, x_size, y_size) -> None:
        for j in range(-y_size, y_size):
            j_off = j//2
            for i in range(-j_off, x_size - j_off):
                self.__make_data(i, j)

    def __make_hexagons_hexagon(self, radius) -> None:
        for i in range(-radius, radius+1):
            j1 = max(-radius, -i - radius)
            j2 = min(radius, -i + radius)
            for j in range(j1, j2+1):
                self.__make_data(i, j)

    @staticmethod
    def get_cartesian_coordinates(i, j):
        x = cfg.get("hex_size") * (np.sqrt(3) * i + np.sqrt(3) / 2 * j)
        y = cfg.get("hex_size") * (3. / 2 * j)
        return x, y

    def get_being_coordinates(self, being_id):
        return self.__hashmap_loc_by_id[being_id]

    def get_all_coordinates(self):
        to_return = []
        for key_i, nested_dict in self.__data.items():
            for key_j, values in nested_dict.items():
                to_return.append((key_i, key_j))
        return to_return

    def get_grid_in_cartesian(self):
        if not self.__converted_coordinates:
            cartesian = []
            for key_i, nested_dict in self.__data.items():
                for key_j, values in nested_dict.items():
                    x, y = self.get_cartesian_coordinates(key_i, key_j)
                    cartesian.append((x, y, values))
            return cartesian
        else:
            return self.__converted_coordinates

    @staticmethod
    def __get_all_moves(key_i, key_j):
        all_possible_moves = [
            [key_i + 1, key_j,      Move.E],
            [key_i - 1, key_j,      Move.W],
            [key_i,     key_j + 1,  Move.NE],
            [key_i - 1, key_j + 1,  Move.NW],
            [key_i + 1, key_j - 1,  Move.SE],
            [key_i,     key_j - 1,  Move.SW]
        ]
        return all_possible_moves

    def __fill_moves(self):
        for key_i, nested_dict in self.__data.items():
            for key_j, values in nested_dict.items():
                for move in self.__get_all_moves(key_i, key_j):
                    try:
                        self.__data[move[0]][move[1]]
                    except KeyError:
                        continue
                    else:
                        values['allowed_moves'].append(move[2])

    def __get_allowed_moves(self, i, j):
        return self.__data[i][j]['allowed_moves']

    def get_possible_moves(self, i, j):
        allowed_moves = self.__get_allowed_moves(i, j)
        neighbours = self.get_neighbours(i, j)
        for neighbour in neighbours:
            if neighbour[1] != 0:
                try:
                    allowed_moves.remove(neighbour[0])
                except ValueError:
                    continue
        return allowed_moves

    def get_being_id_at(self, i, j):
        try:
            return self.__data[i][j]['person']
        except KeyError:
            return 0

    def get_id(self, i, j):
        try:
            return list(self.__hashmap_loc_by_id.keys())[list(self.__hashmap_loc_by_id.values()).index((i, j))]
        except ValueError:
            return 0

    def get_neighbours(self, i, j):         # returns list of neighbours as [direction, Being.id]
        ij = self.__get_all_moves(i, j)
        return list(set([(x[2], self.get_being_id_at(x[0], x[1])) for x in ij]))

    def insert_population(self, population):
        grid_sample = random.sample(self.get_all_coordinates(), k=len(population))
        population_all = population.get_whole()
        for it in range(len(grid_sample)):
            i = grid_sample[it][0]
            j = grid_sample[it][1]
            being_id = population_all[it].id
            self.__data[i][j]['person'] = being_id
            self.__hashmap_loc_by_id[being_id] = (i, j)

    def move_being(self, being_id: int, direction: Move = Move.NOPE):
        i = self.__hashmap_loc_by_id[being_id][0]
        j = self.__hashmap_loc_by_id[being_id][1]
        if direction != Move.NOPE:
            move_coordinates = self.__get_all_moves(i, j)
            for move in move_coordinates:
                if move[2] == direction:
                    try:
                        temp1 = self.__data[move[0]][move[1]]['person']
                        temp2 = self.__data[i][j]['person']
                    except KeyError:
                        continue
                    else:
                        self.__data[move[0]][move[1]]['person'] = self.__data[i][j]['person']
                        self.__data[i][j]['person'] = 0
                        self.__hashmap_loc_by_id[being_id] = (move[0], move[1])
