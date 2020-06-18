import Plotter
import TextLogger
from Mast5G import Mast5G


def main():
    mast = Mast5G()
    i = 0
    names = ["param_set_1",
             "param_set_2",
             "param_set_3",
             "param_set_4",
             "param_set_5",
             "param_set_6",
             "param_set_7",
             "param_set_8"]
    j = 0
    file_name = "{}_try_{}.txt".format(names[i], j)
    print(file_name)
    try:
        # while True:
        for xx in range(2):
            mast.tick()
    except RuntimeError:
        print(mast)
    except ValueError:
        print("Zła całkowita ilość studentów - coś poszło nie tak")
    # data_logger.append(mast.log)
    # try:
    #     Plotter.plot(i, mast.logged_values)
    # finally:
    #     pass

    TextLogger.write_to_file(file_name, mast.logged_values)


if __name__ == '__main__':
    main()
