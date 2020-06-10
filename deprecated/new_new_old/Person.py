from deprecated.Clock import Clock
from Enumeration import State, Action
import random


class Person:                                       # metoda id będzie służyć do identyfikacji
    def __init__(self, home_x=0, home_y=0):
        self.home: tuple = (home_x, home_y)                 # gdzie mieszka
        self.destination = (home_x, home_y)               # dokąd zmierza
        self.x_pos = home_x
        self.y_pos = home_y
        self.last_x_pos = 0
        self.last_y_pos = 0
        self.state: State = State.Susceptible     # jaki jest jego stan
        self.__vulnerability = 0.1                  # jaka szansa że umrze
        self.is_busy = False                      # czy jest zajęty (nie można wyznaczyć nowego celu podróży)
        self.__timeout = (0, 0, 0)                  # do kiedy nie może podjąć kolejnego działania
        self.__study_prob = 100
        self.__party_prob = 20
        self.__sleep_prob = 20
        self.__action = None

    def check(self, clk):
        if self.is_busy and self.check_time(clk):
            self.__timeout = (0, 0, 0)
            self.is_busy = False
        self.check_schedule(clk)
        # self.check_if_in_destination(self.x_pos, self.x_pos, clk)

    def move(self, x, y):
        self.last_x_pos = self.x_pos
        self.last_y_pos = self.y_pos
        self.x_pos = x
        self.y_pos = y

    def set_destination(self, x, y):
        self.destination = (x, y)

    def check_time(self, clk):
        if clk.get()[0] == self.__timeout[0]:
            if clk.get()[1] == self.__timeout[1]:
                if clk.get()[2] == self.__timeout[2]:
                    return True
        return False

    def check_schedule(self, clk: Clock):
        h, m, s = clk.get()
        if not self.is_busy:
            if 20 < h < 2:
                if self.__is_time_for_party():
                    self.is_busy = True
                    self.__action = Action.GoParty
                    return Action.GoParty
                if self.__is_time_for_sleep():
                    self.is_busy = True
                    self.__action = Action.GoSleep
                    return Action.GoSleep
            elif 8 < h < 18:
                if self.__is_time_for_study():
                    self.is_busy = True
                    self.__action = Action.GoStudy
                    return Action.GoStudy
            self.__action = Action.GoHome
            return Action.GoHome

    def check_if_arrived(self):
        if self.is_busy:
            if self.x_pos == self.destination[0]:
                if self.y_pos == self.destination[1]:
                    return True
        return False

    def update_location(self, clk):
        if not self.check_if_arrived() and self.is_busy:
            if self.__action == Action.GoHome:
                self.is_busy = False
                self.last_x_pos = 0
                self.last_y_pos = 0
                return True
            elif self.__action == Action.GoStudy:
                self.is_busy = True
                self.__timeout = (clk.get()[0]+1, clk.get()[1]+30, clk.get()[2])
                self.last_x_pos = 0
                self.last_y_pos = 0
                return True
            elif self.__action == Action.GoParty:
                self.is_busy = True
                r1 = random.randrange(2)
                r2 = random.randrange(30)
                self.__timeout = (clk.get()[0] + r1, clk.get()[1] + r2, clk.get()[2])
                self.last_x_pos = 0
                self.last_y_pos = 0
                return True
            elif self.__action == Action.GoSleep:
                self.is_busy = True
                r = random.randrange(6, 9)
                self.__timeout = (clk.get()[0] + r, clk.get()[1], clk.get()[2])
                self.last_x_pos = 0
                self.last_y_pos = 0
                return True
            return False

    def __is_time_for_party(self):
        r = random.randrange(100)
        if r <= self.__party_prob:
            return True
        return False

    def __is_time_for_study(self):
        r = random.randrange(100)
        if r <= self.__study_prob:
            return True
        return False

    def __is_time_for_sleep(self):
        r = random.randrange(100)
        if r <= self.__sleep_prob:
            return True
        return False
