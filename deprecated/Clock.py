

class Clock:
    def __init__(self, step: int = 30):
        self.__hour = 8
        self.__minute = 0
        self.__second = 0
        self.__step = step

    def __str__(self):
        return "{}h {}min {}sec".format(self.__hour, self.__minute, self.__second)

    def tik_tok(self):
        self.__second += self.__step
        while not self.__is_time_valid():
            self.__overflow_time()
        print(self)

    def __is_time_valid(self):
        if self.__second < 60:
            if self.__minute < 60:
                if self.__hour < 24:
                    return True
        return False

    def __overflow_time(self):
        if self.__second >= 60:
            self.__minute += self.__second // 60
            self.__second = self.__second % 60
        if self.__minute >= 60:
            self.__hour += self.__minute // 60
            self.__minute = self.__minute % 60
        if self.__hour >= 24:
            self.__hour = self.__hour % 24

    def get_h(self):
        return self.__hour

    def get_m(self):
        return self.__minute

    def get_s(self):
        return self.__second

    def get(self):
        return self.__hour, self.__minute, self.__second
