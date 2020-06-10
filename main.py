from Clock import Clock
from Mast5G import Mast5G


def main():
    clk = Clock()
    mast = Mast5G()
    try:
        for i in range(15700):
            mast.tick()
    except RuntimeError:
        print(mast)
    except ValueError:
        print("Zła całkowita ilość studentów - coś poszło nie tak")
    print(mast.log)


if __name__ == '__main__':
    main()
