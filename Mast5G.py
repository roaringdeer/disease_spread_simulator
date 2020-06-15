import random
from copy import copy, deepcopy
from AGHGraph import AGHGraph
from Clock import Clock
from Student import Student
from Enumeration import NodeType, Action, State
from Configuration import mast_param as sim_param


class Mast5G:
    def __init__(self):
        # stworzenie zegara
        self.clk = Clock(5232)  # 8:00

        # stworzenie grafu
        self.agh_graph = AGHGraph()

        # stworzenie słownika zawierającego informację odnośnie lokalizacji studentów
        self.__tracking_clear = {}
        self.__make_tracking()
        self.__tracking = deepcopy(self.__tracking_clear)

        # tworzę pysty slownik do resetowania wartosci odpowiedzialny za liczenie stanow w danym miejscu
        self.__infections_going_places_clear = {}
        self.__make_infections_going_places_clear()
        self.infections_going_places = deepcopy(self.__infections_going_places_clear)

        # inicjalizuje zmienne przechowujace informacje o ilosci zakazonych w calym grafie
        self.susceptible_count = 0
        self.infectious_count = 0
        self.recovered_count = 0
        self.deceased_count = 0

        # tworze studentow
        self.__total_student_count = 0
        self.sheeple = {}
        self.__make_sheeple()

        # inicjalizuje liste przechowujaca dane z kazdego dnia
        self.log = []

        # fragment kodu do testowania algorytmu dla pojedynczego studenta
        # print(self.__tracking)
        # n = Student()
        # self.sheeple[id(n)] = n
        # self.__tracking[0] = [id(n)]

    # Wypisanie informacji o stanie symulacji - używane jako podsumowanie symulacji
    def __str__(self):
        return "===\nElapsed: {} ticks ({} day {}h {}min)\nS: {}\nI: {}\nD: {}\nR: {}\n===".format(
            self.clk.counter, self.clk.day_counter, self.clk.hour_counter, self.clk.minute_counter,
            self.susceptible_count, self.infectious_count, self.deceased_count, self.recovered_count)

    # stworzenie pustego słownika wzorcowego do śledzenia studentów
    def __make_tracking(self):
        for i in range(len(self.agh_graph.cost_matrix)):
            self.__tracking_clear[i] = []
            for j in range(len(self.agh_graph.cost_matrix)):
                if self.agh_graph.cost_matrix[i][j] is not None:
                    self.__tracking_clear[i, j] = []
        self.__tracking_clear["quarantine"] = []
        self.__tracking_clear["graveyard"] = []

    # stworzenie studentów i rozłożenie ich po grafie
    def __make_sheeple(self):
        infected = sim_param["initial_infectious_count"]["dorms"]
        infected_outside = sim_param["initial_infectious_count"]["outside"]
        for dorm in self.agh_graph.dormitories:
            if dorm == 0:
                student_count = sim_param["student_count"]["outside"]
            else:
                student_count = sim_param["student_count"]["dorms"]
            for i in range(student_count):
                self.__total_student_count += 1
                new_sheep = Student(dorm)
                if infected > 0 and dorm != 0:
                    new_sheep.state = State.Infectious
                    infected -= 1
                if infected_outside > 0 and dorm == 0:
                    new_sheep.state = State.Infectious
                    infected_outside -= 1
                self.sheeple[id(new_sheep)] = new_sheep
                self.__tracking[dorm].append(id(new_sheep))

    # inicjalizacja slownika sluzacego do zliczania osob w danym wierzcholku/drodze
    def __make_infections_going_places_clear(self):
        for location in self.__tracking.keys():
            self.__infections_going_places_clear[location] = {State.Susceptible: 0,
                                                              State.Infectious: 0,
                                                              State.Recovered: 0}

    # wybranie nowego celu podrozy i zajecia dla każdego studenta
    def __control_sheeple_minds(self):
        for location, students in self.__tracking.items():
            # nowy cel dla studentów może zostać wybrany wyłącznie w wierzchołku
            if isinstance(location, int):
                for student_id in students:
                    # print(">", location)
                    # nowy cel może zostać wybrany tylko jeśli student nie jest niczym zajęcy (nie ma żadnej trasy do
                    # przebycia ani nie wykonuje żadnej czynności)
                    if len(self.sheeple[student_id].path) == 0 and self.sheeple[student_id].timeout == 0:
                        if self.__is_home_time():
                            self.sheeple[student_id].path = self.agh_graph.find_path(location, self.sheeple[student_id].home)
                            self.sheeple[student_id].action = Action.GoHome

                            # print('home')
                            # print(self.sheeple[student_id].path)

                        elif self.__is_sleep_time():
                            self.sheeple[student_id].path = self.agh_graph.find_path(location, self.sheeple[student_id].home)
                            self.sheeple[student_id].action = Action.GoSleep

                            # print('sleep')
                            # print(self.sheeple[student_id].path)

                        elif self.__is_party_time():
                            target = self.agh_graph.get_party_node()
                            self.sheeple[student_id].path = self.agh_graph.find_path(location, target)
                            self.sheeple[student_id].action = Action.GoParty

                            # print('party', target)
                            # print(self.sheeple[student_id].path)

                        elif self.__is_study_time():
                            target = self.agh_graph.get_campus_building_node()
                            self.sheeple[student_id].path = self.agh_graph.find_path(location, target)
                            self.sheeple[student_id].action = Action.GoStudy

                            # print('study', target)
                            # print(self.sheeple[student_id].path)

                        elif self.__is_sport_time():
                            target = self.agh_graph.get_sport_node()
                            self.sheeple[student_id].path = self.agh_graph.find_path(location, target)
                            self.sheeple[student_id].action = Action.GoSports

                            # print('sport', target)
                            # print(self.sheeple[student_id].path)

                        if len(self.sheeple[student_id].path) == 0:
                            self.sheeple[student_id].timeout = self.__get_timeout(self.sheeple[student_id].action)

                            # print('idle')
                            # print(self.sheeple[student_id].timeout)
                    # print(location, student_id, self.sheeple[student_id].path)

    # wykonanie jednej iteracji symulacji
    def tick(self):
        # przejście do kolejnego ticku symulacji
        self.clk.tick()

        # wybranie nowego celu dla studentow nic nie robiacych
        self.__control_sheeple_minds()

        # zliczanie i zarażanie studentów
        for location, students in self.__tracking.items():
            # pobranie ilości osób w danej lokacji
            states_counted = self.infections_going_places[location]
            for student_id in students:
                # deinkrementacja liczników studentów w danej lokacji
                self.sheeple[student_id].tick()
                # aktualizacja stanów dla studentów w danej lokacji
                # print(states_counted, self.agh_graph.place_infectiousness[
                #                                           self.agh_graph.get_node_type(location)])
                self.sheeple[student_id].state_update(states_counted,
                                                      self.agh_graph.place_infectiousness[
                                                          self.agh_graph.get_node_type(location)])
                # usunięcie osoby martwej z grafu
                if self.sheeple[student_id].state == State.Deceased and location != "graveyard":
                    self.__tracking[location].remove(student_id)
                    self.__tracking["graveyard"].append(student_id)
                    self.deceased_count += 1

        # przesuniecie studentow w kolejne miejsce jak tylko mozna
        self.__get_sheeple_to_move()

        # zliczenie wszystkich osób (do sprawdzenia poprawności wykonania symulacji)
        check_sum = self.susceptible_count + self.infectious_count + self.recovered_count + self.deceased_count

        # wypisanie aktualnego stanu symulacji w danym kroku
        print("{}\t | S: {:06} | I: {:06} | R: {:06} | D: {:06}| <FREE: {:06} | QUARANTINE: {:06}| GRAVEYARD: {:06}>".
              format(self.clk,
                     self.susceptible_count,
                     self.infectious_count,
                     self.recovered_count,
                     self.deceased_count,
                     self.__total_student_count-len(self.__tracking["quarantine"])-len(self.__tracking["graveyard"]),
                     len(self.__tracking["quarantine"]),
                     len(self.__tracking["graveyard"])))
        # print(self.__total_student_count, len(self.__tracking["quarantine"])+len(self.__tracking["graveyard"]))

        # dobowe zapisywanie stanu
        if self.clk.counter == 15696:
            print("Raport dobowy: ", self.clk, self.susceptible_count, self.infectious_count, self.recovered_count,
                  self.deceased_count)
            self.log.append([self.susceptible_count, self.infectious_count, self.recovered_count, self.deceased_count])

        # print(self.__tracking)

        # zakończenie jak już nic nie może się zarazić
        if self.infectious_count == 0:
            if self.recovered_count > 0 or self.deceased_count > 0:
                raise RuntimeError

        # zakończenie jeśli zaginął gdzieś student (suma studentów jest różna od początkowej liczby studentów)
        if check_sum != self.__total_student_count:
            raise ValueError

        # reset wartosci dla danej iteracji // self.deceased się nie zmienia, bo nie mogą zmartwychwstać
        self.susceptible_count = 0
        self.infectious_count = 0
        self.recovered_count = 0

    # przesuniecie studentow po grafie
    def __get_sheeple_to_move(self):
        # stworzenie słowników dla kolejnego kroku symulacji
        new_tracking = deepcopy(self.__tracking_clear)
        new_infection_map = deepcopy(self.__infections_going_places_clear)

        # iteracja po każdej lokalizacji na grafie
        for location in self.__tracking.keys():
            # iteracja po studentach w danym miejscu na grafie dopóki jeszcze jakiś w tym miejscu się znajduje
            while len(self.__tracking[location]) > 0:
                # zdjęcie ID studenta z listy
                student_id = self.__tracking[location].pop()

                # zliczanie studentow
                state = self.sheeple[student_id].state
                if state == State.Susceptible:
                    self.susceptible_count += 1
                    new_infection_map[location][State.Susceptible] += 1
                elif state == State.Infectious:
                    self.infectious_count += 1
                    new_infection_map[location][State.Infectious] += 1
                elif state == State.Recovered:
                    self.recovered_count += 1
                # sprawdzenie czy rozpatrywana lokalizacja jest kwarantanną lub cmentarzem
                if isinstance(location, str):
                    if location == "quarantine":
                        if self.sheeple[student_id].state == State.Recovered:
                            new_tracking[self.sheeple[student_id].home].append(student_id)
                        elif self.sheeple[student_id].state == State.Deceased:
                            new_tracking["graveyard"].append(student_id)
                        else:
                            new_tracking["quarantine"].append(student_id)
                    if location == "graveyard":
                        new_tracking["graveyard"].append(student_id)

                # sprawdzenie czy student moze przejść do drogi
                elif isinstance(location, int):
                    if self.sheeple[student_id].timeout <= 0:
                        if len(self.sheeple[student_id].path) > 1:
                            # poruszenie studenta
                            current_node = self.sheeple[student_id].path.pop(0)
                            next_node = self.sheeple[student_id].path[0]
                            new_tracking[current_node, next_node].append(student_id)
                            self.sheeple[student_id].timeout = self.agh_graph.cost_matrix[current_node][next_node]
                        else:
                            new_tracking[location].append(student_id)
                    else:
                        new_tracking[location].append(student_id)

                # sprawdzenie czy student moze przejść do wierzchołka
                elif isinstance(location, tuple):
                    to_node = location[1]
                    enter_building_flag = False
                    if self.sheeple[student_id].timeout <= 0:
                        # poruszenie studenta
                        if self.sheeple[student_id].path[-1] == to_node:
                            enter_building_flag = True
                            self.sheeple[student_id].path = []
                            self.sheeple[student_id].timeout = self.__get_timeout(self.sheeple[student_id].action)
                        if enter_building_flag:
                            if self.__is_quarantined(student_id) and to_node in self.agh_graph.campus_buildings:
                                new_tracking["quarantine"].append(student_id)
                            else:
                                new_tracking[to_node].append(student_id)
                        else:
                            new_tracking[to_node].append(student_id)
                    else:
                        new_tracking[location].append(student_id)
                else:
                    new_tracking[location].append(student_id)
        # nadpisanie słowników z poprzedniej iteracji
        self.__tracking = deepcopy(new_tracking)
        self.infections_going_places = deepcopy(new_infection_map)

    # zwraca czas ktory musi student przeczekac aby podjac kolejne dzialanie
    def __get_timeout(self, action):
        if action == Action.GoParty:
            return random.randrange(sim_param["timeout"]["party"]["min"], sim_param["timeout"]["party"]["max"])
        elif action == Action.GoSports:
            return random.randrange(sim_param["timeout"]["sport"]["min"], sim_param["timeout"]["sport"]["max"])
        elif action == Action.GoStudy:
            return random.randrange(sim_param["timeout"]["study"]["min"], sim_param["timeout"]["study"]["max"])
        elif action == Action.GoSleep:
            return random.randrange(sim_param["timeout"]["sleep"]["min"], sim_param["timeout"]["sleep"]["max"])
        elif action == Action.GoHome:
            return random.randrange(sim_param["timeout"]["home"]["min"], sim_param["timeout"]["home"]["max"])
        else:
            return sim_param["timeout"]["default"]

    # metody decydujace o akcji studenta
    def __is_party_time(self):
        modifier = sim_param["probability_modifier"]["party"]
        if 14388 < self.clk.counter < 15696 or 0 < self.clk.counter < 1308:
            modifier = 1
        random.seed()
        r = random.random() * 100 * modifier
        if r < sim_param["probability"]["action"]["party"]:
            return True
        return False

    def __is_study_time(self):
        modifier = sim_param["probability_modifier"]["study"]
        if 5232 < self.clk.counter < 11772:
            modifier = 1
        random.seed()
        r = random.random() * 100 * modifier
        if r < sim_param["probability"]["action"]["study"]:
            return True
        return False

    def __is_home_time(self):
        modifier = sim_param["probability_modifier"]["home"]
        random.seed()
        r = random.random() * 100 * modifier
        if r < sim_param["probability"]["action"]["home"]:
            return True
        return False

    def __is_sport_time(self):
        modifier = sim_param["probability_modifier"]["sport"]
        if 5232 < self.clk.counter < 11772:
            modifier = 1
        random.seed()
        r = random.random() * 100 * modifier
        if r < sim_param["probability"]["action"]["sport"]:
            return True
        return False

    def __is_sleep_time(self):
        modifier = sim_param["probability_modifier"]["sleep"]
        if 14388 < self.clk.counter < 15696 or 0 < self.clk.counter < 2616:
            modifier = 1
        random.seed()
        r = random.random() * 100 * modifier
        if r < sim_param["probability"]["action"]["sleep"]:
            return True
        return False

    # sprawdzenie czy student jest przeniesiony do kwarantanny
    def __is_quarantined(self, student_id):
        modifier = 1
        if self.sheeple[student_id].state == State.Infectious:
            modifier = sim_param["probability_modifier"]["quarantine"]["right"]
        elif self.sheeple[student_id].state == State.Susceptible:
            modifier = sim_param["probability_modifier"]["quarantine"]["wrong"]
        random.seed()
        r = random.random() * 100 * modifier
        prob = sim_param["probability"]["quarantine"]
        if r < prob:
            return True
        return False

    # zarażanie studenciaków
    # def __infect_people(self):
    #     for key, val in self.infections_going_places.items():
    #         if val[1] > 0:
    #             for student_id in self.__tracking[key]:
    #                 if self.sheeple[student_id].state == State.Susceptible:
    #                     if self.__is_infected(sum(val), val[1], 1):
    #                         self.sheeple[student_id].state = State.Infectious
    #         else:
    #             pass
