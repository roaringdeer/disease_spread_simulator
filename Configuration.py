
# class MetaConfiguration:
#     def __getitem__(cls, item):


class Configuration:
    __values = {}

    @staticmethod
    def get(attr):
        try:
            return Configuration.__values[attr]
        except KeyError:
            return 0

    @staticmethod
    def load(file_dir: str = "config.txt"):
        f = open(file_dir)
        for line in f:
            splitted = line.split()
            if len(splitted) != 0:
                if splitted[0] != '#':
                    if '.' in splitted[1]:
                        Configuration.__values[splitted[0]] = float(splitted[1])
                    else:
                        try:
                            Configuration.__values[splitted[0]] = int(splitted[1])
                        except ValueError:
                            Configuration.__values[splitted[0]] = splitted[1]

    @staticmethod
    def print_all():
        print("---------------Configuration---------------")
        for key, val in Configuration.__values.items():
            if isinstance(val, float):
                print("{:25}| {:>16}".format(key, val))
            else:
                print("{:25}| {:>16}".format(key, val))
        print("-------------------------------------------")

