import Plotter
import TextLogger
from Mast5G import Mast5G

parameters = {"odniesienie": {"hygiene": 1,
                                  "probability_quarantine": 0,
                                  "adaptive": False},
                  "lepsza_higiena": {"hygiene": 0.5,
                                     "probability_quarantine": 0,
                                     "adaptive": True},
                  "kwarantanna": {"hygiene": 1,
                                  "probability_quarantine": 5,
                                  "adaptive": True},
                  }


def main():
    mast = Mast5G(is_adaptive=True, adaptive_params=parameters["kwarantanna"])
    print(mast.is_adaptive)
    try:
        while True:
            mast.tick()
    except RuntimeError:
        print(mast)
    except ValueError:
        print("Zła całkowita ilość studentów - coś poszło nie tak")


if __name__ == '__main__':
    main()
