from Enums import State


class Being:  # basic simulation unit, represents a human being
    def __init__(self, personal_id: int = 0, state: State = State.Susceptible):
        self.id = personal_id
        self.state_counter = 0
        self.state = state

    def __str__(self):
        return "<{:}|{:>}>".format(self.id, self.state.name)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.id == other.id:
            if self.state == other.state:
                if self.state_counter == other.state_counter:
                    return True
        return False
