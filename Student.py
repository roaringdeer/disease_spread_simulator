import random
from Configuration import student_param as sim_param
from Enumeration import State, Action


class Student:
    def __init__(self, home=0):
        self.home = home
        self.hygiene = sim_param["hygiene"]
        self.symptoms = sim_param["symptoms"]
        self.action = Action.GoHome
        self.path = []
        self.state = State.Susceptible
        self.infected_counter = random.randrange(sim_param["infected_counter"]["min"],
                                                 sim_param["infected_counter"]["max"])
        self.timeout = 0

    # wypisanie stanu studenta // do użycia w postaci print(student)
    def __str__(self):
        return "{} {} {} {}".format(self.home, self.timeout, self.path, self.action)

    # deinkrementacje liczników
    def tick(self):
        # deinkrementacja licznika akcji
        if self.timeout > 0:
            self.timeout -= 1
        # deinkrementacja licznika stanu
        if self.state == State.Infectious:
            if self.infected_counter > 0:
                self.infected_counter -= 1

    # aktualizacja stanu studenta
    def state_update(self, states_counted: dict, infectiousness):
        infectious = states_counted[State.Infectious]
        susceptible = states_counted[State.Susceptible]
        total = infectious + susceptible
        if infectious > 0:
            if self.state == State.Susceptible:
                if self.__is_infected(total, infectious, infectiousness):
                    self.state = State.Infectious

        # wyzdrowienie/smierc studenta
        if self.infected_counter == 0 and self.state == State.Infectious:
            if self.__is_recovered():
                self.state = State.Recovered
            else:
                self.state = State.Deceased

    # sprawdzenie czy dany student jest zarażony
    def __is_infected(self, total_count, infectious_count, infectiousness):
        random.seed()
        r = random.random()
        prob = 0
        if total_count > 0:
            prob = (infectious_count / total_count) * infectiousness * self.hygiene
        # print("prob", prob, r)
        if r < prob:
            # print('yay')
            return True
        # print('nay')
        return False

    # sprawdzenie czy dany student wyzdrowiał - prob[%] na wyzdrowienie, 100%-prob[%] na śmierć
    def __is_recovered(self):
        random.seed()
        r = random.random()
        prob = sim_param["probability"]["recovery"]
        if r < prob:
            return True
        return False
