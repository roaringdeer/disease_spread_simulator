from Clock import Clock
from Mast5G import Mast5G
import Configuration
import Plotter

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
    # list of collected data
    data_logger = []
    # simulation of all scenarios
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
        print(mast.log)


if __name__ == '__main__':
    main()
