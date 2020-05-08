from Drawer import Drawer as drw
from Configuration import Configuration as cfg
from Overseer import Overseer


def main():
    cfg.load()                                      # load and show configuration values
    cfg.print_all()
    ov = Overseer()                                 # create overseer
    ov.society.preview()
    drw.draw_from_grid_WIP(ov.grid, ov.society)     # draw iteration 0
    for i in range(20):                             # simulate and draw concurrent iterations
        ov.tick()
        drw.draw_from_grid_WIP(ov.grid, ov.society)


if __name__ == '__main__':
    main()
