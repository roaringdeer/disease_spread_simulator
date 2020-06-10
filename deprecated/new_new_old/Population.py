from deprecated.new_new_old.Person import Person


class Population:
    def __init__(self):
        self.__people: dict = {}

    def make_population(self, population_size: int):
        for i in range(population_size):
            new_person = Person()
            self.__people[id(new_person)] = new_person

    def get(self, person_id):
        pass
