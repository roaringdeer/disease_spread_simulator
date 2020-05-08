import random
from Configuration import Configuration as cfg
from Enums import State
from Grid import Grid
from Society import Society


class Overseer:             # class responsible for simulation single grid
    def __init__(self):
        self.grid = Grid(cfg.get("width"), cfg.get("height"), cfg.get("radius"), plane_type=cfg.get("map_type"))
        self.society = Society()
        self.grid.insert_population(self.society)

    def tick(self):
        for being in self.society.get_whole():
            self.move_being(being.id)
            self.update_being_state(being.id)
        self.society.preview()

    def move_being(self, being_id):
        i, j = self.grid.get_being_coordinates(being_id)
        possible_moves = self.grid.get_possible_moves(i, j)
        move = random.choice(possible_moves)
        self.grid.move_being(being_id, move)

    def update_being_state(self, being_id):
        i, j = self.grid.get_being_coordinates(being_id)
        being = self.society.get_being(being_id)
        if being.state == State.Susceptible:
            for neighbour in self.grid.get_neighbours(i, j):
                if self.society.get_being(neighbour[1]).state == State.Infectious:
                    if self.is_susceptible_infected():
                        self.society.update_state(being_id, State.Infectious)
        elif being.state == State.Infectious:
            being.state_counter += 1
            if self.is_infected_deceased(being.state_counter):
                being.state = State.Deceased
            if self.is_infected_recovered(being.state_counter):
                being.state = State.Recovered

    def is_susceptible_infected(self):  # TODO probability of infection
        return True

    def is_infected_deceased(self, counter):     # TODO probability of death
        return False

    def is_infected_recovered(self, counter):    # TODO probability of recovery
        return False
