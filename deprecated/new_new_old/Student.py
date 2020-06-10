import random

from Enumeration import State, Action


class Student:
    def __init__(self, home_x=0, home_y=0):
        self.home_x = home_x
        self.home_y = home_y
        self.dest_x = home_x
        self.dest_y = home_y
        self.x_pos = home_x
        self.y_pos = home_y
        self.last_pos = []
        self.state: State = State.Susceptible     # jaki jest jego stan
        self.__vulnerability = 0.1                  # jaka szansa że umrze
        self.is_busy = False                      # czy jest zajęty (nie można wyznaczyć nowego celu podróży)
        self.__timeout = (0, 0, 0)                  # do kiedy nie może podjąć kolejnego działania
        self.__study_prob = 100
        self.__party_prob = 20
        self.__sleep_prob = 20
        self.__action = None

    def animate(self, clk):
        if self.check_time(clk):
            self.__timeout = None
            self.is_busy = False
        if self.dest_x is not None:
            if self.dest_y is not None:
                if self.check_if_arrived():
                    self.is_busy = True
                    self.dest_x = None
                    self.dest_y = None
                    self.last_pos = []
                    if self.__action == Action.GoHome:
                        self.__home_timeout(clk)
                    elif self.__action == Action.GoSleep:
                        self.__sleep_timeout(clk)
                    elif self.__action == Action.GoStudy:
                        self.__study_timeout(clk)
                    elif self.__action == Action.GoParty:
                        self.__party_timeout(clk)

    def is_move_backwards(self, x, y):
        if (x, y) in self.last_pos:
            return True
        return False

    def move(self, next_x, next_y):
        self.last_pos = []
        self.x_pos = next_x
        self.y_pos = next_y

    def check_time(self, clk):
        if clk.get_h == self.__timeout[0]:
            if clk.get_m == self.__timeout[1]:
                return True
        return False

    def check_if_arrived(self):
        if self.x_pos == self.dest_x:
            if self.y_pos == self.dest_y:
                return True
        return False

    def go_party(self, dest):
        self.dest_x = dest[0]
        self.dest_y = dest[1]
        self.__action = Action.GoParty

    def go_study(self, dest):
        self.dest_x = dest[0]
        self.dest_y = dest[1]
        self.__action = Action.GoStudy

    def go_home(self):
        self.dest_x = self.home_x
        self.dest_y = self.home_y
        self.__action = Action.GoHome

    def go_sleep(self):
        self.dest_x = self.home_x
        self.dest_y = self.home_y
        self.__action = Action.GoSleep

    def get_new_activity(self, clk):
        h, m, s = clk.get()
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

    def __study_timeout(self, clk):
        rh = random.randrange(4)
        rm = random.randrange(59)
        self.__timeout = (clk.get_h() + 1, clk.get_m + 30, clk.get_s())

    def __party_timeout(self, clk):
        rh = random.randrange(2)
        rm = random.randrange(59)
        self.__timeout = (clk.get_h() + rh, clk.get_m + rm, clk.get_s())

    def __sleep_timeout(self, clk):
        rh = random.randrange(6, 11)
        rm = random.randrange(59)
        self.__timeout = (clk.get_h() + rh, clk.get_m + rm, clk.get_s())

    def __home_timeout(self, clk):
        rh = random.randrange(3)
        rm = random.randrange(59)
        self.__timeout = (clk.get_h() + rh, clk.get_m + rm, clk.get_s())