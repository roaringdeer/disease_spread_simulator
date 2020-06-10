from copy import deepcopy
from deprecated.new_old.Enums import State
from deprecated.new_new_old.Person import Person
from deprecated.new_new_old.Configuration import Configuration as cfg
from Plane import Plane, Point


class Population:
    def __init__(self, population_size: int = -1, initial_infected_num: int = -1):
        if population_size == -1:
            population_size = cfg.get('population_size')
        if initial_infected_num == -1:
            initial_infected_num = cfg.get('initial_infected_number')
        self.null_person = Person(0, State.Deceased)
        self.population = []
        self.make_population_great_again(population_size, initial_infected_num)

    def __str__(self):
        string = "-----------Population-----------\n"
        for person in self.population:
            string += person.__str__()
            string += "\n"
        string += "--------------------------------"
        return string

    def make_population_great_again(self, population_size, initial_infected_num):
        for i in range(population_size):
            if i < initial_infected_num:
                self.population.append(Person(i + 1, State.Infectious))
            else:
                self.population.append(Person(i + 1, State.Susceptible))

    def get_by_id(self, person_id):
        if person_id != 0:
            for person in self.population:
                if person.id == person_id:
                    return person
        return self.null_person

    def scatter(self, plane: Plane):
        hexes = plane.get_random_hexes(len(self.population))
        # print(hexes)
        for i in range(len(self.population)):
            # print(hexes[i])
            self.population[i].coordinates = deepcopy(hexes[i].coordinates)

    def get_people_near(self, point):
        to_return = []
        for person in self.population:
            diff = point - person.coordinates
            if diff == Point(1, 0):
                to_return.append(person)
            elif diff == Point(-1, 0):
                to_return.append(person)
            elif diff == Point(0, 1):
                to_return.append(person)
            elif diff == Point(-1, 1):
                to_return.append(person)
            elif diff == Point(1, -1):
                to_return.append(person)
            elif diff == Point(0, -1):
                to_return.append(person)
        return to_return

    def get_susceptible_count(self):
        count = 0
        for person in self.population:
            if person.state == State.Susceptible:
                count += 1
        return count

    def get_infectious_count(self):
        count = 0
        for person in self.population:
            if person.state == State.Infectious:
                count += 1
        return count

    def get_deceased_count(self):
        count = 0
        for person in self.population:
            if person.state == State.Deceased:
                count += 1
        return count

    def get_recovered_count(self):
        count = 0
        for person in self.population:
            if person.state == State.Recovered:
                count += 1
        return count
