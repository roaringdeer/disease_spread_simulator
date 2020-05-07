from time import sleep

from Configuration import Configuration as cfg
from Plane import Plane, Hexagon
from Population import Population
from Drawer import Drawer


class Simulator:
    def __init__(self):
        self.iteration = 0
        cfg.load()
        self.plane = Plane(cfg.get("width"), cfg.get("height"), cfg.get("radius"), cfg.get("map_type"))
        self.population = Population()
        self.population.scatter(self.plane)
        self.drawer = Drawer()
        pass

    def tick(self) -> None:
        print("Iteration {}".format(self.iteration))
        self.iteration += 1
        self.report()
        print()
        # self.drawer.draw_hexes(self.plane.hexagons, self.population.population)
        for person in self.population.population:
            person.go_brr(self.population, self.plane.get_surrounding(person.coordinates))
        # print(self.population)
        # sleep(1)

    def report(self):
        print("SUSCEPTIBLE: {:>7}".format(self.population.get_susceptible_count()))
        print("INFECTIOUS:  {:>7}".format(self.population.get_infectious_count()))
        print("DECEASED:    {:>7}".format(self.population.get_deceased_count()))
        print("RECOVERED:   {:>7}".format(self.population.get_recovered_count()))
