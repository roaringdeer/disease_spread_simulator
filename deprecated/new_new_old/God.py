from deprecated.Clock import Clock
from Enumeration import Action
from deprecated.new_new_old.Student import Student


class God:
    def __init__(self):
        self.students_curr_it: dict = {}
        self.students_new_it = {}
        new = Student(7, 23)
        new.is_busy = True
        new.dest_x = 81
        new.dest_y = 24
        self.students_curr_it[7, 23] = [new]

        # self.__make_population()
        self.clk = Clock(30)

    def mind_control(self):
        for location, people in self.students_curr_it.items():
            for person in people:
                if person.is_busy:

                    print(person.dest_x, person.dest_y, location[0], location[1], person.last_pos)

                    new_move = self.__get_next_step(person.dest_x, person.dest_y,
                                                    location[0], location[1],
                                                    person.last_pos)
                    print(new_move)
                    if new_move is None:
                        for v in self.__get_nearby(location[0], location[1]):
                            if v[0] == location[0]:
                                if v[1] == location[1]:
                                    print("yay")
                                    break

                        person.last_pos = []
                        new_move = self.__get_next_step(person.dest_x, person.dest_y,
                                                        location[0], location[1],
                                                        person.last_pos)
                    if (new_move[0], new_move[1]) not in self.students_new_it:
                        self.students_new_it[new_move[0], new_move[1]] = []
                    person.last_pos.append((location[0], location[1]))
                    self.students_new_it[new_move[0], new_move[1]].append(person)

                    pass  # move person
                else:
                    act = person.get_new_activity(self.clk)
                    if act is Action.GoHome:
                        person.go_home()
                    if act is Action.GoSleep:
                        person.go_sleep()
                    if act is Action.GoStudy:
                        person.go_study(self.__get_dest_from_act(act))
                    if act is Action.GoParty:
                        person.go_party(self.__get_dest_from_act(act))
                    pass  # get new destination

        self.students_curr_it = self.students_new_it
        self.students_new_it = {}
