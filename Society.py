from Being import Being
from Configuration import Configuration as cfg
from Enums import State


class Society:
    def __init__(self, population_size: int = -1, initial_infected_num: int = -1):
        if population_size == -1:
            population_size = cfg.get('population_size')
        if initial_infected_num == -1:
            initial_infected_num = cfg.get('initial_infected_number')
        self.null_person = Being(0, State.Inactive)
        self.__population_hashmap = {}
        self.susceptible_count = 0
        self.infectious_count = 0
        self.deceased_count = 0
        self.recovered_count = 0
        self.__make_population_great_again(population_size, initial_infected_num)

    def __len__(self):
        return len(self.__population_hashmap)

    def get_whole(self):
        return list(self.__population_hashmap.values())

    def get_being(self, being_id):
        try:
            return self.__population_hashmap[being_id]
        except KeyError:
            return self.null_person

    def preview(self):
        print("Society:")
        for key, being in self.__population_hashmap.items():
            print(being)

    def __make_population_great_again(self, population_size, initial_infected_num):
        for i in range(population_size):
            if i < initial_infected_num:
                self.__population_hashmap[i + 1] = Being(i + 1, State.Infectious)
            else:
                self.__population_hashmap[i + 1] = Being(i + 1, State.Susceptible)

    def update_state(self, being_id, state):
        self.__population_hashmap[being_id].state = state
