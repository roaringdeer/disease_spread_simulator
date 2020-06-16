from Clock import Clock
from Mast5G import Mast5G
import Configuration
import Plotter
import TextLogger


def main():
    # parameters of each scenario
    # hygiene, probability of quarantine, right quarantine assessment modifier, wrong quarantine assessment modifier
    parameters = [[0.8, 0, 1, 0],
                  [0.5, 0, 1, 0],
                  [0.1, 0, 1, 0],
                  [0.5, 5, 0.1, 0],
                  [0.5, 5, 0.5, 0],
                  [0.5, 5, 1, 0],
                  [0.5, 5, 1, 0.5],
                  [0.5, 5, 1, 0.1]
                  ]
    names = ["param_set_1",
             "param_set_2",
             "param_set_3",
             "param_set_4",
             "param_set_5",
             "param_set_6",
             "param_set_7",
             "param_set_8"]

    # list of collected data
    data_logger = []
    # simulation of all scenarios

    for j in range(3):
        i = 0
        for parameter_set in parameters:

            mast = Mast5G()
            print()
            print("hygiene: {}\nAssertion probability {}\nCorrect assertion modifier {}\nWrong assertion modifier {}\n"
                  .format(parameter_set[0], parameter_set[1], parameter_set[2], parameter_set[3]))
            Configuration.student_param["hygiene"] = parameter_set[0]
            Configuration.mast_param["probability"]["quarantine"] = parameter_set[1]
            Configuration.mast_param["probability_modifier"]["right"] = parameter_set[2]
            Configuration.mast_param["probability_modifier"]["wrong"] = parameter_set[3]
            # Configuration.display()
            try:
                while True:
                # for i in range(500):
                    mast.tick()
            except RuntimeError:
                print(mast)
            except ValueError:
                print("Zła całkowita ilość studentów - coś poszło nie tak")
            data_logger.append(mast.log)
            Plotter.plot(mast.logged_values)
            file_name = "{}_try_{}.txt".format(names[i], j)
            TextLogger.write_to_file(file_name, mast.logged_values)
            i += 1
            print(mast.log)


if __name__ == '__main__':
    main()
