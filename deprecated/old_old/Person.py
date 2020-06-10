from typing import List
from deprecated.new_old.Enums import State, Neighbour
from Hexagon import *
import Utilities as util
import random


class Person(Hexagon):

    def __init__(self, person_id: int = 0, state: State = State.Susceptible, i: int = 0, j: int = 0):
        super().__init__(i, j)
        self.id = person_id
        self.state = state
        self.__death_counter = 0

    def __str__(self):
        return "<id:{} state:{} coord:{}>".format(self.id, self.state.name, self.coordinates)

    def get_allowed_moves(self, people_around: List[Hexagon], available_hexes) -> list:
        if len(people_around) == 0:
            return [Neighbour.NOPE]
        moves = [x for x in available_hexes if x not in people_around]
        if len(moves) == 0:
            return [Neighbour.NOPE]
        return moves

    def is_infected(self, nearby) -> bool:
        if self.state == State.Susceptible:
            for person in nearby:
                if person.state == State.Infectious:
                    return True
        return False

    def go_brr(self, population, available_hexes):
        random.seed()
        # death_probability = self.__death_counter*cfg.get("mortality")//100
        nearby = population.get_people_near(self.coordinates)
        nearby_enum = util.point_list2enum(self.coordinates, [x.coordinates for x in nearby])
        moves = self.get_allowed_moves(nearby_enum, available_hexes)
        move = random.choice(moves)
        # move = moves[0]
        if self.state == State.Infectious:
            self.__death_counter += 1
        self.update_state(nearby)
        self.move(move)

    def update_state(self, surrounding):
        if self.is_infected(surrounding):
            self.state = State.Infectious

    def move(self, move):
        if move == Neighbour.E:
            self.move_e()
        elif move == Neighbour.W:
            self.move_w()
        elif move == Neighbour.NE:
            self.move_ne()
        elif move == Neighbour.NW:
            self.move_nw()
        elif move == Neighbour.SE:
            self.move_se()
        elif move == Neighbour.SW:
            self.move_sw()

    def move_e(self) -> None:       # E = +1, 0
        self.coordinates.i += 1

    def move_w(self) -> None:       # W = -1, 0
        self.coordinates.i -= 1

    def move_ne(self) -> None:      # NE = 0, +1
        self.coordinates.j += 1

    def move_nw(self) -> None:      # NW = -1, +1
        self.coordinates.i -= 1
        self.coordinates.j += 1

    def move_se(self) -> None:      # SE = +1, -1
        self.coordinates.i += 1
        self.coordinates.j -= 1

    def move_sw(self) -> None:      # SW = 0, -1
        self.coordinates.j -= 1

    def coord2move(self, target: Hexagon):
        return util.get_direction(target.coordinates, self.coordinates)
