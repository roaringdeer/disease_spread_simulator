import Plotter
import TextLogger
from Mast5G import Mast5G


def main():
    mast = Mast5G()

    try:
        # while True:
        for i in range(1000):
            mast.tick()
    except RuntimeError:
        print(mast)
    except ValueError:
        print("Zła całkowita ilość studentów - coś poszło nie tak")
    Plotter.plot(mast.logged_values)
    TextLogger.write_to_file("test.txt", mast.logged_values)


if __name__ == '__main__':
    main()
0