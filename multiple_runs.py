from Clock import Clock
from Mast5G import Mast5G
import Configuration
import Plotter
import TextLogger


def main():
    # parameters of each scenario
    # hygiene, probability of quarantine, right quarantine assessment modifier, wrong quarantine assessment modifier
    # ideal tests

    parameters = {
        "kwarantanna": {"hygiene": 1,
                        "probability_quarantine": 9,
                        "adaptive": True},
        "lepsza_higiena": {"hygiene": 0.5,
                           "probability_quarantine": 0,
                           "adaptive": True},
        "odniesienie": {"hygiene": 1,
                        "probability_quarantine": 0,
                        "adaptive": False}}

    # names = ["param_set_1",
             # "param_set_2",
             # "param_set_3",
             # "param_set_4",
             # "param_set_5",
             # "param_set_6",
             # "param_set_7",
             # "param_set_8"]

    # list of collected data
    data_logger = []
    # simulation of all scenarios

    for i in range(3):
        for key, val in parameters.items():
            mast = Mast5G(val["adaptive"], val)
            try:
                while True:
                    mast.tick()
            except RuntimeError:
                print(mast)
            except ValueError:
                print("Zła całkowita ilość studentów - coś poszło nie tak")
            file_name = "{}_{}.txt".format(key, i)
            TextLogger.write_to_file(file_name, mast.logged_values)


if __name__ == '__main__':
    main()
