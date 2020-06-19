import Configuration
import Plotter
import TextLogger
from Mast5G import Mast5G

parameters = {"hygiene": 1,
              "probability_quarantine": 5,
              "adaptive": True}


def main():
    Configuration.display()
    Configuration.default()
    Configuration.mast_param["probability"]["quarantine"] = 10
    Configuration.display()
    Configuration.default()
    Configuration.display()


if __name__ == '__main__':
    main()
