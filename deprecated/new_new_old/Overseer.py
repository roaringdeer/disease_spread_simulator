import random
from deprecated.new_new_old import BMPReader
from deprecated.Clock import Clock
from Enumeration import Action
from deprecated.new_new_old.Person import Person


class Overseer:
    def __init__(self):
        self.agh_map, self.roads, self.campus_buildings, self.party_zones, self.dormitories = BMPReader.get_map_as_dict()
        self.population: dict = {}

        new = Person(7, 23)
        self.population[id(new)] = new

        # self.__make_population()
        self.clk = Clock(30)

    def tick(self):
        self.clk.tik_tok()
        for person_id, person in self.population.items():
            if person.check_time(self.clk) and person.check_if_arrived():
                person.is_busy = False
            if not person.is_busy:
                act = person.check_schedule(self.clk)
                if act == Action.GoHome or act == Action.GoSleep:
                    person.destination = person.home
                elif act == Action.GoParty:
                    person.destination = random.choice(list(self.party_zones.keys()))
                elif act == Action.GoStudy:
                    person.destination = random.choice(list(self.campus_buildings.keys()))
                allowed_tiles = self.__get_allowed_tiles(person.x_pos, person.y_pos, person.last_x_pos, person.last_y_pos)
                next_hop = self.__get_next_place(person.x_pos, person.y_pos, allowed_tiles)
                person.move(next_hop[0], next_hop[1])
            print(person.x_pos, person.y_pos, end=" ")

        print()

        # print(self.__get_allowed_tiles(97, 34))
        # print(self.__get_next_place(95, 33, self.__get_allowed_tiles(97, 34)))

    def __make_population(self):
        for k, v in self.dormitories.items():
            while v.capacity > len(v.people_inside):
                new = Person(k[0], k[1])
                self.population[id(new)] = new
                v.people_inside.append(id(new))

    def __get_next_place(self, x, y, surroundings):
        min_cost = 100000000
        best = None
        for v in surroundings:
            cost = self.__get_distance(x, y, v[0], v[1])
            if cost < min_cost:
                best = v
                min_cost = cost
        return best

    def __get_allowed_tiles(self, x, y, last_x, last_y):
        vert = [(x + 1, y),
                (x, y - 1),
                (x, y + 1),
                (x - 1, y)]
        print(vert)
        try:
            vert.remove((last_x, last_y))
        except ValueError:
            pass
        output = []
        for v in vert:
            try:
                self.agh_map[v]
            except KeyError:
                pass
            else:
                output.append(v)
        print(output)
        return output

    def __get_distance(self, x1, y1, x2, y2):
        return (x2-x1)**2 + (y2-y1)**2
