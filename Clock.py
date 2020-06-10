

class Clock:
    def __init__(self, start_tick: int = 0):
        self.counter = start_tick
        self.minute_counter = 0
        self.hour_counter = 0
        self.day_counter = 0
        self.month_counter = 0
        self.year_counter = 0

    def tick(self):
        self.counter += 1
        self.hour_counter = self.counter // 654
        self.minute_counter = (self.counter % 654) * 60 // 654
        if self.counter > 15696:
            self.counter = 0
            self.day_counter += 1

    def __str__(self):
        return "#{:05} = days {:04} time {:02}:{:02}".format(
            self.counter, self.day_counter, self.hour_counter, self.minute_counter)
