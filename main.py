import Drawer
from Enums import Neighbour, State
from Hexagon import *
from Person import Person
from Configuration import Configuration as cfg
from Population import Population
from Simulator import Simulator
import Utilities as util


def main():
    cfg.load()
    cfg.print_all()

    hexes = [Person(i=0, j=0),
             Person(i=0, j=-5),
             Person(i=5, j=-5),
             Person(i=-4, j=5)]

    # person = Person(i=0, j=0)
    # for i in range(10):
    #     print(person.go_brr(hexes).name)

    # pop = Population()
    # pop.get_by_id(4).state = State.Deceased
    # pop.get_by_id(5).state = State.Recovered
    # print(pop)

    sim = Simulator()
    # print(sim.population)
    # d = Drawer.Drawer()
    # d.draw_hexes(sim.plane.hexagons, hexes)
    # print(util.get_surrounding(hexes[1].coordinates, sim.plane.hexagons))
    # sim.tick()
    # sim.tick()
    for i in range(10):
        sim.tick()


if __name__ == '__main__':
    main()
